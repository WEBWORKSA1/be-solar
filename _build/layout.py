"""Shared page chrome for Be.Solar. Every page gets the AdSense tag, the offer bar,
header, footer, consent notice and structured data. Links are relative so the site
works on a custom domain and on a GitHub Pages project path alike."""
import json

SITE = "https://be.solar"
NAME = "Be.Solar"
ADSENSE = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6620975821265271" crossorigin="anonymous"></script>'
OFFER_URL = "https://web.works/contact"

LOGO = ('<svg viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="17" r="8" fill="var(--sun)"/>'
        '<g stroke="var(--sun)" stroke-width="2.4" stroke-linecap="round"><path d="M20 3v3M8.5 8.5l2 2M31.5 8.5l-2 2M5 17h3M32 17h3"/></g>'
        '<path d="M6 27h28l-3 9H9z" fill="var(--cell)"/><path d="M13 27l-1 9M20 27v9M27 27l1 9M7.5 31.5h25" stroke="var(--paper)" stroke-width="1.2"/></svg>')

NAV = [
    ("tools.html", "Calculators"),
    ("guides.html", "Guides"),
    ("incentives.html", "Incentives"),
    ("videos.html", "Videos"),
    ("contests.html", "Contests"),
    ("support.html", "Support us"),
]


def page(*, path, title, desc, body, active="", schema=None, mobile_cta=True, noindex=False, extra_head=""):
    depth = path.count("/")
    r = "../" * depth
    canonical = SITE + "/" + ("" if path == "index.html" else path)
    nav = "".join(
        f'<a href="{r}{href}"{" aria-current=page" if active == href else ""}>{label}</a>' for href, label in NAV)
    ld = [{
        "@context": "https://schema.org", "@type": "Organization", "name": NAME, "url": SITE,
        "logo": SITE + "/assets/img/icon.svg",
    }]
    if schema:
        ld += schema if isinstance(schema, list) else [schema]
    ld_html = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    robots = '<meta name="robots" content="noindex,follow">' if noindex else '<meta name="robots" content="index,follow,max-image-preview:large">'
    mcta = (f'<div class="mobile-cta"><a class="btn" href="{r}get-quotes.html">Get free solar quotes</a></div>'
            if mobile_cta else "")
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
{robots}
<meta name="theme-color" content="#13293D">
<meta property="og:type" content="website"><meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary">
<meta name="google-adsense-account" content="ca-pub-6620975821265271">
<link rel="icon" href="{r}assets/img/icon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=Public+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/css/site.css">
{ADSENSE}
{ld_html}
{extra_head}
</head>
<body{' class="has-mcta"' if mobile_cta else ''}>
<a class="skip" href="#main">Skip to content</a>
<div class="offer">Interested in this website, the Be.Solar domain name, sponsorship, advertising or partnership? <a href="{OFFER_URL}" rel="noopener">Contact us</a></div>
<header class="site-head">
  <div class="wrap head-row">
    <a class="brand" href="{r}index.html" aria-label="Be.Solar home">{LOGO}<span>Be<b>.</b>Solar</span></a>
    <button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Main">{nav}<a class="btn" href="{r}get-quotes.html">Get free quotes</a>
      <button class="theme-btn" type="button" aria-label="Switch light or dark theme"><svg viewBox="0 0 24 24" width="18" height="18" style="margin:auto" aria-hidden="true"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12 4a8 8 0 0 1 0 16z" fill="currentColor"/></svg></button></nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="brand" href="{r}index.html">{LOGO}<span>Be<b>.</b>Solar</span></a>
        <p class="muted small" style="margin-top:12px">Independent solar math, plain-language guides and vetted installer quotes for homeowners in the US, Canada, UK, Australia and India.</p>
        <form class="inline-form js-form" data-subject="Newsletter signup" data-ok="You're on the list. One email a month, no spam.">
          <label class="hp">Leave empty<input name="_honey" tabindex="-1" autocomplete="off"></label>
          <input type="email" name="email" required placeholder="Email for the monthly solar brief" aria-label="Email address">
          <button class="btn" type="submit">Subscribe</button>
          <div class="form-msg" style="flex-basis:100%"></div>
        </form>
      </div>
      <div><h4>Plan</h4><ul>
        <li><a href="{r}tools/solar-savings-calculator.html">Savings calculator</a></li>
        <li><a href="{r}tools/system-size-calculator.html">System size</a></li>
        <li><a href="{r}tools/battery-backup-calculator.html">Battery backup</a></li>
        <li><a href="{r}tools/payback-roi-calculator.html">Payback &amp; ROI</a></li>
        <li><a href="{r}get-quotes.html">Get quotes</a></li></ul></div>
      <div><h4>Learn</h4><ul>
        <li><a href="{r}guides.html">All guides</a></li>
        <li><a href="{r}incentives.html">Incentives by country</a></li>
        <li><a href="{r}videos.html">Video library</a></li>
        <li><a href="{r}glossary.html">Solar glossary</a></li></ul></div>
      <div><h4>Community</h4><ul>
        <li><a href="{r}support.html">Support Be.Solar</a></li>
        <li><a href="{r}contests.html">Contests &amp; prizes</a></li>
        <li><a href="{r}careers.html">Work with us</a></li>
        <li><a href="{r}partners.html">Installers &amp; advertisers</a></li></ul></div>
      <div><h4>Company</h4><ul>
        <li><a href="{r}about.html">About</a></li>
        <li><a href="{r}contact.html">Contact</a></li>
        <li><a href="{r}privacy.html">Privacy &amp; cookies</a></li>
        <li><a href="{r}terms.html">Terms of use</a></li>
        <li><a href="{r}disclaimer.html">Disclaimer &amp; trademarks</a></li></ul></div>
    </div>
    <div class="legal-note">
      <p>© <span data-year>2026</span> Be.Solar, a Webworks Media Network property. Content is for general information and is not financial, tax, legal or engineering advice. Estimates are approximations; confirm with a licensed installer and your tax adviser.</p>
      <p>Be.Solar is an independent publication. It is not affiliated with, endorsed by or connected to any company, product or mark named "BeSolar", "Be Solar" or similar, or with any manufacturer, installer or government agency mentioned on this site. All third-party names and trademarks belong to their owners and are used only to identify products and programs. <a href="{r}disclaimer.html">Read the full disclosure</a>.</p>
    </div>
  </div>
</footer>
{mcta}
<div class="consent" role="dialog" aria-label="Cookie choices">
  <p>We use cookies for essential site functions and, with your choice, for analytics and ads served by Google that keep Be.Solar free. <a href="{r}privacy.html#cookies">How we use cookies</a></p>
  <div class="btns"><button class="btn" data-consent="all">Accept all</button><button class="btn ghost" data-consent="essential">Essential only</button></div>
</div>
<script src="{r}assets/js/site.js" defer></script>
</body>
</html>
"""


def quote_band(r):
    return f"""<section><div class="wrap"><div class="quote-band">
  <div><h2>See what installers near you would actually charge</h2>
  <p>Answer five quick questions. We match you with up to three vetted local installers. Free, no obligation, and you choose whether to talk to anyone.</p></div>
  <div><a class="btn" href="{r}get-quotes.html">Start my free quote</a><p class="small" style="margin-top:12px">Takes about 60 seconds.</p></div>
</div></div></section>"""
