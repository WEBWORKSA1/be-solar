"""Build Be.Solar: python3 _build/build.py  (writes static HTML to the repo root)."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from guides_a import GUIDES_A
from guides_b import GUIDES_B
from guides_c import GUIDES_C
import pages_core as core
import pages_more as more

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
GUIDES = GUIDES_A + GUIDES_B + GUIDES_C
# Rewrite in-article links: guides use "../tools/..." and sibling "x.html" already.

out = {}
out["index.html"] = core.home(GUIDES)
out["get-quotes.html"] = core.quotes()
out.update(core.tools())
out["guides.html"] = more.guides_hub(GUIDES)
for g in GUIDES:
    out[f"guides/{g['slug']}.html"] = more.article(g, GUIDES)
out["incentives.html"] = more.incentives()
out["videos.html"] = more.videos()
out["support.html"] = more.support()
out["contests.html"] = more.contests()
out["careers.html"] = more.careers()
out["partners.html"] = more.partners()
out["about.html"] = more.about()
out["contact.html"] = more.contact()
out["glossary.html"] = more.glossary()
out["privacy.html"] = more.legal("privacy.html", "Privacy and cookie policy", "How Be.Solar collects, uses and protects information, and how ads and cookies work.", more.PRIVACY)
out["terms.html"] = more.legal("terms.html", "Terms of use", "Terms for using the Be.Solar website, calculators and quote service.", more.TERMS)
out["disclaimer.html"] = more.legal("disclaimer.html", "Disclaimer, trademark and copyright notice", "Be.Solar's trademark and copyright disclosure, advice disclaimer and advertising disclosure.", more.DISCLAIMER)

nf = more.not_found()
base_js = ("<script>document.write('<base href=\"'+(location.pathname.indexOf('/be-solar/')===0?'/be-solar/':'/')+'\">')</script>")
out["404.html"] = nf.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n' + base_js, 1)

for path, html in out.items():
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)

# sitemap
urls = [p for p in out if p != "404.html"]
prio = {"index.html": "1.0", "get-quotes.html": "0.9", "tools.html": "0.9", "guides.html": "0.8", "incentives.html": "0.9"}
with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for p in sorted(urls, key=lambda x: (x.count("/"), x)):
        loc = "https://be.solar/" + ("" if p == "index.html" else p)
        f.write(f"  <url><loc>{loc}</loc><lastmod>2026-10-21</lastmod><priority>{prio.get(p, '0.7')}</priority></url>\n")
    f.write("</urlset>\n")
print(f"Built {len(out)} pages")
