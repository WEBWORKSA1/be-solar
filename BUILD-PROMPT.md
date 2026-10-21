# Be.Solar — Idea and Phase-wise Build Prompt

## 1. The idea: an independent solar decision engine with a lead-gen core

**Positioning:** "Know your solar numbers before anyone tries to sell you panels." Be.Solar is an independent desk for homeowners in five markets (US, Canada, UK, Australia, India): instant calculators, plain-language guides, an incentive tracker, and a quote marketplace that routes each request to at most three vetted installers.

**Why this beats the alternatives for this domain**

| Option | Revenue per 1,000 visitors (est.) | Verdict |
|---|---|---|
| Pure solar news blog (AdSense only) | Low: AdSense pays the publisher a share of the click price, typically cents to a few dollars per click | Weak alone |
| Solar e-commerce / dropship | Margin on hardware, heavy ops, returns | Wrong fit for a static site |
| **Calculator + guides + installer lead marketplace** | Leads sell for roughly $40–$400 each to installers (US); ads and donations on top | **Chosen** |

Unit economics to aim for: a 2–4% visitor-to-lead rate on calculator and guide traffic. At 10,000 monthly visits, 2% conversion and a conservative $40/lead, that is about $8,000/month from leads before any AdSense income. Advertiser-side CPCs for installer keywords run around $10–$28 in the US, which signals both strong lead value and above-average AdSense rates on these pages.

**Revenue stack, in order of value:** (1) installer leads and partner subscriptions, (2) AdSense (auto ads, kept away from the quote flow), (3) sponsorships of calculators, guides, newsletter and contest prizes, (4) reader donations, (5) domain/website acquisition interest (offer bar on every page).

**Moat to build next:** a quarterly "Be.Solar price index" from quote data, the same data asset that makes Solar Choice and EnergySage cited sources.

## 2. Research basis

37 solar sites were reviewed: EnergySage, SolarReviews, Solar.com, Project Sunroof, NREL PVWatts, SolarQuotes, Solar Choice, Forbes Home, This Old House, Bob Vila, EnergyBot, Sunrun, Tesla, Palmetto, Freedom Forever, SunPower, Enphase, Solar Insure, Aurora, OpenSolar, pv magazine, PV Tech, Solar Power World, Mercom, SolarQuarter, CleanTechnica, Canary Media, Electrek, Ember, IEA, IRENA, SEIA, Energy Saving Trust, MCS, Clean Energy Council, Solar United Neighbors and Solar Energy UK.

Patterns adopted:
- Results without an email wall.
- A multi-step quote form with a progress bar.
- An ownership question that diverts renters instead of discarding them.
- Consent text naming the number of installers.
- Repeated quote CTAs and a sticky mobile CTA.
- Editorial trust stack and transparent formulas.
- An incentive tracker with official sources.
- A donation module with once or monthly gifts.
- Contests.
- A glossary.
- FAQ schema.

## 3. Phase-wise build prompt

Use these prompts in order with any capable AI coding assistant. Each phase ends with a testable result.

### Phase 1: Foundation and compliance
> Build a static HTML/CSS/JS site for the domain be.solar, hostable on GitHub Pages free plan (no server code, relative links, `.nojekyll`). Include in every page `<head>`:
> - the Google AdSense tag for ca-pub-6620975821265271
> - meta description, canonical, Open Graph, JSON-LD Organization
>
> Add at the very top of every page an offer bar: "Interested in this website, the Be.Solar domain name, sponsorship, advertising or partnership? Contact us", linked to https://web.works/contact.
>
> Create the following:
> - `ads.txt` (`google.com, pub-6620975821265271, DIRECT, f08c47fec0942fa0`), `robots.txt`, `sitemap.xml` and a 404 page.
> - Privacy and cookie policy with Google advertising-cookie disclosures and opt-out links.
> - Terms of use.
> - Disclaimer with a trademark and copyright notice stating no affiliation with any "BeSolar"/"Be Solar" mark.
> - About and Contact pages.
>
> Add a cookie consent banner offering two choices: Accept all and Essential only.

### Phase 2: Design system
> Design tokens:
> - Colours: ink #13293D, sun #F4A300, cell blue #1D4E89, leaf green #1B7F66, cool background #F4F7FA, plus a dark theme.
> - Fonts: Bricolage Grotesque (display) and Public Sans (body).
>
> Layout and interaction:
> - Left-aligned layouts.
> - List rows instead of identical cards.
> - Visible keyboard focus; respect reduced motion.
> - Mobile-first down to 360px, with a sticky "Get free solar quotes" bar on mobile.
>
> Hero: an interactive "sun dial". A country selector and a monthly-bill slider move a sun along an arc and update three outputs live:
> - 25-year net savings
> - system kW
> - panel count

