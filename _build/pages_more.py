"""Guides, incentives, videos, community, company and legal pages."""
import re
from layout import page, quote_band

UPDATED = "October 21, 2026"
UPDATED_ISO = "2026-10-21"


def article(g, all_guides):
    r = "../"
    heads = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', g["body"])
    toc = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in heads)
    related = [x for x in all_guides if x["slug"] != g["slug"] and x["cat"] == g["cat"]][:3]
    if len(related) < 3:
        related += [x for x in all_guides if x["slug"] != g["slug"] and x not in related][:3 - len(related)]
    rel = "".join(f'<li><a href="{x["slug"]}.html">{x["title"]}</a></li>' for x in related)
    faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in g["faq"])
    body = f"""
<div class="wrap article">
  <article>
    <p class="crumbs"><a href="{r}index.html">Home</a> / <a href="{r}guides.html">Guides</a> / {g["cat"]}</p>
    <h1>{g["title"]}</h1>
    <p class="meta">By the Be.Solar editorial team. Updated {UPDATED}.</p>
    <p class="lede">{g["desc"]}</p>
    <div class="prose">{g["body"]}
    <h2 id="faq">Frequently asked</h2><div class="faq">{faq_html}</div>
    <div class="notice"><strong>Run your own numbers.</strong> Try the <a href="{r}tools/solar-savings-calculator.html">savings calculator</a>, then <a href="{r}get-quotes.html">compare up to three installer quotes</a>.</div>
    <p class="small muted">General information only, not financial, tax or legal advice. Incentives and rules change; confirm with official sources and a qualified professional. Spotted something out of date? <a href="{r}contact.html">Tell us</a>.</p>
    </div>
  </article>
  <aside><div class="toc panel"><h3 style="font-size:1.05rem">On this page</h3><ol>{toc}<li><a href="#faq">Frequently asked</a></li></ol>
  <hr style="border:0;border-top:1px solid var(--line);margin:16px 0">
  <h3 style="font-size:1.05rem">Related guides</h3><ul style="padding-left:1.1em;margin:0">{rel}</ul>
  <p style="margin-top:16px"><a class="btn" href="{r}get-quotes.html">Get free quotes</a></p></div></aside>
</div>
{quote_band(r)}"""
    schema = [{"@context": "https://schema.org", "@type": "Article", "headline": g["title"], "description": g["desc"],
               "dateModified": UPDATED_ISO, "datePublished": "2026-10-21",
               "author": {"@type": "Organization", "name": "Be.Solar editorial team"},
               "publisher": {"@type": "Organization", "name": "Be.Solar"},
               "mainEntityOfPage": f"https://be.solar/guides/{g['slug']}.html"},
              {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
                  {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in g["faq"]]},
              {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                  {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://be.solar/"},
                  {"@type": "ListItem", "position": 2, "name": "Guides", "item": "https://be.solar/guides.html"},
                  {"@type": "ListItem", "position": 3, "name": g["title"]}]}]
    return page(path=f"guides/{g['slug']}.html", title=f"{g['title']} | Be.Solar", desc=g["desc"], body=body,
                active="guides.html", schema=schema)


def guides_hub(guides):
    cats = []
    for g in guides:
        if g["cat"] not in cats:
            cats.append(g["cat"])
    blocks = ""
    for c in cats:
        rows = "".join(f'<a class="row" href="guides/{g["slug"]}.html"><h3>{g["title"]}</h3><p>{g["desc"]}</p><span class="go">Read</span></a>'
                       for g in guides if g["cat"] == c)
        blocks += f'<h2 style="margin-top:44px">{c}</h2><div class="rows">{rows}</div>'
    body = f"""<section class="page-head"><div class="wrap"><h1>Solar guides</h1><p class="lede">Plain-language answers on costs, incentives, financing, batteries and buying safely. Reviewed and updated as rules change.</p></div></section>
<section style="padding-top:0"><div class="wrap">{blocks}
<div class="notice" style="margin-top:36px">New words? The <a href="glossary.html">solar glossary</a> explains kW, kWh, PPA, STC, SEG and more in one line each.</div></div></section>{quote_band("")}"""
    return page(path="guides.html", title="Solar guides: costs, incentives, batteries and buying | Be.Solar",
                desc="Independent guides to home solar: costs, tax credits and subsidies by country, financing, batteries, net metering and avoiding scams.",
                body=body, active="guides.html")


