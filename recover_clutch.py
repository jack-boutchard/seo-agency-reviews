#!/usr/bin/env python3
"""Second pass: try to recover Clutch profiles for no_profile agencies.
Direct slug guesses (cheap, cached) + refined search, validated by name match.
Saves incrementally so interruptions never lose progress."""
import json, re, time
import scrape_clutch as S

facts = json.load(open("clutch_facts.json"))

SLUG_HINTS = {
    "The HOTH": ["the-hoth"], "FATJOE": ["fatjoe", "fat-joe"],
    "WebMechanix": ["webmechanix"], "Portent": ["portent"],
    "Vertical Leap": ["vertical-leap"], "Hallam": ["hallam-internet", "hallam"],
    "Reboot Online": ["reboot-online", "reboot-online-marketing"],
    "Nina Hale": ["nina-hale"], "New Breed": ["new-breed", "new-breed-marketing"],
    "Bluleadz": ["bluleadz"], "Embryo": ["embryo", "embryo-digital"],
    "Dejan Marketing": ["dejan-marketing", "dejanseo"],
    "Grow and Convert": ["grow-and-convert"], "Animalz": ["animalz"],
}

def guesses(name):
    base = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    out = SLUG_HINTS.get(name, []) + [base, base.replace("-and-", "-")]
    return list(dict.fromkeys(out))

def validate(md, name):
    if not md or len(md) < 2000:
        return False
    toks = [t for t in re.findall(r"[a-z]+", name.lower()) if len(t) > 2]
    head = md[:1500].lower()
    return sum(t in head for t in toks) >= max(1, (len(toks) + 1) // 2)

targets = [k for k, v in facts.items() if v.get("no_profile") and k != "Exalt Growth"]
print("targets:", targets, flush=True)
for name in targets:
    found = None
    for slug in guesses(name)[:3]:
        url = f"https://clutch.co/profile/{slug}"
        try:
            md = S.scrape_profile(url)
        except Exception as ex:
            continue
        if validate(md, name):
            found = (url, md); break
    if not found:
        u = S.search_profile(name)
        if u:
            try:
                md = S.scrape_profile(u)
                if validate(md, name):
                    found = (u, md)
            except Exception:
                pass
    if found:
        url, md = found
        rec = S.parse_profile(md, name); rec["clutch_url"] = url
        if rec.get("rating") or rec.get("founded") or rec.get("summary"):
            facts[name] = rec
            print(f"RECOVERED {name} -> {url.split('/')[-1]} rating={rec.get('rating')} founded={rec.get('founded')}", flush=True)
        else:
            print(f"weak {name} (no fields), keep no_profile", flush=True)
    else:
        print(f"none {name}", flush=True)
    json.dump(facts, open("clutch_facts.json", "w"), indent=1, ensure_ascii=False)
    time.sleep(0.8)

print("FINAL rating:", sum(1 for v in facts.values() if v.get("rating")),
      "| no_profile:", sum(1 for v in facts.values() if v.get("no_profile")), flush=True)