### Phase 3: Calculators (client-side, no data stored)
> Build a shared solar model with country presets (US, CA, UK, AU, IN, Other). Each preset sets currency, electricity price, peak sun hours, installed cost per watt and grid CO₂.
>
> Formulas:
> - kW = annual kWh × offset ÷ (sun hours × 365 × 0.8)
> - Panels assume 430 W.
> - Degradation is 0.5% per year.
> - Electricity prices escalate at a user-set rate.
> - Self-use is capped at the home's own consumption.
> - India's PM Surya Ghar subsidy is applied automatically (₹30k/kW for 2 kW + ₹18k for the 3rd kW, maximum ₹78k).
>
> Pages, each with an explanation, an FAQ and WebApplication + FAQPage schema:
> 1. Savings calculator with a 25-year cumulative cash bar chart (SVG).
> 2. System size and panel count.
> 3. Battery backup sizing.
> 4. Payback and ROI.

### Phase 4: Lead generation engine
> Build `get-quotes.html` as a 5-step wizard with a progress bar and validation per step:
> 1. Country, postal code, ownership (renters diverted to community solar), property type
> 2. Monthly bill slider and utility
> 3. Shade, roof age, roof material
> 4. Interests, payment method, timeline, optional credit band
> 5. Name, email, phone, address, best time, and an explicit consent checkbox naming "up to three installers"
>
> Add a live estimate side panel and pass the bill and country from any calculator via the query string. Include the estimate and a computed lead score (Hot/Warm/Nurture) in the submission.
>
> Submit through FormSubmit's AJAX endpoint to the site inbox. The address must be assembled at runtime from encoded fragments so it never appears in page source or on screen. Add a honeypot field. The thank-you state shows a quote-comparison checklist.

### Phase 5: Content for AdSense approval and SEO
> Write at least 16 original, people-first guides (800–1,200 words each). Each guide carries a table of contents, FAQ, Article, FAQPage and Breadcrumb schema, related guides and an end-of-article quote CTA. Topics:
> - Is solar worth it
> - Costs by country
> - Comparing quotes
> - The US tax credit after 25D ended
> - Lease vs loan vs cash
> - Net metering
> - How panels work
> - Batteries
> - Installation timeline
> - Scams
> - Renters and community solar
> - Maintenance
> - India PM Surya Ghar
> - UK VAT/SEG
> - Australia STC/batteries
> - Canada incentives
>
> Also build:
> - An incentives-by-country page with official source links and a "last reviewed" date
> - A glossary with DefinedTermSet schema
> - A video library: click-to-load YouTube embeds via youtube-nocookie, plus topic searches

### Phase 6: Community and monetisation extras
> Build these pages:
> - **Support:** donation tiers ($5 / $25 / $100 / $500+) feeding a pledge form with amount, frequency, payment method and fund direction (operations, hiring, contests, promotion); a sponsorship inquiry form; a "not tax-deductible" note.
> - **Contests:** monthly photo, savings story and video contests plus a student challenge, each with an entry form and official rules ("no purchase necessary").
> - **Careers:** role list and application form.
> - **Partners:** an installer partner application (service areas, monthly volume, certifications, licence confirmation) and advertising options.

### Phase 7: Deploy and launch
> 1. Push to github.com/WEBWORKSA1/be-solar on branch `main`.
> 2. Enable GitHub Pages (Settings → Pages → Deploy from branch → main / root).
> 3. To use be.solar:
>    - Add a `CNAME` file containing `be.solar`.
>    - Point apex A records to 185.199.108.153, 185.199.109.153, 185.199.110.153 and 185.199.111.153.
>    - Point `www` CNAME to webworksa1.github.io.
>    - Enable "Enforce HTTPS".
> 4. Submit the sitemap in Google Search Console.
> 5. Apply for AdSense on the custom domain and enable Google's certified CMP for EEA/UK/CH consent.
> 6. Activate FormSubmit by confirming the first submission's email, then optionally switch to its random alias.

### Phase 8: Growth (after launch)
- Replace the national averages with the NREL PVWatts API (US) and add an address-based roof estimate.
- Publish state/province/city cost pages and "best installers in [state]" pages with a methodology.
- Start the quarterly price index from anonymised quote data.
- Add an installer directory with reviews.
- Run a weekly incentive-alert newsletter.
- Add Hindi and Spanish versions.