def incentives():
    body = f"""<section class="page-head"><div class="wrap"><h1>Solar incentives by country</h1>
<p class="lede">Where things stand in October 2026, with links to the official sources. Rules change often; always confirm before you sign.</p></div></section>
<section style="padding-top:0"><div class="wrap">
<div class="table-wrap"><table>
<thead><tr><th>Country</th><th>Main homeowner incentive now</th><th>Status and deadlines</th><th>Our guide</th></tr></thead>
<tbody>
<tr><td><strong>United States</strong></td><td>No federal credit for homeowner-owned systems. Leases and PPAs may carry a commercial credit claimed by the provider. State, utility and local programs vary.</td><td>Residential credit (25D) unavailable for property placed in service after Dec 31, 2025. Commercial credit deadlines for third-party systems: begin construction by July 4, 2026 or be in service by end of 2027.</td><td><a href="guides/us-solar-tax-credit-2026.html">US tax credit guide</a></td></tr>
<tr><td><strong>India</strong></td><td>PM Surya Ghar central subsidy: ₹30,000/kW for the first 2 kW, ₹18,000 for the third kW, up to ₹78,000. Higher rates in special-category states.</td><td>Active. Apply through the national portal; domestic-content equipment required.</td><td><a href="guides/pm-surya-ghar-subsidy-guide.html">PM Surya Ghar guide</a></td></tr>
<tr><td><strong>United Kingdom</strong></td><td>0% VAT on installed residential solar and batteries; Smart Export Guarantee payments for exports.</td><td>0% VAT until 31 March 2027, then 5%. SEG rates set by suppliers; MCS certification usually required.</td><td><a href="guides/uk-solar-panels-guide.html">UK solar guide</a></td></tr>
<tr><td><strong>Australia</strong></td><td>STC discount on panels; Cheaper Home Batteries discount on batteries.</td><td>STC value falls each January until the scheme ends Dec 31, 2030. Battery certificates per kWh step down every six months and taper above 14 kWh.</td><td><a href="guides/australia-solar-rebates-stc-batteries.html">Australia rebates guide</a></td></tr>
<tr><td><strong>Canada</strong></td><td>No current federal homeowner solar grant or loan. Provincial, utility and municipal programs.</td><td>Greener Homes Grant closed; Greener Homes Loan fully committed. New affordability program focuses on heat pumps and insulation.</td><td><a href="guides/canada-solar-incentives-2026.html">Canada incentives guide</a></td></tr>
</tbody></table></div>

<h2 style="margin-top:48px">Official sources</h2>
<div class="grid g2">
<div class="panel"><h3>United States</h3><ul><li><a href="https://www.irs.gov/credits-deductions/residential-clean-energy-credit" rel="noopener" target="_blank">IRS: Residential Clean Energy Credit</a></li><li><a href="https://www.dsireusa.org/" rel="noopener" target="_blank">DSIRE database of state incentives</a></li><li><a href="https://pvwatts.nrel.gov/" rel="noopener" target="_blank">NREL PVWatts production estimator</a></li></ul></div>
<div class="panel"><h3>India</h3><ul><li><a href="https://pmsuryaghar.gov.in/" rel="noopener" target="_blank">PM Surya Ghar national portal</a></li><li><a href="https://mnre.gov.in/" rel="noopener" target="_blank">Ministry of New and Renewable Energy</a></li></ul></div>
<div class="panel"><h3>United Kingdom</h3><ul><li><a href="https://www.gov.uk/guidance/vat-on-energy-saving-materials-and-heating-equipment-notice-7086" rel="noopener" target="_blank">HMRC VAT Notice 708/6</a></li><li><a href="https://energysavingtrust.org.uk/advice/solar-panels/" rel="noopener" target="_blank">Energy Saving Trust: solar panels</a></li><li><a href="https://mcscertified.com/" rel="noopener" target="_blank">MCS: find a certified installer</a></li></ul></div>
<div class="panel"><h3>Australia</h3><ul><li><a href="https://cer.gov.au/" rel="noopener" target="_blank">Clean Energy Regulator</a></li><li><a href="https://www.cleanenergycouncil.org.au/" rel="noopener" target="_blank">Clean Energy Council</a></li></ul></div>
<div class="panel"><h3>Canada</h3><ul><li><a href="https://natural-resources.canada.ca/energy-efficiency/home-energy-efficiency/canada-greener-homes-initiative" rel="noopener" target="_blank">Natural Resources Canada: Greener Homes</a></li></ul></div>
<div class="panel sun"><h3>Know a program we missed?</h3><p>Utilities and cities launch programs all the time. Send us the link and we'll review it for the next update.</p><a href="contact.html">Suggest a program</a></div>
</div>
<p class="small muted" style="margin-top:28px">Last reviewed {UPDATED}. Be.Solar is not a government agency. Summaries are for general information and are not tax or legal advice.</p>
</div></section>{quote_band("")}"""
    return page(path="incentives.html", title="Solar incentives 2026: US, Canada, UK, Australia, India | Be.Solar",
                desc="Current solar incentives by country: US tax credit changes, India PM Surya Ghar subsidy, UK 0% VAT and SEG, Australian STCs and battery discounts, Canada programs.",
                body=body, active="incentives.html")


VIDEO_TOPICS = [
    ("How solar panels work", "how solar panels work explained"),
    ("Is home solar worth it?", "is home solar worth it real numbers"),
    ("Home battery backup explained", "home solar battery backup explained"),
    ("Net metering and export tariffs", "net metering explained solar"),
    ("What a solar installation looks like", "residential solar installation time lapse"),
    ("Cleaning panels safely", "how to clean solar panels safely"),
    ("Balcony and plug-in solar", "balcony solar plug in solar panels"),
    ("Microinverters vs string inverters", "microinverters vs string inverter"),
    ("PM Surya Ghar application walkthrough", "PM Surya Ghar apply online"),
]


