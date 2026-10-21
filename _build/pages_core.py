"""Home, quote wizard, calculators."""
from layout import page, quote_band

COUNTRY_OPTS = ('<option value="US">United States</option><option value="CA">Canada</option>'
                '<option value="UK">United Kingdom</option><option value="AU">Australia</option>'
                '<option value="IN">India</option><option value="XX">Other country</option>')


def home(guides):
    r = ""
    guide_rows = "".join(
        f'<a class="row" href="guides/{g["slug"]}.html"><h3>{g["title"]}</h3><p>{g["desc"]}</p><span class="go">Read guide</span></a>'
        for g in guides[:6])
    body = f"""
<section class="hero"><div class="wrap hero-grid">
  <div>
    <h1>Know your solar numbers before anyone tries to sell you panels.</h1>
    <p class="lede">Be.Solar is an independent solar desk for homeowners. Run the math in seconds, read guides written without a sales script, and get quotes from vetted local installers only when you're ready.</p>
    <div class="hero-ctas"><a class="btn" id="dial-quote" data-base="get-quotes.html" href="get-quotes.html">Get free installer quotes</a><a class="btn ghost" href="tools/solar-savings-calculator.html">Open the full calculator</a></div>
    <ul class="trust"><li>No cost, no obligation</li><li>Your details go to at most three installers</li><li>Five countries covered</li></ul>
  </div>
  <div class="dial" id="dial" aria-live="polite">
    <svg class="arc" viewBox="0 0 400 210" role="img" aria-label="The sun rises along the arc as your monthly bill grows">
      <path d="M40 190 A160 160 0 0 1 360 190" fill="none" stroke="var(--line)" stroke-width="3" stroke-dasharray="2 8" stroke-linecap="round"/>
      <line x1="20" y1="190" x2="380" y2="190" stroke="var(--ink)" stroke-width="2"/>
      <g fill="var(--cell)"><rect x="128" y="176" width="40" height="12" rx="2"/><rect x="180" y="176" width="40" height="12" rx="2"/><rect x="232" y="176" width="40" height="12" rx="2"/></g>
      <g class="sun-dot" transform="translate(40 190)"><circle r="22" fill="var(--sun)" opacity=".25"/><circle r="14" fill="var(--sun)"/></g>
    </svg>
    <div class="two" style="margin-top:10px">
      <div class="field"><label for="dial-country">Where is your home?</label><select id="dial-country">{COUNTRY_OPTS}</select></div>
      <div><div class="bill-label"><span>Monthly power bill</span><span class="bill-value" id="dial-bill-out">$160</span></div>
      <input id="dial-bill" type="range" min="20" max="600" value="160" aria-label="Monthly electricity bill"></div>
    </div>
    <div class="dial-out">
      <div><strong id="dial-save">–</strong><span>25-year net savings</span></div>
      <div><strong id="dial-kw">–</strong><span>suggested system</span></div>
      <div><strong id="dial-panels">–</strong><span>panels at 430 W</span></div>
    </div>
    <p class="small muted" style="margin:12px 0 0">Estimate uses national averages for price, sunshine and installed cost. Refine every input in the <a href="tools/solar-savings-calculator.html">savings calculator</a>.</p>
  </div>
</div></section>

<section><div class="wrap">
  <div class="section-head"><h2>How going solar actually works</h2><p class="lede">Four decisions, in this order. Most regret comes from doing them backwards.</p></div>
  <ol class="steps">
    <li><h3>Check the fit</h3><p>Roof direction, shade, roof age and your local electricity price decide whether solar pays. Our calculators answer this in a minute.</p></li>
    <li><h3>Size it right</h3><p>Match the system to your real usage, not the biggest array a roof can hold. Oversizing wastes money where export rates are low.</p></li>
    <li><h3>Compare three quotes</h3><p>Prices for identical systems often differ by a third or more. Compare cost per watt, equipment and warranty, not monthly payment.</p></li>
    <li><h3>Claim every incentive</h3><p>Subsidies, export payments and tax treatment differ by country and change often. Our incentive pages track the current rules.</p></li>
  </ol>
</div></section>

<section class="band"><div class="wrap">
  <div class="section-head"><h2>Free solar calculators</h2><p class="lede">Transparent formulas, editable assumptions, no email wall.</p></div>
  <div class="rows">
    <a class="row" href="tools/solar-savings-calculator.html"><h3>Solar savings calculator</h3><p>Year-one and 25-year savings, cost after incentives, and a year-by-year cash chart.</p><span class="go">Calculate</span></a>
    <a class="row" href="tools/system-size-calculator.html"><h3>System size &amp; panel count</h3><p>How many kilowatts and panels you need, and how much roof that takes.</p><span class="go">Calculate</span></a>
    <a class="row" href="tools/battery-backup-calculator.html"><h3>Battery backup sizing</h3><p>Storage needed to ride through an outage for your essential loads.</p><span class="go">Calculate</span></a>
    <a class="row" href="tools/payback-roi-calculator.html"><h3>Payback &amp; ROI</h3><p>Break-even year and return compared with leaving the money elsewhere.</p><span class="go">Calculate</span></a>
  </div>
</div></section>

{quote_band(r)}

<section><div class="wrap">
  <div class="section-head"><h2>Start with these guides</h2></div>
  <div class="rows">{guide_rows}</div>
  <p style="margin-top:22px"><a href="guides.html">Browse all guides</a></p>
</div></section>

<section class="band"><div class="wrap grid g2" style="align-items:center">
  <div class="video"><button class="yt-facade" data-yt="xKxrkht7CpY" aria-label="Play: How do solar panels work? (TED-Ed)"></button></div>
  <div><h2>Two minutes on how a panel turns light into power</h2><p class="lede">A clear primer from TED-Ed. Our video library collects the best explainers on batteries, net metering, installation and maintenance.</p><a class="btn ghost" href="videos.html">Open the video library</a></div>
</div></section>

<section><div class="wrap grid g3">
  <div class="panel sun"><h3>Keep Be.Solar independent</h3><p>Reader support funds new calculators, data updates and guides with no installer paying for placement.</p><a href="support.html">Support the project</a></div>
  <div class="panel leaf"><h3>Win a solar prize</h3><p>Monthly contests for best solar photo, best savings story and student projects, with gear and cash prizes.</p><a href="contests.html">See current contests</a></div>
  <div class="panel cell"><h3>Install solar for a living?</h3><p>Receive homeowner requests in your service area and list your company in our directory.</p><a href="partners.html">Become a partner installer</a></div>
</div></section>
"""
    faq = [
        ("Is solar still worth it in 2026?", "In most places with average or higher electricity prices and a sunny, unshaded roof, a fairly priced system still pays back well within its 25-year warranty. Run the savings calculator with your own bill to see your break-even year."),
        ("How much does a home solar system cost?", "Installed prices vary by country. In the US most quotes land between about $2.50 and $3.50 per watt before incentives, so a 7 kW system is roughly $18,000 to $25,000. The calculators let you change the cost per watt to match quotes you receive."),
        ("Do I need a battery?", "Not to save money in most grid-connected homes. A battery is worth it when your utility pays little for exported power, charges peak-time rates, or when outages are frequent. Use the battery calculator to size one."),
    ]
    schema = [{"@context": "https://schema.org", "@type": "WebSite", "name": "Be.Solar", "url": "https://be.solar/"},
              {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
                  {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}]
    body += '<section class="band"><div class="wrap" style="max-width:820px"><h2>Quick answers</h2><div class="faq">' + "".join(
        f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq) + "</div></div></section>"
    return page(path="index.html", title="Be.Solar — Solar calculators, guides and free installer quotes",
                desc="Independent solar savings calculators, plain-language guides, incentives by country and free quotes from vetted local installers.",
                body=body, active="index.html", schema=schema)


def quotes():
    body = f"""
<section class="page-head"><div class="wrap">
  <h1>Get up to three free solar quotes</h1>
  <p class="lede">Tell us about your home and power use. We pass your request to vetted installers serving your area. You decide whether to go ahead with any of them.</p>
</div></section>
<section style="padding-top:12px"><div class="wrap wizard">
  <div class="panel">
    <div class="wiz-meta"><div class="progress"><i></i></div><p class="small muted" id="wiz-count" aria-live="polite">Step 1 of 5</p></div>
    <form id="quote-wizard" class="js-wizard" data-subject="Solar quote request (lead)" novalidate>
      <label class="hp">Leave empty<input name="_honey" tabindex="-1" autocomplete="off"></label>
      <div class="step on">
        <h2>Where is the property?</h2>
        <div class="two">
          <div class="field"><label for="w-country">Country</label><select id="w-country" name="country" required>{COUNTRY_OPTS}</select></div>
          <div class="field"><label for="w-zip">ZIP / postal code / PIN</label><input id="w-zip" name="postal_code" type="text" required autocomplete="postal-code" placeholder="e.g. 94110"></div>
        </div>
        <div class="field" style="margin-top:14px"><span class="legend">Do you own the home?</span>
          <div class="choices">
            <label class="choice"><input type="radio" name="ownership" value="Own" required><span>I own it</span></label>
            <label class="choice"><input type="radio" name="ownership" value="Rent"><span>I rent<small>We'll show community-solar options</small></span></label>
            <label class="choice"><input type="radio" name="ownership" value="Buying"><span>Buying soon</span></label>
          </div></div>
        <div class="field" style="margin-top:14px"><span class="legend">Property type</span>
          <div class="choices">
            <label class="choice"><input type="radio" name="property" value="Detached house" required><span>Detached house</span></label>
            <label class="choice"><input type="radio" name="property" value="Townhouse / semi"><span>Townhouse or semi</span></label>
            <label class="choice"><input type="radio" name="property" value="Business"><span>Business or farm</span></label>
            <label class="choice"><input type="radio" name="property" value="Other"><span>Other</span></label>
          </div></div>
      </div>

      <div class="step">
        <h2>How much do you spend on electricity?</h2>
        <div class="bill-label"><span>Average monthly bill</span><span class="bill-value" id="wiz-bill-out">$160</span></div>
        <input type="range" name="bill" id="w-bill" min="20" max="600" value="160" aria-label="Average monthly electricity bill">
        <div class="field" style="margin-top:16px"><label for="w-util">Electricity provider (optional)</label><input id="w-util" name="utility" type="text" placeholder="e.g. PG&amp;E, Hydro-Québec, Octopus, BSES"></div>
      </div>

      <div class="step">
        <h2>Tell us about the roof</h2>
        <div class="field"><span class="legend">How much shade does it get?</span>
          <div class="choices">
            <label class="choice"><input type="radio" name="shade" value="No shade" required><span>No shade</span></label>
            <label class="choice"><input type="radio" name="shade" value="Light shade"><span>Light shade</span></label>
            <label class="choice"><input type="radio" name="shade" value="Heavy shade"><span>Heavy shade</span></label>
            <label class="choice"><input type="radio" name="shade" value="Not sure"><span>Not sure</span></label>
          </div></div>
        <div class="two" style="margin-top:14px">
          <div class="field"><label for="w-roofage">Roof age</label><select id="w-roofage" name="roof_age" required><option value="">Choose</option><option>Under 10 years</option><option>10–20 years</option><option>Over 20 years</option><option>Not sure</option></select></div>
          <div class="field"><label for="w-roof">Roof material</label><select id="w-roof" name="roof_material"><option>Asphalt shingle</option><option>Metal</option><option>Tile</option><option>Flat / concrete</option><option>Other / not sure</option></select></div>
        </div>
      </div>

      <div class="step">
        <h2>What are you interested in?</h2>
        <div class="field"><span class="legend">Pick all that apply</span>
          <div class="choices">
            <label class="choice"><input type="checkbox" name="interest" value="Solar panels" checked><span>Solar panels</span></label>
            <label class="choice"><input type="checkbox" name="interest" value="Battery storage"><span>Battery storage</span></label>
            <label class="choice"><input type="checkbox" name="interest" value="EV charger"><span>EV charger</span></label>
            <label class="choice"><input type="checkbox" name="interest" value="Solar water heating"><span>Solar water heating</span></label>
          </div></div>
        <div class="two" style="margin-top:14px">
          <div class="field"><label for="w-fin">How would you pay?</label><select id="w-fin" name="financing" required><option value="">Choose</option><option>Cash</option><option>Loan</option><option>Lease or PPA</option><option>Not sure yet</option></select></div>
          <div class="field"><label for="w-time">When do you want it installed?</label><select id="w-time" name="timeline" required><option value="">Choose</option><option>Within 3 months</option><option>3–6 months</option><option>6–12 months</option><option>Just researching</option></select></div>
        </div>
        <div class="field" style="margin-top:14px"><label for="w-credit">Credit range (optional, helps installers suggest financing)</label><select id="w-credit" name="credit_band"><option value="">Prefer not to say</option><option>Excellent (720+)</option><option>Good (660–719)</option><option>Fair (600–659)</option><option>Below 600</option></select></div>
      </div>

      <div class="step">
        <h2>Where should installers send your quotes?</h2>
        <div class="two">
          <div class="field"><label for="w-first">First name</label><input id="w-first" name="first_name" required autocomplete="given-name"></div>
          <div class="field"><label for="w-last">Last name</label><input id="w-last" name="last_name" required autocomplete="family-name"></div>
        </div>
        <div class="two" style="margin-top:14px">
          <div class="field"><label for="w-email">Email</label><input id="w-email" name="email" type="email" required autocomplete="email"></div>
          <div class="field"><label for="w-phone">Phone</label><input id="w-phone" name="phone" type="tel" required autocomplete="tel" pattern="[0-9+()\\-\\s]{{7,}}"></div>
        </div>
        <div class="field" style="margin-top:14px"><label for="w-addr">Street address (optional, for a satellite roof check)</label><input id="w-addr" name="address" autocomplete="street-address"></div>
        <div class="field" style="margin-top:14px"><label for="w-best">Best time to reach you</label><select id="w-best" name="best_time"><option>Any time</option><option>Morning</option><option>Afternoon</option><option>Evening</option><option>Email only, please</option></select></div>
        <label class="check" style="margin-top:16px"><input type="checkbox" name="consent" value="Yes" required><span>I agree that Be.Solar may share my request with up to three solar installers serving my area, and that they may contact me by phone, text or email about my quote, including with automated technology. Consent is not a condition of purchase. I can opt out at any time. See the <a href="privacy.html">privacy policy</a>.</span></label>
      </div>

      <div class="form-msg"></div>
      <div class="wiz-nav"><button type="button" class="btn ghost" id="wiz-back">Back</button><button type="button" class="btn" id="wiz-next">Continue</button><button type="submit" class="btn" id="wiz-submit" hidden>Get my free quotes</button></div>
    </form>
    <div id="wiz-done" hidden tabindex="-1">
      <h2>Request received</h2>
      <p>Matched installers usually reach out within one business day. While you wait, these three checks make every quote easier to compare:</p>
      <ol><li>Ask each installer for the price per watt before incentives.</li><li>Ask for the panel, inverter and battery model numbers and their warranty terms.</li><li>Ask for a production estimate in kWh per year, and how it was calculated.</li></ol>
      <p><a href="guides/how-to-compare-solar-quotes.html">Read our full quote comparison checklist</a></p>
    </div>
  </div>

  <aside class="live panel cell" aria-live="polite">
    <h3>Your instant estimate</h3>
    <dl>
      <dt>System size</dt><dd id="live-kw">–</dd>
      <dt>Panels (430 W)</dt><dd id="live-panels">–</dd>
      <dt>First-year savings</dt><dd id="live-save1">–</dd>
      <dt>25-year net savings</dt><dd id="live-save25">–</dd>
      <dt>CO₂ avoided over 25 years</dt><dd id="live-co2">–</dd>
    </dl>
    <p class="small muted" style="margin-top:14px">Based on national averages. Installers refine this with your roof, usage and local rates.</p>
    <hr style="border:0;border-top:1px solid var(--line);margin:16px 0">
    <ul class="small" style="padding-left:1.1em;margin:0">
      <li>Free and no obligation</li>
      <li>Shared with no more than three installers</li>
      <li>Never sold to unrelated marketers</li>
      <li>Opt out at any time</li>
    </ul>
  </aside>
</div></section>
<section class="band"><div class="wrap" style="max-width:820px">
  <h2>Questions about getting quotes</h2>
  <div class="faq">
    <details><summary>Why three quotes?</summary><p>Three quotes give you a reliable sense of the local price per watt without drowning you in calls. Price spreads between installers for the same system are common, so comparing pays.</p></details>
    <details><summary>Does Be.Solar install systems?</summary><p>No. We are an independent publisher. Partner installers may pay a referral fee when we send them a request. That fee never changes the price you're quoted and never affects our calculators or guides.</p></details>
    <details><summary>I rent. Can I still use solar?</summary><p>Often yes, through community solar subscriptions, balcony or plug-in kits where allowed, or by sharing a proposal with your landlord. Submit the form and choose "I rent" and we'll point you to options in your area.</p></details>
  </div>
</div></section>
"""
    return page(path="get-quotes.html", title="Get free solar quotes from vetted local installers | Be.Solar",
                desc="Compare up to three free, no-obligation quotes from vetted solar installers near you. Instant savings estimate included.",
                body=body, mobile_cta=False)


def calc_shell(path, title, h1, lede, form, out, explain, faq, desc):
    r = "../"
    body = f"""
<section class="page-head"><div class="wrap"><p class="crumbs"><a href="{r}index.html">Home</a> / <a href="{r}tools.html">Calculators</a></p>
<h1>{h1}</h1><p class="lede">{lede}</p></div></section>
<section style="padding-top:8px"><div class="wrap calc">{form}{out}</div></section>
<section class="band"><div class="wrap" style="max-width:820px"><div class="prose">{explain}</div>
<h2 style="margin-top:40px">Frequently asked</h2><div class="faq">{"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in faq)}</div></div></section>
{quote_band(r)}"""
    schema = [{"@context": "https://schema.org", "@type": "WebApplication", "name": h1, "applicationCategory": "FinanceApplication",
               "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0"}},
              {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
                  {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}]
    return page(path=path, title=title, desc=desc, body=body, active="tools.html", schema=schema)


def field(name, label, val, step="any", unit="", hint="", cur=False):
    pre = '<span data-cur>$</span> ' if cur else ""
    return (f'<div class="field"><label for="f-{name}">{pre}{label}{(" ("+unit+")") if unit else ""}</label>'
            f'<input id="f-{name}" name="{name}" type="number" step="{step}" min="0" value="{val}">'
            f'{f"<div class=hint>{hint}</div>" if hint else ""}</div>')


COUNTRY_FIELD = f'<div class="field"><label for="f-country">Country</label><select id="f-country" name="country">{COUNTRY_OPTS}</select></div>'

SAVINGS_OUT = """<div class="results" id="out" aria-live="polite">
  <p class="muted" style="margin:0">Estimated 25-year net savings</p>
  <p class="big" data-o="save25">–</p>
  <p class="small muted">Lifetime bill savings minus the cost after incentives.</p>
  <div class="stat-list">
    <div><strong data-o="save1">–</strong><span>First-year savings</span></div>
    <div><strong data-o="payback">–</strong><span>Payback period</span></div>
    <div><strong data-o="kw">–</strong><span>System size</span></div>
    <div><strong data-o="panels">–</strong><span>Panels</span></div>
    <div><strong data-o="gross">–</strong><span>Price before incentives</span></div>
    <div><strong data-o="net">–</strong><span>Price after incentives</span></div>
    <div><strong data-o="prod">–</strong><span>First-year production</span></div>
    <div><strong data-o="co2">–</strong><span>CO₂ avoided, 25 years</span></div>
  </div>
  <div class="chart"></div>
  <p class="small muted">Blue bars are years still paying off the system; green bars are years in profit.</p>
  <a class="btn" data-quote-link data-base="../get-quotes.html" href="../get-quotes.html">Check this against real quotes</a>
</div>"""


def tools():
    savings_form = f"""<form class="calc-form panel form" data-calc="savings" data-out="out">
{COUNTRY_FIELD}
<div class="two">{field("bill","Monthly bill",160,cur=True)}{field("rate","Electricity price","0.18",unit="per kWh",cur=True)}</div>
<div class="two">{field("sun","Peak sun hours",4.6,unit="per day",hint="3 (cloudy north) to 6 (desert)")}{field("cpw","Installed cost","2.9",unit="per watt",cur=True)}</div>
<div class="two">{field("offset","Bill offset",100,unit="%",hint="Share of usage solar should cover")}{field("esc","Price rise",3,unit="% a year")}</div>
<div class="two">{field("credit","Tax credit",0,unit="% of cost",hint="Enter if one applies to you")}{field("rebate","Other rebates",0,cur=True)}</div>
<p class="small muted">India: the PM Surya Ghar central subsidy is applied automatically for systems up to 3 kW and above.</p>
</form>"""
    explain = """<h2>How this calculator works</h2>
<p>It converts your monthly bill into annual electricity use by dividing by your price per kWh. It then sizes a system to cover the share you choose, using your daily peak sun hours and an 80% performance ratio that accounts for inverter losses, heat, wiring and dirt.</p>
<p>Savings in each year equal the energy the system produces (capped at your own usage, so exports are not over-counted) multiplied by an electricity price that rises by the rate you set. Panel output falls by 0.5% a year, in line with typical tier-one warranties. Payback is the point where cumulative savings exceed the price after incentives.</p>
<h3>What it leaves out on purpose</h3>
<ul><li>Export payments. Many utilities now credit exported power below the retail price. If yours pays full retail net metering, your real savings will be higher.</li><li>Financing costs. Loan interest lengthens payback; use the payback and ROI calculator to compare cash with a loan.</li><li>Maintenance and inverter replacement, typically a modest cost over 25 years for string inverters.</li></ul>
<div class="callout"><strong>Make it precise:</strong> replace the default installed cost with the price per watt from a real quote, and the electricity price with the all-in rate from your bill (total charges divided by kWh used).</div>"""
    faq = [("What is a good payback period for solar?", "Under 10 years is strong in most markets; 6 to 8 years is typical where electricity is expensive. Panels usually carry 25-year performance warranties, so anything well inside that window means decades of profit."),
           ("What are peak sun hours?", "The number of hours per day the sun would need to shine at 1,000 watts per square metre to deliver your location's daily solar energy. It is not the same as daylight hours."),
           ("Why is my estimate different from an installer's?", "Installers use your exact roof pitch, direction, shading and utility tariff. Use this result as a sanity check: if a quote's production or price is far off, ask why.")]
    savings = calc_shell("tools/solar-savings-calculator.html", "Solar savings calculator: payback, 25-year savings and cost | Be.Solar",
                         "Solar savings calculator", "See what solar would save you, what it costs after incentives and when it pays for itself. Every assumption is editable.",
                         savings_form, SAVINGS_OUT, explain, faq,
                         "Free solar savings calculator for the US, Canada, UK, Australia and India. Payback period, 25-year savings, system size and CO₂ avoided.")

    size_form = f"""<form class="calc-form panel form" data-calc="size" data-out="out2">
{COUNTRY_FIELD}
<div class="two">{field("bill","Monthly bill",160,cur=True)}{field("rate","Electricity price","0.18",unit="per kWh",cur=True)}</div>
<div class="two">{field("sun","Peak sun hours",4.6,unit="per day")}{field("offset","Bill offset",100,unit="%")}</div>
<input type="hidden" name="cpw" value="2.9">
</form>"""
    size_out = """<div class="results" id="out2" aria-live="polite">
<p class="muted" style="margin:0">Recommended system size</p><p class="big" data-o="kw">–</p>
<div class="stat-list">
<div><strong data-o="panels">–</strong><span>Panels</span></div>
<div><strong data-o="roof">–</strong><span>Approximate roof area</span></div>
<div><strong data-o="prod">–</strong><span>Yearly production</span></div>
<div><strong data-o="gross">–</strong><span>Typical installed price</span></div>
</div>
<a class="btn" style="margin-top:20px" data-quote-link data-base="../get-quotes.html" href="../get-quotes.html">Get quotes for this size</a></div>"""
    size_explain = """<h2>The sizing formula</h2>
<p>System size in kW = annual kWh you want to cover ÷ (peak sun hours × 365 × 0.8). The 0.8 factor covers real-world losses. Panel count assumes 430-watt modules, the common size for residential panels today; each needs roughly 2 square metres of usable roof including spacing.</p>
<p>Fire codes in many regions require clear walkways along ridges and edges, so the roof area you need is usually 15 to 25% more than the panel footprint. South-facing roofs (north-facing in the southern hemisphere) give the most energy; east and west roofs typically produce 10 to 20% less but can suit time-of-use tariffs better.</p>
<h3>When to size below 100%</h3>
<p>If your utility credits exported energy at a low rate, size for the energy you use during daylight, often 60 to 80% of total usage, and consider a battery for the rest.</p>"""
    size_faq = [("How many solar panels does an average home need?", "A home using about 10,000 kWh a year in a location with 4.5 peak sun hours needs a 7 to 8 kW system, or about 17 to 19 panels at 430 W."),
                ("Can I add panels later?", "Yes, but adding to an existing system can mean a second inverter and a new permit. It is usually cheaper to size for planned changes, such as an EV or heat pump, up front.")]
    size = calc_shell("tools/system-size-calculator.html", "Solar system size calculator: how many panels do I need? | Be.Solar",
                      "How many solar panels do you need?", "Turn your electricity bill into a system size, panel count and roof area.",
                      size_form, size_out, size_explain, size_faq,
                      "Work out the solar system size, number of panels and roof space your home needs from your electricity bill.")

    bat_form = """<form class="calc-form panel form" data-calc="battery" data-out="out3">
<div class="field"><label for="b-country">Currency</label><select id="b-country" name="country">""" + COUNTRY_OPTS + """</select></div>
<div class="two">""" + field("daily", "Daily home usage", 30, unit="kWh", hint="Annual kWh ÷ 365") + field("critical", "Essential loads", 40, unit="% of usage", hint="Fridge, lights, Wi-Fi, pumps") + """</div>
<div class="two">""" + field("hours", "Backup time", 24, unit="hours") + field("dod", "Usable depth of discharge", 90, unit="%") + """</div>
<div class="two">""" + field("unit", "Battery module size", 13.5, unit="kWh") + field("perkwh", "Installed cost", 1000, unit="per kWh", cur=True) + """</div>
</form>"""
    bat_out = """<div class="results" id="out3" aria-live="polite">
<p class="muted" style="margin:0">Storage you need</p><p class="big" data-o="kwh">–</p>
<div class="stat-list"><div><strong data-o="units">–</strong><span>Battery modules</span></div>
<div><strong data-o="cost">–</strong><span>Approximate installed cost</span></div>
<div><strong data-o="power">–</strong><span>Suggested continuous power</span></div></div>
<a class="btn" style="margin-top:20px" href="../get-quotes.html">Get battery quotes</a></div>"""
    bat_explain = """<h2>How battery sizing works</h2>
<p>Storage needed = daily usage × share that is essential × (backup hours ÷ 24) ÷ usable depth of discharge. Lithium iron phosphate batteries typically allow 90 to 100% of their rated capacity to be used.</p>
<p>Capacity (kWh) decides how long you last; power (kW) decides what can run at once. A well pump, air conditioner or electric range can need 3 to 5 kW on start-up, so check the battery's peak rating against your largest motor load.</p>
<h3>With solar, you need less</h3>
<p>During a multi-day outage, panels recharge the battery each sunny day, so a battery sized for one night of essential loads often covers longer events. Without solar, size for the full outage.</p>"""
    bat_faq = [("Is a home battery worth it financially?", "Mainly where exported solar earns little, where peak-time rates are high, or where a rebate lowers the price. As pure backup it is insurance, valued differently by each household."),
               ("Can a battery run my whole house?", "It can if it is sized for it, but whole-home backup often needs two or three modules. Most owners back up a critical-loads panel instead.")]
    bat = calc_shell("tools/battery-backup-calculator.html", "Home battery backup calculator: what size solar battery? | Be.Solar",
                     "Battery backup calculator", "Size a home battery for the loads and outage length that matter to you.",
                     bat_form, bat_out, bat_explain, bat_faq,
                     "Calculate the home battery capacity, number of modules and cost you need for backup power during outages.")

    pay_form = f"""<form class="calc-form panel form" data-calc="payback" data-out="out4">
{COUNTRY_FIELD}
<div class="two">{field("bill","Monthly bill",160,cur=True)}{field("cpw","Installed cost","2.9",unit="per watt",cur=True)}</div>
<div class="two">{field("rate","Electricity price","0.18",unit="per kWh",cur=True)}{field("sun","Peak sun hours",4.6,unit="per day")}</div>
<div class="two">{field("credit","Tax credit",0,unit="% of cost")}{field("rebate","Rebates",0,cur=True)}</div>
<div class="two">{field("esc","Electricity price rise",3,unit="% a year")}{field("offset","Bill offset",100,unit="%")}</div>
</form>"""
    pay_out = """<div class="results" id="out4" aria-live="polite">
<p class="muted" style="margin:0">Payback period</p><p class="big" data-o="payback">–</p>
<div class="stat-list"><div><strong data-o="roi">–</strong><span>25-year return on cost</span></div>
<div><strong data-o="net">–</strong><span>Cost after incentives</span></div>
<div><strong data-o="save25">–</strong><span>Net 25-year gain</span></div>
<div><strong data-o="subsidy">–</strong><span>Incentives applied</span></div></div>
<div class="chart"></div>
<a class="btn" data-quote-link data-base="../get-quotes.html" href="../get-quotes.html">Compare real quotes</a></div>"""
    pay_explain = """<h2>Reading the result</h2>
<p>The payback period is the year when cumulative bill savings equal what you paid after incentives. Return on cost is net 25-year gain divided by that price. A 200% figure means every unit of currency spent returns three over 25 years: the original plus two in profit.</p>
<p>To compare with investing the money instead, divide the return by 25 for a rough simple annual figure, then remember that bill savings are usually not taxed as income, while investment returns often are.</p>
<h3>Loans and leases</h3>
<p>A loan adds interest, pushing payback out. A lease or power purchase agreement (PPA) usually means no upfront cost and smaller savings, with the provider keeping incentives. Neither is wrong; compare total cost over the term.</p>"""
    pay_faq = [("What makes solar pay back faster?", "Higher electricity prices, more sun, lower installed cost, larger incentives and using most of your solar power yourself rather than exporting it."),
               ("Does solar add value to a home?", "Several studies of owned (not leased) systems have found buyers pay a premium for homes with solar. Leased systems can complicate a sale, so read transfer terms carefully.")]
    pay = calc_shell("tools/payback-roi-calculator.html", "Solar payback and ROI calculator | Be.Solar",
                     "Solar payback & ROI calculator", "Find your break-even year and the return a solar system earns over its life.",
                     pay_form, pay_out, pay_explain, pay_faq,
                     "Calculate the payback period and 25-year return on investment of a home solar system after incentives.")

    hub_body = """<section class="page-head"><div class="wrap"><h1>Solar calculators</h1><p class="lede">Four free tools. Country presets for the US, Canada, UK, Australia and India, and every assumption can be changed.</p></div></section>
<section style="padding-top:8px"><div class="wrap"><div class="rows">
<a class="row" href="tools/solar-savings-calculator.html"><h3>Solar savings calculator</h3><p>The all-in estimate: size, price after incentives, savings and payback, with a 25-year chart.</p><span class="go">Open</span></a>
<a class="row" href="tools/system-size-calculator.html"><h3>System size &amp; panel count</h3><p>Kilowatts, panels and roof area from your monthly bill.</p><span class="go">Open</span></a>
<a class="row" href="tools/battery-backup-calculator.html"><h3>Battery backup sizing</h3><p>kWh of storage and modules for your essential loads and outage length.</p><span class="go">Open</span></a>
<a class="row" href="tools/payback-roi-calculator.html"><h3>Payback &amp; ROI</h3><p>Break-even year and lifetime return, including tax credits and rebates.</p><span class="go">Open</span></a>
</div>
<div class="notice" style="margin-top:28px">Calculators run entirely in your browser. Nothing you type is stored or sent anywhere unless you choose to request quotes.</div>
</div></section>""" + quote_band("")
    hub = page(path="tools.html", title="Free solar calculators: savings, size, battery and payback | Be.Solar",
               desc="Free solar calculators for savings, system size, battery backup and payback. Country presets and editable assumptions.",
               body=hub_body, active="tools.html")
    return {"tools/solar-savings-calculator.html": savings, "tools/system-size-calculator.html": size,
            "tools/battery-backup-calculator.html": bat, "tools/payback-roi-calculator.html": pay, "tools.html": hub}
