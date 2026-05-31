#!/usr/bin/env python3
"""
Resolve + scrape Clutch profiles for our agency roster, then distill the
public facts into clutch_facts.json (committed, attributed to Clutch).

- Reads FIRECRAWL_API_KEY from the environment ONLY (never hardcoded/printed).
- Raw scrapes are cached under clutch_data/ (gitignored) so reruns are cheap.
- Missing fields stay blank; nothing is invented.

Usage:
  python3 scrape_clutch.py --test          # parse the cached sample profile
  python3 scrape_clutch.py --run           # resolve+scrape all agencies
  python3 scrape_clutch.py --run --only "Siege Media,Directive"
"""
import json, os, re, sys, time, urllib.request, urllib.error

KEY = os.environ.get("FIRECRAWL_API_KEY", "")
RAW = "clutch_data"
FACTS = "clutch_facts.json"
LISTING_PARSED = "clutch_data/_listing_parsed.json"
os.makedirs(RAW, exist_ok=True)


def fc(endpoint, payload, timeout=90):
    req = urllib.request.Request(
        f"https://api.firecrawl.dev/v1/{endpoint}",
        data=json.dumps(payload).encode(),
        headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


# --------------------------------------------------------------------------
def parse_profile(md, name=""):
    rec = {}
    # Overall rating + review count
    m = re.search(r"Overall Review Rating\s*\n+\s*([0-5](?:\.\d)?)\s*\n+\s*\(\s*([\d,]+)\s*\)", md)
    if m:
        rec["rating"] = float(m.group(1))
        rec["reviews"] = int(m.group(2).replace(",", ""))
    else:
        m2 = re.search(r"Overall Review Rating\s*\n+\s*([0-5](?:\.\d)?)", md)
        if m2:
            rec["rating"] = float(m2.group(1))
    # Min project size
    m = re.search(r"Min(?:\.| project size)[^\n]*\n+\s*(\$[\d,]+\+?)", md)
    rec["min_project"] = m.group(1) if m else None
    # Hourly rate
    m = re.search(r"Hourly rate\s*\n+\s*(\$[\d,]+\s*-\s*\$[\d,]+|\$[\d,]+\+|Undisclosed)", md)
    rec["hourly"] = re.sub(r"\s+", " ", m.group(1)).strip() if m else None
    # Employees
    m = re.search(r"Employees\s*\n+\s*([\d,]+\s*-\s*[\d,]+|[\d,]+\+)", md)
    rec["employees"] = re.sub(r"\s+", " ", m.group(1)).strip() if m else None
    # Founded
    m = re.search(r"Founded\s*(\d{4})", md)
    rec["founded"] = m.group(1) if m else None
    # Primary location (first under Locations)
    m = re.search(r"Locations\s*\n+\s*([A-Z][A-Za-z .'\-]+,\s*[A-Z]{2})", md)
    if not m:
        m = re.search(r"\n([A-Z][A-Za-z .'\-]+,\s*[A-Z]{2})\s*\n", md[:1500])
    rec["location"] = m.group(1).strip() if m else None
    # "What Clients Have Said" summary
    m = re.search(r"What Clients Have Said\s*\n+\s*(.+?)\n", md)
    rec["summary"] = m.group(1).strip() if m and len(m.group(1).strip()) > 40 else None
    # Most common project size
    m = re.search(r"Most Common Project Size\s*\n+\s*\*\*([^*]+)\*\*\s*based on\s*([\d,]+)\s*reviews", md)
    if m:
        rec["common_project"] = m.group(1).strip()
    # Top mentions
    mm = re.search(r"Top Mentions\s*\n(.+?)\n###", md, re.S)
    if mm:
        rec["top_mentions"] = re.findall(r"-\s*([A-Za-z][^\n(]+\(\d+\))", mm.group(1))[:8]
    # Review highlights
    hi = re.search(r"Review Highlights\s*\n(.+?)\n## ", md, re.S)
    rec["highlights"] = []
    if hi:
        for hm in re.finditer(r"####\s*([^\n]+)\n+\s*([^\n]+)", hi.group(1)):
            rec["highlights"].append({"title": hm.group(1).strip(), "text": hm.group(2).strip()})
        rec["highlights"] = rec["highlights"][:4]
    # Sub-ratings
    subs = {}
    for label in ["Quality", "Schedule", "Cost", "Willing to Refer"]:
        sm = re.search(rf"-\s*{label}\s*\n+\s*([0-5](?:\.\d)?)", md)
        if sm:
            subs[label] = float(sm.group(1))
    if subs:
        rec["subratings"] = subs
    return rec


def search_profile(name):
    try:
        d = fc("search", {"query": f'{name} SEO agency clutch.co/profile', "limit": 6}, timeout=60)
    except Exception as ex:
        print(f"   search error for {name}: {ex}")
        return None
    cands = [r.get("url", "") for r in (d.get("data") or [])]
    cands = [u.split("#")[0].split("?")[0] for u in cands if "clutch.co/profile/" in u]
    if not cands:
        return None
    nn = norm(name)
    best, score = None, -1
    for u in cands:
        slug = u.rstrip("/").split("/")[-1]
        ns = norm(slug)
        s = 0
        if ns == nn: s = 100
        elif nn and (ns.startswith(nn) or nn.startswith(ns)): s = 80
        elif nn in ns or ns in nn: s = 60
        else:
            toks = set(re.findall(r"[a-z]+", name.lower()))
            s = 10 * sum(1 for t in toks if t and t in ns)
        if s > score:
            best, score = u, s
    return best if score >= 30 else None


def scrape_profile(url):
    slug = url.rstrip("/").split("/")[-1]
    cache = f"{RAW}/{slug}.json"
    if os.path.exists(cache):
        d = json.load(open(cache))
    else:
        d = fc("scrape", {"url": url, "formats": ["markdown"], "onlyMainContent": True})
        json.dump(d, open(cache, "w"))
    return ((d.get("data") or {}).get("markdown") or "")


# --------------------------------------------------------------------------
def run(only=None):
    sys.path.insert(0, ".")
    import generate
    names = [a["name"] for a in generate.B.AGENCIES] + [t[0] for t in generate.DIRECTORY]
    if only:
        only = {norm(x) for x in only}
        names = [n for n in names if norm(n) in only]

    listing = {}
    if os.path.exists(LISTING_PARSED):
        for e in json.load(open(LISTING_PARSED)):
            listing[norm(e["name"])] = e["url"]

    facts = json.load(open(FACTS)) if os.path.exists(FACTS) else {}
    for i, name in enumerate(names, 1):
        if name in facts and not facts[name].get("error") and not facts[name].get("_retry"):
            print(f"[{i}/{len(names)}] skip (cached): {name}")
            continue
        url = listing.get(norm(name)) or search_profile(name)
        if not url:
            facts[name] = {"clutch_url": None, "no_profile": True}
            print(f"[{i}/{len(names)}] NO PROFILE: {name}")
            json.dump(facts, open(FACTS, "w"), indent=1, ensure_ascii=False)
            time.sleep(1.0)
            continue
        try:
            md = scrape_profile(url)
            rec = parse_profile(md, name)
            rec["clutch_url"] = url
            facts[name] = rec
            print(f"[{i}/{len(names)}] OK: {name} -> {url.split('/')[-1]} "
                  f"rating={rec.get('rating')} reviews={rec.get('reviews')} founded={rec.get('founded')}")
        except Exception as ex:
            facts[name] = {"clutch_url": url, "error": str(ex)[:120]}
            print(f"[{i}/{len(names)}] ERROR: {name}: {ex}")
        json.dump(facts, open(FACTS, "w"), indent=1, ensure_ascii=False)
        time.sleep(1.2)
    print("DONE. facts written:", len(facts))


if __name__ == "__main__":
    if "--test" in sys.argv:
        md = json.load(open("clutch_data/_profile_sample.json"))["data"]["markdown"]
        print(json.dumps(parse_profile(md, "Siege Media"), indent=2, ensure_ascii=False))
    elif "--run" in sys.argv:
        only = None
        if "--only" in sys.argv:
            only = sys.argv[sys.argv.index("--only") + 1].split(",")
        run(only)
    else:
        print(__doc__)