def videos():
    rows = "".join(
        f'<a class="topic-link" href="https://www.youtube.com/results?search_query={q.replace(" ", "+")}" target="_blank" rel="noopener"><span>{t}</span><span class="muted small">Watch on YouTube</span></a>'
        for t, q in VIDEO_TOPICS)
    body = f"""<section class="page-head"><div class="wrap"><h1>Solar video library</h1><p class="lede">The clearest explainers we've found, plus curated YouTube searches for every stage of going solar.</p></div></section>
<section style="padding-top:0"><div class="wrap grid g2" style="align-items:start">
  <div><div class="video"><button class="yt-facade" data-yt="xKxrkht7CpY" aria-label="Play: How do solar panels work? (TED-Ed)"></button></div>
  <h2 style="margin-top:18px;font-size:1.4rem">How do solar panels work?</h2><p class="muted">TED-Ed, presented by Richard Komp. A five-minute animated primer on the photovoltaic effect, cells and panels. Videos load only when you press play.</p>
  <p><a href="guides/how-solar-panels-work.html">Read our companion guide</a></p></div>
  <div><h2 style="font-size:1.4rem">Browse by topic</h2>{rows}
  <p class="small muted" style="margin-top:14px">Topic links open YouTube search results in a new tab. Videos are produced by third parties; Be.Solar does not endorse any product or channel.</p></div>
</div></section>
<section class="band"><div class="wrap grid g2" style="align-items:center">
<div><h2>Make a solar video, win a prize</h2><p class="lede">Film your installation, your monitoring app after a year, or a clear explainer. Our monthly video contest pays cash and gear prizes.</p></div>
<div><a class="btn" href="contests.html">Enter the video contest</a></div></div></section>"""
    return page(path="videos.html", title="Solar video library: explainers on panels, batteries and installs | Be.Solar",
                desc="Curated solar videos: how panels work, batteries, net metering, installation, cleaning and subsidies.",
                body=body, active="videos.html")


def support():
    body = """<section class="page-head"><div class="wrap"><h1>Support independent solar advice</h1>
<p class="lede">Be.Solar is free to read. Reader support pays for data updates, new calculators, writers, contest prizes and outreach, and keeps our advice independent of any installer or manufacturer.</p></div></section>
<section style="padding-top:0"><div class="wrap">
<div class="grid g4" style="margin-bottom:32px">
  <div><h3 style="font-size:1.05rem">Operations</h3><p class="small muted">Hosting, data sources, fact-checking incentive changes every month.</p></div>
  <div><h3 style="font-size:1.05rem">Talent</h3><p class="small muted">Paying solar engineers, writers and translators to expand coverage.</p></div>
  <div><h3 style="font-size:1.05rem">Contests &amp; prizes</h3><p class="small muted">Funding cash and equipment prizes for students and creators.</p></div>
  <div><h3 style="font-size:1.05rem">Promotion</h3><p class="small muted">Reaching renters and first-time buyers who need unbiased guidance most.</p></div>
</div>
<div class="tiers">
  <div class="tier"><h3>Ray</h3><p class="amt">$5</p><ul><li>Our thanks, and a supporter shout-out in the monthly brief</li></ul><button class="btn ghost" data-amount="5" data-tier="Ray">Choose $5</button></div>
  <div class="tier featured"><span class="tag">Most chosen</span><h3>Panel</h3><p class="amt">$25</p><ul><li>Name on the supporters list</li><li>Early access to new tools</li></ul><button class="btn" data-amount="25" data-tier="Panel">Choose $25</button></div>
  <div class="tier"><h3>Array</h3><p class="amt">$100</p><ul><li>Everything in Panel</li><li>Vote on the next calculator or guide</li></ul><button class="btn ghost" data-amount="100" data-tier="Array">Choose $100</button></div>
  <div class="tier"><h3>Power plant</h3><p class="amt">$500+</p><ul><li>Named sponsor of a contest prize</li><li>Logo on the contest page</li></ul><button class="btn ghost" data-amount="500" data-tier="Power plant">Choose $500</button></div>
</div>

<div class="grid g2" style="margin-top:44px;align-items:start">
<div class="panel">
<h2 style="font-size:1.5rem">Pledge your support</h2>
<p class="muted">Tell us your amount and preferred payment method. We'll reply within two business days with a secure payment link and a receipt. One-time and monthly options are available.</p>
<form id="pledge-form" class="form js-form" data-subject="Donation pledge" data-ok="Thank you. Your pledge is in. We'll email a secure payment link within two business days.">
<label class="hp">Leave empty<input name="_honey" tabindex="-1" autocomplete="off"></label>
<input type="hidden" name="tier" value="">
<div class="two"><div class="field"><label for="p-amount">Amount (USD or equivalent)</label><input id="p-amount" name="amount" type="number" min="1" required></div>
<div class="field"><label for="p-freq">Frequency</label><select id="p-freq" name="frequency"><option>One-time</option><option>Monthly</option><option>Yearly</option></select></div></div>
<div class="two"><div class="field"><label for="p-name">Name</label><input id="p-name" name="name" required autocomplete="name"></div>
<div class="field"><label for="p-email">Email</label><input id="p-email" name="email" type="email" required autocomplete="email"></div></div>
<div class="field"><label for="p-method">Preferred payment method</label><select id="p-method" name="payment_method"><option>Card</option><option>PayPal</option><option>Bank transfer</option><option>UPI (India)</option><option>Other</option></select></div>
<div class="field"><label for="p-use">Direct my gift to (optional)</label><select id="p-use" name="direct_to"><option>Wherever it's needed most</option><option>Operations and data</option><option>Hiring writers and engineers</option><option>Contests and prizes</option><option>Promotion and outreach</option></select></div>
<label class="check"><input type="checkbox" name="public_credit" value="Yes"><span>List my name as a supporter.</span></label>
<button class="btn" type="submit">Send my pledge</button>
<div class="form-msg"></div>
</form></div>
<div>
<h2 style="font-size:1.5rem">Sponsor or partner instead</h2>
<p class="muted">Companies can sponsor a calculator, a guide series or a contest prize. Sponsorships are always labelled and never change our recommendations.</p>
<form class="form js-form panel" data-subject="Sponsorship inquiry" data-ok="Thanks. We'll send our sponsorship options within two business days.">
<label class="hp">Leave empty<input name="_honey" tabindex="-1" autocomplete="off"></label>
<div class="two"><div class="field"><label for="s-co">Company</label><input id="s-co" name="company" required></div><div class="field"><label for="s-name">Your name</label><input id="s-name" name="name" required></div></div>
<div class="field"><label for="s-email">Work email</label><input id="s-email" name="email" type="email" required></div>
<div class="field"><label for="s-int">Interested in</label><select id="s-int" name="interest"><option>Contest prize sponsorship</option><option>Calculator sponsorship</option><option>Guide series sponsorship</option><option>Newsletter sponsorship</option><option>Other partnership</option></select></div>
<div class="field"><label for="s-msg">Message</label><textarea id="s-msg" name="message"></textarea></div>
<button class="btn dark" type="submit">Send inquiry</button><div class="form-msg"></div></form>
<p class="small muted" style="margin-top:14px">Interested in acquiring this website or the Be.Solar domain? <a href="https://web.works/contact" rel="noopener">Contact the owner</a>.</p>
</div></div>
<p class="small muted" style="margin-top:28px">Be.Solar is not a registered charity; contributions are not tax-deductible. Funds support the operation of the website as described above.</p>
</div></section>"""
    return page(path="support.html", title="Support Be.Solar: donate, sponsor or partner",
                desc="Support independent solar guidance. Donate once or monthly, sponsor a contest prize or partner with Be.Solar.",
                body=body, active="support.html")


