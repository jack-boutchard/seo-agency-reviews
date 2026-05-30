#!/usr/bin/env python3
"""
Static-site generator for seo-agency-reviews.com.

This is a LOCAL BUILD TOOL only. It emits plain static HTML files that are
served directly by GitHub Pages. No server, no client-side rendering: every
byte of page content lives in the generated HTML at load time.

Run:  python3 build.py
"""
import html
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

SITE = {
    "name": "SEO Agency Reviews",
    "domain": "seo-agency-reviews.com",
    "base": "https://seo-agency-reviews.com",
    "tagline": "Independent, editorial reviews of SEO agencies.",
    "publisher": "SEO Agency Reviews",
    "email": "editor@seo-agency-reviews.com",
    "updated": "2026-05-30",
    "og_img": "/assets/img/og-default.svg",
}

# Editorial scoring model. Weights sum to 100.
CRITERIA = [
    ("results",      "Results & case studies",   30),
    ("strategy",     "Strategy & expertise",      20),
    ("transparency", "Transparency & reporting",  20),
    ("value",        "Pricing & value",           15),
    ("support",      "Communication & support",   15),
]
CRIT_LABEL = {k: l for k, l, _ in CRITERIA}
CRIT_WEIGHT = {k: w for k, _, w in CRITERIA}

# Populated by data module below.
AGENCIES = []        # list of dicts
AGENCY_BY_SLUG = {}
CATEGORIES = []
COMPARISONS = []


def e(s):
    return html.escape(str(s), quote=True)


def overall(agency):
    total = sum(agency["scores"][k] * w for k, _, w in CRITERIA)
    return round(total / 100, 1)


# --------------------------------------------------------------------------
# HTML scaffolding
# --------------------------------------------------------------------------
def jsonld(blocks):
    out = []
    for b in blocks:
        out.append(
            '<script type="application/ld+json">\n'
            + json.dumps(b, indent=2, ensure_ascii=False)
            + "\n</script>"
        )
    return "\n".join(out)


def breadcrumb_ld(trail):
    # trail: list of (name, url_path)
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": i + 1,
                "name": name,
                "item": SITE["base"] + path,
            }
            for i, (name, path) in enumerate(trail)
        ],
    }


def breadcrumb_html(trail):
    items = []
    for i, (name, path) in enumerate(trail):
        if i == len(trail) - 1:
            items.append(f'<li aria-current="page">{e(name)}</li>')
        else:
            items.append(f'<li><a href="{e(path)}">{e(name)}</a></li>')
    return (
        '<nav class="crumbs" aria-label="Breadcrumb"><ol>'
        + "".join(items)
        + "</ol></nav>"
    )


NAV = [
    ("Reviews", "/reviews/"),
    ("Best of", "/best/"),
    ("Methodology", "/methodology/"),
    ("Sources", "/sources/"),
    ("About", "/about/"),
]


def header_html(active=""):
    links = "".join(
        f'<li><a href="{e(p)}"{" aria-current=\"page\"" if active == p else ""}>{e(t)}</a></li>'
        for t, p in NAV
    )
    return f"""<header class="site-header">
  <div class="wrap">
    <a class="brand" href="/">SEO Agency <b>Reviews</b></a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="site-nav">Menu</button>
    <nav id="site-nav" class="site-nav" aria-label="Primary"><ul>{links}</ul></nav>
  </div>
</header>"""


def footer_html():
    rev_links = "".join(
        f'<li><a href="/reviews/{a["slug"]}/">{e(a["name"])}</a></li>'
        for a in AGENCIES[:6]
    )
    cat_links = "".join(
        f'<li><a href="/best/{c["slug"]}/">{e(c["h1"])}</a></li>'
        for c in CATEGORIES[:6]
    )
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <h4>SEO Agency Reviews</h4>
        <p class="small" style="color:#c2c8ff">{e(SITE['tagline'])} Editorial assessments by an
        independent publisher. We do not sell leads to the agencies we review.</p>
        <p class="small" style="color:#c2c8ff">Last updated {e(SITE['updated'])}.</p>
      </div>
      <div>
        <h4>Reviews</h4>
        <ul>{rev_links}<li><a href="/reviews/">All reviews →</a></li></ul>
      </div>
      <div>
        <h4>Best of &amp; info</h4>
        <ul>{cat_links}<li><a href="/best/">All categories →</a></li></ul>
      </div>
    </div>
    <div class="footer-bottom wrap" style="padding-left:0;padding-right:0">
      <p>
        <a href="/about/">About</a> ·
        <a href="/methodology/">Methodology</a> ·
        <a href="/sources/">Sources</a> ·
        <a href="/llms-info/">LLM info</a> ·
        <a href="/llms.txt">llms.txt</a> ·
        <a href="/sitemap.xml">Sitemap</a>
      </p>
      <p>© 2026 SEO Agency Reviews. Editorial content. Agency names and trademarks
      belong to their respective owners.</p>
    </div>
  </div>
</footer>"""


def page(path, title, description, body, ld=None, crumbs=None,
         active="", canonical=None, use_js=True):
    """Write one fully pre-rendered HTML file."""
    canonical = canonical or (SITE["base"] + path)
    ld = ld or []
    blocks = list(ld)
    if crumbs:
        blocks.append(breadcrumb_ld(crumbs))

    crumbs_html = breadcrumb_html(crumbs) if crumbs else ""
    js = '<script src="/assets/js/main.js" defer></script>' if use_js else ""

    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<link rel="canonical" href="{e(canonical)}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{e(SITE['name'])}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{e(canonical)}">
<meta property="og:image" content="{e(SITE['base'] + SITE['og_img'])}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(description)}">
<meta name="twitter:image" content="{e(SITE['base'] + SITE['og_img'])}">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/css/styles.css">
{jsonld(blocks)}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{header_html(active)}
<div class="wrap">{crumbs_html}</div>
<main id="main"><div class="wrap">
{body}
</div></main>
{footer_html()}
{js}
</body>
</html>
"""
    out_dir = os.path.join(ROOT, path.strip("/"))
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(doc)
    return path


def write_raw(relpath, content):
    full = os.path.join(ROOT, relpath)
    os.makedirs(os.path.dirname(full), exist_ok=True) if os.path.dirname(full) else None
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


# --------------------------------------------------------------------------
# Reusable content fragments
# --------------------------------------------------------------------------
def faq_html(faqs):
    if not faqs:
        return ""
    rows = "".join(
        f"<details><summary>{e(q)}</summary><div>{a}</div></details>"
        for q, a in faqs
    )
    return f'<section class="faq" id="faq"><h2>Frequently asked questions</h2>{rows}</section>'


def faq_ld(faqs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)},
            }
            for q, a in faqs
        ],
    }


def strip_tags(s):
    import re
    return re.sub(r"<[^>]+>", "", s).replace("  ", " ").strip()


def score_table(agency):
    rows = ""
    for k, label, w in CRITERIA:
        rows += (
            f"<tr><th scope=\"row\">{e(label)}</th>"
            f"<td>{agency['scores'][k]:.1f} / 10</td>"
            f"<td>{w}%</td></tr>"
        )
    rows += (
        f'<tr style="font-weight:700"><th scope="row">Weighted overall</th>'
        f'<td>{overall(agency):.1f} / 10</td><td>100%</td></tr>'
    )
    return f"""<div class="table-scroll"><table class="score-table">
<caption>Editorial scores — the publisher's assessment, not user ratings.</caption>
<thead><tr><th scope="col">Criterion</th><th scope="col">Score</th><th scope="col">Weight</th></tr></thead>
<tbody>{rows}</tbody></table></div>"""