def contests():
    body = """<section class="page-head"><div class="wrap"><h1>Contests and prizes</h1><p class="lede">Share your solar story, your best photo or your clearest explainer. We run three contests every month and a student challenge each term.</p></div></section>
<section style="padding-top:0"><div class="wrap grid g3">
<div class="panel sun"><span class="tag">Monthly</span><h3>Solar photo of the month</h3><p>Your array at sunrise, a clever mounting, a balcony kit in a city window. Original photos only.</p><p><strong>Prize:</strong> $100 gift card or equivalent, featured on our homepage.</p></div>
<div class="panel leaf"><span class="tag">Monthly</span><h3>Real savings story</h3><p>Share a year of production and bill data and what you learned. Most useful story wins.</p><p><strong>Prize:</strong> $150 and a feature article.</p></div>
<div class="panel cell"><span class="tag">Monthly</span><h3>Best explainer video</h3><p>A short video that explains one solar idea clearly: net metering, batteries, sizing.</p><p><strong>Prize:</strong> $200 plus channel promotion in our newsletter.</p></div>
</div>
<div class="wrap" style="margin-top:28px"><div class="panel"><h3>Student solar challenge</h3><p>For secondary and university students: design a solar project for your school, home or community. Judged on clarity, numbers and impact. Prize pool funded by sponsors and supporters. <a href="support.html">Sponsor a prize</a>.</p></div></div>
</section>
<section class="band"><div class="wrap grid g2" style="align-items:start">
<div><h2>Enter a contest</h2><p class="muted">Send a link to your photo, video or story (Google Drive, Dropbox, YouTube or similar). One entry per contest per month.</p>
<form class="form js-form" data-subject="Contest entry" data-ok="Entry received. Good luck. Winners are announced in the first week of next month.">
<label class="hp">Leave empty<input name="_honey" tabindex="-1" autocomplete="off"></label>
<div class="field"><label for="c-contest">Contest</label><select id="c-contest" name="contest" required><option>Solar photo of the month</option><option>Real savings story</option><option>Best explainer video</option><option>Student solar challenge</option></select></div>
<div class="two"><div class="field"><label for="c-name">Name</label><input id="c-name" name="name" required></div><div class="field"><label for="c-email">Email</label><input id="c-email" name="email" type="email" required></div></div>
<div class="two"><div class="field"><label for="c-country">Country</label><input id="c-country" name="country" required></div><div class="field"><label for="c-link">Link to your entry</label><input id="c-link" name="entry_link" type="url" required placeholder="https://"></div></div>
<div class="field"><label for="c-desc">Tell us about it (2–3 sentences)</label><textarea id="c-desc" name="description" required></textarea></div>
<label class="check"><input type="checkbox" name="rights" value="Yes" required><span>I created this entry, own the rights to it, and allow Be.Solar to publish it with credit. I accept the official rules below.</span></label>
<button class="btn" type="submit">Submit my entry</button><div class="form-msg"></div>
</form></div>
<div><h2>Official rules (summary)</h2>
<ul class="muted"><li>No purchase or payment necessary to enter or win.</li><li>Open to individuals aged 18 or over, or 13–17 with written parental consent for the student challenge, where permitted by law. Void where prohibited.</li><li>Entries must be original, lawful and free of third-party trademarks as the main subject.</li><li>Judged by the Be.Solar editorial team on originality, usefulness and quality. Judges' decisions are final.</li><li>Winners are notified by email and must respond within 14 days, or an alternate winner is chosen.</li><li>Prizes are non-transferable; cash equivalents may be substituted. Winners are responsible for any taxes.</li><li>Personal data is used only to administer the contest; see our <a href="privacy.html">privacy policy</a>.</li></ul>
</div></div></section>"""
    return page(path="contests.html", title="Solar contests and prizes: photo, story and video | Be.Solar",
                desc="Enter monthly solar contests for photos, savings stories and explainer videos, plus a student solar challenge with prizes.",
                body=body, active="contests.html")


def careers():
    roles = [("Solar content writer (freelance)", "Write and update guides on costs, incentives and equipment. Experience in energy or personal finance writing preferred.", "Remote"),
             ("Solar engineer / technical reviewer", "Review calculator assumptions and guides for accuracy. NABCEP, MCS or equivalent experience valued.", "Remote, part-time"),
             ("Regional editor: India", "Cover PM Surya Ghar, state subsidies and DISCOM rules. Hindi a plus.", "Remote, India"),
             ("Partnerships manager", "Recruit and support installer partners across the US, UK and Australia.", "Remote, commission-based"),
             ("Video creator", "Produce short explainers and installation stories for YouTube and social.", "Remote, per project"),
             ("Front-end developer", "Build new calculators and data visualisations in plain HTML, CSS and JavaScript.", "Remote, contract")]
    rows = "".join(f'<div class="row" style="grid-template-columns:minmax(180px,1fr) 2fr auto"><h3>{t}</h3><p>{d}</p><span class="tag">{w}</span></div>' for t, d, w in roles)
    opts = "".join(f"<option>{t}</option>" for t, _, _ in roles)
    body = f"""<section class="page-head"><div class="wrap"><h1>Work with Be.Solar</h1><p class="lede">We're a small, remote team building the most trusted independent solar resource. If you know solar, write clearly or build well, we'd like to hear from you.</p></div></section>
<section style="padding-top:0"><div class="wrap"><div class="rows">{rows}</div></div></section>
<section class="band"><div class="wrap" style="max-width:760px"><h2>Apply or introduce yourself</h2>
<form class="form js-form" data-subject="Job application" data-ok="Application received. We read every one and reply within two weeks.">
<label class="hp">Leave empty<input name="_honey" tabindex="-1" autocomplete="off"></label>
<div class="field"><label for="j-role">Role</label><select id="j-role" name="role">{opts}<option>Something else</option></select></div>
<div class="two"><div class="field"><label for="j-name">Name</label><input id="j-name" name="name" required></div><div class="field"><label for="j-email">Email</label><input id="j-email" name="email" type="email" required></div></div>
<div class="two"><div class="field"><label for="j-loc">Location and time zone</label><input id="j-loc" name="location" required></div><div class="field"><label for="j-link">Portfolio, LinkedIn or CV link</label><input id="j-link" name="portfolio" type="url" required placeholder="https://"></div></div>
<div class="field"><label for="j-why">Why you, in a few sentences</label><textarea id="j-why" name="message" required></textarea></div>
<button class="btn" type="submit">Send application</button><div class="form-msg"></div></form></div></section>"""
    return page(path="careers.html", title="Careers at Be.Solar: writers, engineers, partnerships",
                desc="Remote roles at Be.Solar for solar writers, engineers, regional editors, partnership managers, video creators and developers.",
                body=body)


def partners():
    body = """<section class="page-head"><div class="wrap"><h1>For installers and advertisers</h1><p class="lede">Reach homeowners who have already run the numbers. Be.Solar sends partner installers qualified requests from people actively planning solar.</p></div></section>
<section style="padding-top:0"><div class="wrap grid g3">
<div class="panel"><h3>Qualified requests</h3><p>Every request includes location, ownership, bill, roof shade and age, interests, financing preference and timeline, plus an instant system estimate and a lead score.</p></div>
<div class="panel"><h3>Limited sharing</h3><p>A request goes to no more than three installers. You choose your service areas, monthly cap and system types.</p></div>
<div class="panel"><h3>Clear standards</h3><p>Partners must hold required licences and insurance and keep complaint rates low. Homeowners can rate their experience.</p></div>
</div></section>
<section class="band"><div class="wrap grid g2" style="align-items:start">
<div><h2>Become a partner installer</h2><p class="muted">Tell us where you install and what you offer. We'll send pricing and the partner agreement.</p>
<form class="form js-form" data-subject="Installer partner application" data-ok="Thanks. Our partnerships team will contact you within two business days.">
<label class="hp">Leave empty<input name="_honey" tabindex="-1" autocomplete="off"></label>
<div class="two"><div class="field"><label for="i-co">Company name</label><input id="i-co" name="company" required></div><div class="field"><label for="i-web">Website</label><input id="i-web" name="website" type="url" placeholder="https://"></div></div>
<div class="two"><div class="field"><label for="i-name">Contact name</label><input id="i-name" name="name" required></div><div class="field"><label for="i-email">Work email</label><input id="i-email" name="email" type="email" required></div></div>
<div class="two"><div class="field"><label for="i-phone">Phone</label><input id="i-phone" name="phone" type="tel" required></div><div class="field"><label for="i-country">Country</label><select id="i-country" name="country"><option>United States</option><option>Canada</option><option>United Kingdom</option><option>Australia</option><option>India</option><option>Other</option></select></div></div>
<div class="field"><label for="i-areas">Service areas (states, counties, ZIP/postcodes)</label><input id="i-areas" name="service_areas" required></div>
<div class="two"><div class="field"><label for="i-vol">Requests wanted per month</label><select id="i-vol" name="monthly_volume"><option>1–10</option><option>11–30</option><option>31–100</option><option>100+</option></select></div>
<div class="field"><label for="i-cert">Certifications</label><input id="i-cert" name="certifications" placeholder="NABCEP, MCS, SAA, MNRE…"></div></div>
<label class="check"><input type="checkbox" name="licensed" value="Yes" required><span>We hold the licences and insurance required to install solar in our service areas.</span></label>
<button class="btn" type="submit">Apply to partner</button><div class="form-msg"></div></form></div>
<div><h2>Advertising</h2><p class="muted">Display, newsletter and sponsored-tool placements are available to solar manufacturers, financiers, utilities and clean-energy brands. All sponsored content is labelled. We don't sell rankings.</p>
<ul class="muted"><li>Calculator sponsorship</li><li>Newsletter placements</li><li>Guide series sponsorship</li><li>Contest prize sponsorship</li></ul>
<p><a class="btn ghost" href="contact.html?topic=Advertising">Ask about advertising</a></p>
<p class="small muted" style="margin-top:20px">To discuss acquiring this website or domain, or a strategic partnership, <a href="https://web.works/contact" rel="noopener">contact the owner</a>.</p></div>
</div></section>"""
    return page(path="partners.html", title="Solar installer leads and advertising | Be.Solar partners",
                desc="Partner with Be.Solar to receive qualified homeowner solar requests or advertise to people planning solar.",
                body=body)


def about():
    body = """<section class="page-head"><div class="wrap" style="max-width:820px"><h1>About Be.Solar</h1><p class="lede">An independent solar desk for homeowners who want clear numbers before they talk to a salesperson.</p></div></section>
<section style="padding-top:0"><div class="wrap prose" style="max-width:820px">
<h2>What we do</h2>
<p>Be.Solar publishes free calculators, guides and incentive trackers for home solar in the United States, Canada, the United Kingdom, Australia and India. When readers want quotes, we connect them with up to three local installers.</p>
<h2>How we make money</h2>
<p>We're funded by three sources: advertising served by Google, referral fees from partner installers when a reader requests quotes, and reader support. Installer fees never change the price a homeowner is quoted, and no company can pay to change our calculators, guides or recommendations. Sponsored content, if any, is always labelled.</p>
<h2>Editorial standards</h2>
<ul><li>We cite official sources for incentives and rules, and review them regularly.</li><li>Calculators publish their formulas and let readers change every assumption.</li><li>We correct errors promptly and note significant updates.</li><li>We write for homeowners, not for installers or manufacturers.</li></ul>
<h2>Ownership</h2>
<p>Be.Solar is part of the Webworks Media Network, an independent group of websites. It is not affiliated with any solar manufacturer, installer, utility or government body, or with any business using a similar name.</p>
<p><a href="contact.html">Contact us</a> with questions, corrections or ideas.</p>
</div></section>"""
    return page(path="about.html", title="About Be.Solar: independent solar guidance",
                desc="Who runs Be.Solar, how it makes money and the editorial standards behind its solar calculators and guides.", body=body)


def contact():
    body = """<section class="page-head"><div class="wrap"><h1>Contact Be.Solar</h1><p class="lede">Questions, corrections, partnership ideas or press inquiries. We reply within two business days.</p></div></section>
<section style="padding-top:0"><div class="wrap grid g2" style="align-items:start">
<form class="form js-form panel" data-subject="Contact form" data-ok="Message received. We'll reply within two business days.">
<label class="hp">Leave empty<input name="_honey" tabindex="-1" autocomplete="off"></label>
<div class="two"><div class="field"><label for="k-name">Name</label><input id="k-name" name="name" required autocomplete="name"></div><div class="field"><label for="k-email">Email</label><input id="k-email" name="email" type="email" required autocomplete="email"></div></div>
<div class="field"><label for="k-topic">Topic</label><select id="k-topic" name="topic"><option>General question</option><option>Correction or update</option><option>Advertising</option><option>Sponsorship</option><option>Partnership</option><option>Press</option><option>Website or domain acquisition</option><option>Privacy request</option></select></div>
<div class="field"><label for="k-msg">Message</label><textarea id="k-msg" name="message" required></textarea></div>
<button class="btn" type="submit">Send message</button><div class="form-msg"></div></form>
<div><h2 style="font-size:1.4rem">Other ways to reach us</h2>
<p><a href="#contact" data-mail="Be.Solar inquiry">Email the Be.Solar team</a></p>
<p class="muted">Looking for solar quotes? Use the <a href="get-quotes.html">quote request form</a>, which reaches matched installers directly.</p>
<p class="muted">Interested in this website, the domain name, sponsorship, advertising or partnership? <a href="https://web.works/contact" rel="noopener">Contact the owner at Web.Works</a>.</p></div>
</div></section>
<script>(function(){var t=new URLSearchParams(location.search).get("topic");if(t){var s=document.getElementById("k-topic");[].forEach.call(s.options,function(o){if(o.text===t)s.value=t;});}})();</script>"""
    return page(path="contact.html", title="Contact Be.Solar", desc="Contact the Be.Solar team with questions, corrections, partnership or advertising inquiries.", body=body)


def legal(path, title, desc, html):
    body = f'<section class="page-head"><div class="wrap" style="max-width:820px"><h1>{title}</h1><p class="meta">Last updated {UPDATED}</p></div></section><section style="padding-top:0"><div class="wrap prose" style="max-width:820px">{html}</div></section>'
    return page(path=path, title=f"{title} | Be.Solar", desc=desc, body=body, mobile_cta=False)


PRIVACY = """
<p>This policy explains what information Be.Solar ("we", "us") collects, how we use it and your choices. It applies to be.solar and its pages.</p>
<h2>Information we collect</h2>
<ul><li><strong>Information you give us</strong> through forms: quote requests (name, email, phone, address, property and energy details), contact messages, newsletter signups, contest entries, job applications, pledges and sponsorship inquiries.</li><li><strong>Information collected automatically</strong> by our hosting provider and by third-party services such as Google: IP address, browser type, pages viewed, referring site and cookie identifiers.</li><li><strong>Calculator inputs</strong> stay in your browser and are not sent to us unless you submit a form.</li></ul>
<h2>How we use it</h2>
<ul><li>To respond to you and provide what you asked for.</li><li>For quote requests: to share your request with up to three solar installers serving your area, who may contact you about your project, as you consented on the form.</li><li>To send the newsletter if you subscribed (unsubscribe at any time).</li><li>To run contests, consider applications, and process pledges.</li><li>To operate, secure and improve the site.</li></ul>
<p>We do not sell your personal information to data brokers or unrelated marketers.</p>
<h2>Form processing</h2>
<p>Form submissions are delivered to our team through FormSubmit (formsubmit.co), a form-forwarding service, which processes the data on our behalf to deliver it by email.</p>
<h2 id="cookies">Cookies and advertising</h2>
<p>We use Google AdSense to show ads. Third-party vendors, including Google, use cookies to serve ads based on your prior visits to this website or other websites. Google's use of advertising cookies enables it and its partners to serve ads to you based on your visits to this site and/or other sites on the internet.</p>
<p>You may opt out of personalised advertising by visiting <a href="https://www.google.com/settings/ads" rel="noopener" target="_blank">Google Ads Settings</a>, or opt out of some third-party vendors' use of cookies for personalised advertising at <a href="https://www.aboutads.info/choices/" rel="noopener" target="_blank">aboutads.info</a>. Learn how Google uses information from sites that use its services at <a href="https://policies.google.com/technologies/partner-sites" rel="noopener" target="_blank">policies.google.com/technologies/partner-sites</a>.</p>
<p>Visitors in the European Economic Area, the UK and Switzerland are shown a consent message managed by a Google-certified consent management platform before personalised ads are served. Our own banner lets you limit cookies to essential ones. We also store small preferences (theme, consent choice) in your browser's local storage.</p>
<p>YouTube videos load only when you press play and use YouTube's privacy-enhanced mode.</p>
<h2>Sharing</h2>
<p>We share information with partner installers (quote requests only), service providers that help us run the site (hosting, form delivery, email), Google for advertising, and authorities when the law requires it.</p>
<h2>Retention</h2>
<p>We keep form submissions only as long as needed for the purpose, generally up to 24 months, unless the law requires longer.</p>
<h2>Your rights</h2>
<p>Depending on where you live (for example under the GDPR, UK GDPR, California law, Canada's PIPEDA, Australia's Privacy Act or India's Digital Personal Data Protection Act), you may have rights to access, correct, delete or restrict use of your information, and to withdraw consent. Use our <a href="contact.html?topic=Privacy%20request">contact form</a> and choose "Privacy request". To stop installer contact, tell the installer and us.</p>
<h2>Children</h2>
<p>The site is intended for adults. We do not knowingly collect personal information from children under 13; student contest entries from minors require parental consent.</p>
<h2>Changes</h2>
<p>We'll post updates here and change the date above.</p>"""

TERMS = """
<p>By using be.solar you agree to these terms. If you don't agree, please don't use the site.</p>
<h2>Information only</h2>
<p>Content, calculators and estimates are general information. They are not financial, tax, legal, engineering or electrical advice and may not reflect your circumstances or the latest rules. Always confirm with qualified professionals and official sources before making decisions.</p>
<h2>Quotes and installers</h2>
<p>Be.Solar is not an installer or contractor. Installers we refer you to are independent businesses responsible for their own quotes, work, licences and warranties. Any agreement you make is between you and the installer. We don't guarantee their performance, though we act on complaints about partners.</p>
<h2>Acceptable use</h2>
<p>Don't misuse the site: no unlawful activity, spam, scraping at volume, interfering with security, or submitting false information about others.</p>
<h2>Submissions</h2>
<p>When you submit contest entries, stories or comments, you confirm you have the rights to them and grant us a non-exclusive, worldwide, royalty-free licence to publish them with credit.</p>
<h2>Intellectual property</h2>
<p>Site content, design and code are owned by Be.Solar / Webworks Media Network or used with permission. You may share links and quote short passages with attribution. Third-party names and marks belong to their owners.</p>
<h2>Third-party links and services</h2>
<p>We link to external sites and embed third-party content. We're not responsible for their content or practices.</p>
<h2>Donations and pledges</h2>
<p>Contributions support the website's operation and are not tax-deductible. Pledges are voluntary and non-refundable once paid, except where the law requires.</p>
<h2>Liability</h2>
<p>To the extent permitted by law, the site is provided "as is" and we are not liable for losses arising from its use or from reliance on estimates.</p>
<h2>Changes and contact</h2>
<p>We may update these terms; continued use means you accept them. Questions: <a href="contact.html">contact us</a>.</p>"""

DISCLAIMER = """
<h2>Trademark and name disclosure</h2>
<p>"Be.Solar" is the name of this independent website and refers to its domain, be.solar. Be.Solar is <strong>not affiliated with, sponsored by, endorsed by or connected to</strong> any company, product, brand, trademark or registered mark named "BeSolar", "Be Solar", "Bee Solar" or any similar name, in any country. We do not use, and do not claim rights in, any such third-party mark, logo or trade dress. If you represent a rights holder and have a concern, please <a href="contact.html">contact us</a> and we will respond promptly.</p>
<p>Names of manufacturers, installers, products, utilities, government programs and agencies (for example TED-Ed, Google, YouTube, NREL, MCS, the Clean Energy Council and PM Surya Ghar) appear only to identify them and to inform readers. Their use does not imply endorsement or affiliation. All trademarks are the property of their respective owners.</p>
<h2>Copyright</h2>
<p>© 2026 Be.Solar / Webworks Media Network. Original text, calculators, illustrations and code on this site are protected by copyright. Embedded videos and linked content remain the property of their creators and are shown via the platforms' official embed or link features. Figures and facts from public sources are summarised in our own words and attributed.</p>
<p>If you believe content on this site infringes your copyright, send a notice through our <a href="contact.html">contact form</a> identifying the work, the page, and your contact details; we will review and remove infringing material promptly.</p>
<h2>Financial and advice disclaimer</h2>
<p>Savings, payback, sizing and cost figures are estimates based on averages and the assumptions shown. Actual results depend on your roof, location, equipment, tariff, weather, installer and future policy changes. Nothing on this site is financial, tax, legal or engineering advice.</p>
<h2>Advertising and referral disclosure</h2>
<p>Be.Solar displays ads served by Google AdSense and may receive referral fees from partner installers when you request quotes. These relationships don't influence our editorial content. Sponsored material is labelled.</p>"""

GLOSSARY = [("AC / DC", "Panels produce direct current (DC); homes and the grid use alternating current (AC). The inverter converts between them."),
            ("Azimuth", "The compass direction a roof or panel faces. South (in the northern hemisphere) collects the most energy."),
            ("Battery depth of discharge (DoD)", "The share of a battery's capacity that can be used. Most lithium iron phosphate batteries allow 90–100%."),
            ("Cost per watt", "Installed price divided by system size in watts; the standard way to compare quotes."),
            ("DISCOM", "An electricity distribution company in India. It approves rooftop solar connections and net meters."),
            ("Feed-in tariff", "Payment per kWh for power exported to the grid, common in Australia."),
            ("Inverter", "Equipment that converts DC from panels to AC for the home. Types include string, optimiser-based, micro and hybrid."),
            ("kW / kWp", "Kilowatt: power. kWp (kilowatt-peak) is a system's rated output under standard test conditions."),
            ("kWh", "Kilowatt-hour: energy. What your bill measures."),
            ("MCS", "UK certification scheme for installers and products; usually needed for export payments."),
            ("Microinverter", "A small inverter mounted on each panel, letting each work independently."),
            ("Net metering", "Billing that credits exported power, often at the retail rate."),
            ("Net billing", "Billing that credits exported power at a lower rate than retail."),
            ("Peak sun hours", "Daily solar energy at a location expressed as hours of 1,000 W/m² sunshine."),
            ("Performance ratio", "Real-world output as a share of theoretical output after losses, typically 75–85%."),
            ("Permission to operate (PTO)", "Utility approval to switch on a grid-connected system."),
            ("PPA", "Power purchase agreement: a company owns the panels on your roof and sells you the power."),
            ("SEG", "Smart Export Guarantee: UK requirement for larger suppliers to pay for exported solar power."),
            ("Self-consumption", "The share of solar output used on site rather than exported."),
            ("SREC", "Solar renewable energy certificate, tradable in some US state markets."),
            ("STC", "Small-scale technology certificate: Australia's upfront discount mechanism for solar and batteries."),
            ("Temperature coefficient", "How much panel output drops for each degree Celsius above 25 °C."),
            ("Time-of-use (TOU) rate", "A tariff where price per kWh varies by time of day."),
            ("Virtual power plant (VPP)", "A network of home batteries coordinated to support the grid, often paying participants.")]


def glossary():
    items = "".join(f'<div style="padding:14px 0;border-bottom:1px solid var(--line)"><dt style="font-family:var(--f-display);font-weight:700">{t}</dt><dd style="margin:4px 0 0;color:var(--muted)">{d}</dd></div>' for t, d in GLOSSARY)
    body = f'<section class="page-head"><div class="wrap" style="max-width:820px"><h1>Solar glossary</h1><p class="lede">The terms you\'ll meet in quotes and contracts, in one line each.</p></div></section><section style="padding-top:0"><div class="wrap" style="max-width:820px"><dl>{items}</dl></div></section>{quote_band("")}'
    schema = {"@context": "https://schema.org", "@type": "DefinedTermSet", "name": "Solar glossary",
              "hasDefinedTerm": [{"@type": "DefinedTerm", "name": t, "description": d} for t, d in GLOSSARY]}
    return page(path="glossary.html", title="Solar glossary: kW, kWh, PPA, STC, SEG and more | Be.Solar",
                desc="Plain-language definitions of solar terms used in quotes, contracts and incentive programs.", body=body, schema=schema)


def not_found():
    body = """<section class="page-head"><div class="wrap" style="max-width:720px"><h1>That page isn't here</h1><p class="lede">The link may be old or mistyped. These are the most useful places to go next.</p>
<div class="rows" style="margin-top:20px"><a class="row" href="index.html"><h3>Home</h3><p>Start with the instant estimate.</p><span class="go">Go</span></a>
<a class="row" href="tools.html"><h3>Calculators</h3><p>Savings, size, battery and payback.</p><span class="go">Go</span></a>
<a class="row" href="guides.html"><h3>Guides</h3><p>Costs, incentives and buying safely.</p><span class="go">Go</span></a></div></div></section>"""
    return page(path="404.html", title="Page not found | Be.Solar", desc="Page not found.", body=body, noindex=True, mobile_cta=False)
