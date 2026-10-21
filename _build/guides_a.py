"""Guides, part A: decision and money guides."""

GUIDES_A = [
{
"slug": "is-solar-worth-it",
"title": "Is solar worth it in 2026? A five-factor test",
"desc": "Five numbers decide whether rooftop solar pays for your home. Here's how to check each one in minutes.",
"cat": "Getting started",
"body": """
<p>Solar is neither a sure win nor a scam. It is an investment whose return depends on five things you can check before a single installer visits. If four of the five look good, solar is very likely to pay off within its warranty. If two or fewer do, put the money somewhere else.</p>
<h2 id="price">1. What you pay for electricity</h2>
<p>This is the biggest lever. Every kilowatt-hour your panels make replaces one you would have bought, so the higher your rate, the faster solar pays back. Find your all-in rate by dividing the total on a recent bill (including delivery and fixed charges that vary with use) by the kWh you used.</p>
<ul><li><strong>Strong:</strong> above about $0.20 per kWh in the US and Canada, 24p in the UK, A$0.30 in Australia, or ₹7 in India.</li><li><strong>Marginal:</strong> rates well below these, such as parts of the US Northwest or Quebec, where hydro power keeps prices low.</li></ul>
<h2 id="sun">2. How much sun your roof sees</h2>
<p>Installers measure this in peak sun hours: the daily solar energy your location receives, expressed as hours of full-strength sunshine. Phoenix sees around 6, London around 2.7, Delhi around 5. A south-facing roof (north-facing south of the equator) with a pitch of 15 to 40 degrees captures most of it. East and west roofs typically lose 10 to 20%.</p>
<p>Shade matters more than most people think. A tree that shades part of an array at midday can cut its output disproportionately unless the system uses microinverters or optimisers. If your roof is shaded for more than a few hours a day, get a professional shade report.</p>
<h2 id="cost">3. What it costs to install</h2>
<p>Compare quotes in price per watt: the total price divided by the system's size in watts. A 7 kW system quoted at $19,600 is $2.80 per watt. National averages give you a benchmark. In the US, marketplace data puts the typical figure in the mid-$2 range per watt before incentives, while all-installs surveys report higher medians. Quotes well above your local norm deserve hard questions.</p>
<h2 id="incentives">4. Which incentives you can claim</h2>
<p>Incentives can cut 10 to 50% off the price, and they change often. In 2026 the picture looks like this:</p>
<ul><li><strong>United States:</strong> the 30% federal credit for homeowner-owned systems (Section 25D) ended for property placed in service after December 31, 2025. Leases and power purchase agreements can still benefit from a commercial credit claimed by the provider, within deadlines. State, utility and local programs remain. See our <a href="us-solar-tax-credit-2026.html">US tax credit guide</a>.</li><li><strong>India:</strong> the PM Surya Ghar central subsidy pays up to ₹78,000 for a 3 kW home system in most states.</li><li><strong>UK:</strong> 0% VAT on installed panels until 31 March 2027, plus export payments under the Smart Export Guarantee.</li><li><strong>Australia:</strong> small-scale technology certificates reduce the upfront price, falling each year until 2030, plus a federal battery discount.</li><li><strong>Canada:</strong> federal homeowner grants and loans for solar have closed; provincial and utility programs vary.</li></ul>
<h2 id="use">5. How you use and export power</h2>
<p>Where utilities credit exported power at the full retail rate (classic net metering), every kWh is worth the same whether you use it or export it. Many utilities have moved to paying less for exports. Then the share of solar power you use yourself, in daylight hours, matters a great deal. Households home during the day, with an EV that charges at midday or a heat pump, get more value from each panel.</p>
<h2 id="verdict">Putting it together</h2>
<p>Run your numbers through the <a href="../tools/solar-savings-calculator.html">savings calculator</a>. As a rule of thumb:</p>
<ul><li>Payback under 8 years: strong. Get quotes now.</li><li>8 to 12 years: reasonable, especially if electricity prices are rising or you plan to stay put.</li><li>Over 12 years: think twice, check whether a battery, a smaller system, community solar or efficiency upgrades would deliver more per dollar.</li></ul>
<div class="callout">Also weigh the roof. If it will need replacing within about 10 years, replace it first. Removing and reinstalling panels later commonly costs several thousand dollars.</div>
<h2 id="non-financial">Reasons beyond payback</h2>
<p>Some owners value price certainty, lower emissions or backup power during outages enough to accept a longer payback. That's legitimate, as long as you decide with clear numbers rather than a salesperson's monthly-payment pitch.</p>
""",
"faq": [("Do solar panels work on cloudy days?", "Yes, at reduced output, typically 10 to 25% of their rating under heavy cloud. Annual sun hours already account for cloudy weather, which is why Germany and the UK have large solar fleets."),
        ("How long do panels last?", "Most quality panels carry a 25-year performance warranty guaranteeing roughly 80 to 90% of original output, and many keep producing for 30 years or more. Inverters typically need replacement once in that period unless they are microinverters with long warranties.")]
},
{
"slug": "solar-panel-cost",
"title": "How much do solar panels cost? Prices by country and system size",
"desc": "Typical installed solar prices in the US, Canada, UK, Australia and India, and what moves a quote up or down.",
"cat": "Costs",
"body": """
<p>The fairest way to talk about solar prices is cost per watt: the full installed price divided by the system's DC capacity. It lets you compare a 6 kW quote with an 8 kW quote, and your quote with national data.</p>
<h2 id="benchmarks">2026 benchmarks by country</h2>
<div class="table-wrap"><table>
<thead><tr><th>Country</th><th>Typical price before incentives</th><th>Common home system</th><th>Ballpark total</th></tr></thead>
<tbody>
<tr><td>United States</td><td>About $2.50–$3.80 per W, depending on the source and market</td><td>7–12 kW</td><td>$20,000–$32,000</td></tr>
<tr><td>Canada</td><td>About C$2.50–$3.20 per W</td><td>6–10 kW</td><td>C$17,000–C$30,000</td></tr>
<tr><td>United Kingdom</td><td>About £1.50–£1.90 per W (0% VAT)</td><td>3.5–5 kW</td><td>£6,000–£9,000</td></tr>
<tr><td>Australia</td><td>About A$0.90–A$1.40 per W after STCs</td><td>6.6–10 kW</td><td>A$6,000–A$12,000</td></tr>
<tr><td>India</td><td>About ₹50,000–₹65,000 per kW before subsidy</td><td>2–5 kW</td><td>₹1.1–3.2 lakh</td></tr>
</tbody></table></div>
<p class="small muted">Ranges compiled from published marketplace data, national energy agencies and installer surveys in 2025–26. Local prices vary; treat these as sanity checks, not quotes.</p>
<h2 id="why-us-high">Why prices differ so much between countries</h2>
<p>Hardware costs roughly the same worldwide. The difference is "soft costs": permits, inspections, utility interconnection, sales and marketing, and labour. Australia's streamlined permitting and high-volume installers make it one of the cheapest markets in the world. US prices carry heavy customer-acquisition costs, often thousands of dollars per sale, plus local permitting that varies by town.</p>
<h2 id="drivers">What pushes a quote up or down</h2>
<ul>
<li><strong>Roof complexity.</strong> Multiple roof faces, steep pitches, tile or slate add labour.</li>
<li><strong>Equipment tier.</strong> Premium panels and microinverters cost more but may produce more on shaded or complex roofs.</li>
<li><strong>Electrical upgrades.</strong> An older main panel may need replacing, often adding $1,500 to $4,000 in North America.</li>
<li><strong>Batteries.</strong> Storage typically adds the price of a second system; quote it separately so you can compare.</li>
<li><strong>Financing.</strong> Loans with "dealer fees" can inflate the cash price by 15 to 30%. Always ask for the cash price.</li>
<li><strong>Company type.</strong> Local installers often beat national brands on price; national brands may offer stronger long-term service. Compare warranties, not logos.</li>
</ul>
<h2 id="size">Price by system size</h2>
<p>Larger systems cost less per watt because fixed costs (permits, design, the inverter's base cost, travel) spread over more panels. In the US, a 4 kW system may come in well above the national per-watt average while a 12 kW system comes in below it. Use the <a href="../tools/system-size-calculator.html">system size calculator</a> to find the size you actually need before comparing.</p>
<h2 id="hidden">Costs people forget</h2>
<ul><li>Inverter replacement after 10 to 15 years for string inverters (often $1,500–$3,000).</li><li>Removal and reinstallation if you reroof.</li><li>Monitoring subscriptions, which most systems no longer need.</li><li>Higher home insurance premiums in some markets; check with your insurer.</li></ul>
<div class="callout">Quick test: divide any quote's total by its watts. If it is more than about 20% above your local benchmark, ask the installer to explain line by line, then get another quote.</div>
""",
"faq": [("Is it cheaper to buy panels and install them myself?", "Hardware is often less than half of the price, so DIY can save a lot, but most utilities require a licensed electrician to connect, and permits and warranties can be harder to obtain. Plug-in balcony kits are a DIY-friendly option where allowed."),
        ("Will solar prices drop if I wait?", "Hardware prices have fallen steeply over the past decade, but soft costs fall slowly and incentives in several countries are shrinking on fixed schedules. Each year you wait also costs a year of savings.")]
},
{
"slug": "how-to-compare-solar-quotes",
"title": "How to compare solar quotes: a 12-point checklist",
"desc": "Line up quotes on price per watt, production, equipment and warranties, and spot the tricks that make a bad deal look good.",
"cat": "Buying",
"body": """
<p>Getting three quotes is the single most reliable way to save money on solar. The spread between the cheapest and most expensive bid for the same home is often a third or more. But quotes are formatted to make comparison hard. Put each one into the same twelve boxes.</p>
<h2 id="price">Price</h2>
<ol>
<li><strong>Cash price before incentives.</strong> Ask for it even if you plan to finance. It exposes hidden loan fees.</li>
<li><strong>Price per watt.</strong> Divide the cash price by the DC system size in watts.</li>
<li><strong>Incentives assumed.</strong> Check every incentive the quote subtracts actually applies to you. In the US, any quote still subtracting the 30% homeowner tax credit for a system installed in 2026 is out of date.</li>
</ol>
<h2 id="production">Production</h2>
<ol start="4">
<li><strong>Estimated annual kWh.</strong> The number that drives savings. Run it past an independent model such as NREL's PVWatts, or our <a href="../tools/system-size-calculator.html">sizing calculator</a>. An estimate more than about 10% above independent models is a red flag.</li>
<li><strong>Cost per kWh produced over 25 years.</strong> Divide the net price by 25 years of estimated production. This is the truest comparison between quotes of different sizes.</li>
<li><strong>Shade analysis.</strong> Ask how shading was measured: a site visit, drone or satellite.</li>
</ol>
<h2 id="equipment">Equipment</h2>
<ol start="7">
<li><strong>Panel make, model and wattage.</strong> Look up the datasheet: efficiency, temperature coefficient and degradation rate.</li>
<li><strong>Inverter type.</strong> String, string with optimisers, or microinverters. Microinverters and optimisers help on shaded or multi-face roofs.</li>
<li><strong>Battery, if any.</strong> Usable kWh, continuous kW, and whether it backs up the whole home or selected circuits.</li>
</ol>
<h2 id="warranty">Warranties and the company</h2>
<ol start="10">
<li><strong>Three warranties:</strong> product (panels, typically 25 years), performance (output guarantee), and workmanship (installer's labour and roof penetrations: 10 years is good, 25 is excellent).</li>
<li><strong>Who stands behind them.</strong> If the installer closes, who honours the workmanship warranty? Some offer third-party insured warranties.</li>
<li><strong>Licence and certification.</strong> Check the local electrical licence plus relevant certification: NABCEP in North America, MCS in the UK, SAA accreditation in Australia, MNRE-empanelled vendors for India's subsidy.</li>
</ol>
<h2 id="tricks">Common tricks</h2>
<ul>
<li><strong>Monthly payment framing.</strong> "Pay $150 instead of your $200 bill" hides a 25-year total. Compare totals.</li>
<li><strong>Inflated escalation.</strong> Projections assuming 5–6% annual electricity price rises make every system look great. Re-run them at 2–3%.</li>
<li><strong>Escalator leases.</strong> A lease that rises 2.9% a year can outpace your utility.</li>
<li><strong>Pressure.</strong> "This price expires today" is a sales tactic, not a market fact.</li>
</ul>
<div class="callout">Ready to collect quotes? <a href="../get-quotes.html">Request up to three</a> and use this checklist on each.</div>
""",
"faq": [("Should I always pick the cheapest quote?", "No. Pick the lowest cost per kWh over 25 years from an installer with solid warranties and reviews. A slightly higher price for much better workmanship cover is often worth it."),
        ("How long are quotes valid?", "Usually 14 to 30 days, because equipment prices and incentives change. A reasonable installer will extend a deadline while you compare.")]
},
{
"slug": "us-solar-tax-credit-2026",
"title": "The US solar tax credit in 2026: what ended and what's left",
"desc": "The 30% homeowner credit ended after 2025. Here's how leases, PPAs, state programs and batteries fit the new picture.",
"cat": "Incentives",
"body": """
<p>For more than a decade, the federal Residential Clean Energy Credit (Section 25D) let US homeowners subtract 30% of a solar system's cost from their federal income tax. The 2025 budget law ended it early. Here is what that means for anyone considering solar now.</p>
<h2 id="ended">What ended</h2>
<p>According to the IRS, the residential credit is not available for property placed in service after December 31, 2025. The test is when the system is installed and operating, not when you signed or paid. A homeowner who buys a system in 2026, with cash or a loan, cannot claim the federal credit for it.</p>
<p>If you installed a qualifying system in 2025 or earlier, you claim it on that year's return with IRS Form 5695, and unused credit can carry forward to later years.</p>
<h2 id="tpo">What remains: leases and PPAs</h2>
<p>Systems owned by a company, where you lease the equipment or buy its power under a power purchase agreement (PPA), can still qualify for a commercial clean-electricity credit (Section 48E) claimed by that company. Industry analyses describe deadlines: projects generally must begin construction by July 4, 2026, or otherwise be placed in service by the end of 2027, with energy storage treated more favourably. New restrictions on components from certain foreign entities also apply.</p>
<p>The provider, not you, receives that credit. Whether you benefit depends on how much of it is passed through as a lower lease payment or PPA rate. Compare offers on the total you will pay over the term.</p>
<h2 id="other">Incentives that still exist</h2>
<ul>
<li><strong>State tax credits and rebates.</strong> Several states run their own programs. They are not affected by the federal change.</li>
<li><strong>Utility rebates and performance payments.</strong> Some utilities pay per watt installed or per kWh produced.</li>
<li><strong>Solar renewable energy certificates (SRECs).</strong> In states with SREC markets, you earn certificates for your production and can sell them.</li>
<li><strong>Property and sales tax exemptions.</strong> Many states exempt solar's added home value from property tax, and some exempt equipment from sales tax.</li>
<li><strong>Net metering or export credits.</strong> The value of exported power is set by your state and utility.</li>
</ul>
<p>The independent DSIRE database (run by North Carolina State University) lists programs by state.</p>
<h2 id="math">How the math changed</h2>
<p>Losing a 30% credit raises net cost by roughly 43% for the same gross price (paying 100 instead of 70). On a $25,000 system that's $7,500 more out of pocket, typically adding three to five years to payback. Lower installer prices and rising electricity rates partly offset it in high-rate states.</p>
<div class="callout">Re-run your numbers with the <a href="../tools/payback-roi-calculator.html">payback calculator</a>: set the tax credit to 0% for an owned system, then compare against a lease or PPA offer's total cost.</div>
<h2 id="batteries">Batteries</h2>
<p>Home batteries installed by homeowners lost the federal residential credit at the same time. Batteries in third-party-owned arrangements may still be covered by commercial credits. Several states and utilities offer battery-specific incentives or pay owners to share stored power during grid peaks.</p>
<p class="small muted">This guide summarises public sources including the IRS and industry associations. Tax rules depend on your circumstances; confirm with a tax professional before deciding.</p>
""",
"faq": [("Can I still claim the credit if I signed a contract in 2025 but my system was installed in 2026?", "Under the IRS guidance, the credit is not available for property placed in service after December 31, 2025, so a 2026 installation generally does not qualify. Confirm the specifics with a tax adviser."),
        ("Is leasing better now?", "Sometimes. A lease or PPA may carry savings from the commercial credit, but you won't own the system, and escalators and transfer terms matter. Compare 20–25-year totals against buying with cash or a low-rate loan.")]
},
{
"slug": "solar-lease-vs-loan-vs-cash",
"title": "Solar lease vs loan vs cash: which way to pay?",
"desc": "How each payment route changes your savings, who keeps the incentives, and what happens when you sell the house.",
"cat": "Financing",
"body": """
<p>How you pay for solar can matter as much as which panels you buy. The same system can return large savings or barely break even depending on the deal. Here are the three routes and the questions that separate good offers from bad ones.</p>
<h2 id="cash">Cash purchase</h2>
<p><strong>How it works:</strong> you pay the installer up front and own the system outright.</p>
<ul><li><strong>Pros:</strong> the highest lifetime savings, any owner incentives are yours, and no interest.</li><li><strong>Cons:</strong> a large upfront outlay, and the opportunity cost of money that could earn a return elsewhere.</li></ul>
<p><strong>Best for:</strong> homeowners with savings who plan to stay five years or more.</p>
<h2 id="loan">Solar loan</h2>
<p><strong>How it works:</strong> a lender pays the installer; you repay over 10 to 25 years and own the system from day one.</p>
<ul><li><strong>Pros:</strong> little or no money down while you still own the system.</li><li><strong>Cons:</strong> interest, and sometimes hidden "dealer fees" built into the price to advertise a low rate.</li></ul>
<p>Ask for the cash price and the loan price side by side. If the financed price is higher, that difference is a fee. A home-equity loan or credit-union loan at a fair rate can beat installer financing.</p>
<h2 id="lease">Lease or power purchase agreement (PPA)</h2>
<p><strong>How it works:</strong> a company owns panels on your roof. With a lease you pay a fixed monthly amount; with a PPA you pay per kWh the system produces, usually below the utility rate.</p>
<ul><li><strong>Pros:</strong> no upfront cost; the provider handles maintenance; in the US, the provider may still access commercial tax credits that homeowners lost.</li><li><strong>Cons:</strong> smaller savings, escalators that raise payments each year, and transfer paperwork when you sell.</li></ul>
<h2 id="compare">A side-by-side example</h2>
<div class="table-wrap"><table><thead><tr><th></th><th>Cash</th><th>Loan (7%, 15 yrs)</th><th>PPA (escalator 2.9%)</th></tr></thead>
<tbody><tr><td>Upfront cost</td><td>$21,000</td><td>$0</td><td>$0</td></tr>
<tr><td>Who owns it</td><td>You</td><td>You</td><td>Provider</td></tr>
<tr><td>Typical 25-year net savings*</td><td>Highest</td><td>Middle</td><td>Lowest, can be near zero</td></tr>
<tr><td>Main risk</td><td>Tying up cash</td><td>Fees and interest</td><td>Escalator outpacing utility rates</td></tr></tbody></table></div>
<p class="small muted">*Illustrative only. Results depend on your rate, production and terms. Model your own numbers with the <a href="../tools/payback-roi-calculator.html">payback calculator</a>.</p>
<h2 id="questions">Five questions for any financing offer</h2>
<ol><li>What is the cash price, and what is the total I will pay over the full term?</li><li>Is there a dealer fee or origination fee, and how much?</li><li>Does the payment rise each year, and by how much?</li><li>What happens if I sell the house: transfer, buyout, or prepay?</li><li>Who maintains and insures the system, and who pays for inverter replacement?</li></ol>
<h2 id="selling">Selling a home with solar</h2>
<p>Owned systems generally add value and are simple to sell. Loans may need paying off at closing, depending on whether they are secured on the property. Leases and PPAs require the buyer to qualify and agree to take over the contract, which some buyers resist. Read transfer clauses before signing.</p>
""",
"faq": [("Is a $0-down offer really free?", "No. It is financing. You pay through a loan, lease or PPA. It can still be a good deal, but compare the total cost over the contract."),
        ("Can I pay off a solar loan early?", "Most solar loans allow prepayment without penalty, but check. Some loans assume you'll make a lump-sum payment early and raise the monthly payment if you don't.")]
},
{
"slug": "net-metering-and-export-rates-explained",
"title": "Net metering and export rates, explained",
"desc": "What happens to the solar power you don't use, why export rates are falling, and how that changes system size and batteries.",
"cat": "How solar works",
"body": """
<p>On a sunny afternoon, a typical home solar system makes more power than the house uses. The surplus flows to the grid through your meter. What your utility pays or credits for that power decides a large share of solar's value.</p>
<h2 id="classic">Classic net metering</h2>
<p>Under full retail net metering, your meter effectively runs backwards. Each kWh exported earns a credit equal to the price you pay to import one. The grid acts like a free battery, and system size simply follows annual usage.</p>
<h2 id="net-billing">Net billing and export tariffs</h2>
<p>Many places have moved to paying less for exports than for imports. California's 2023 switch to net billing, for example, values exports based on the utility's avoided costs, which are usually far below retail rates. In the UK, suppliers set their own Smart Export Guarantee rates, typically a fraction of import prices. Australian feed-in tariffs have fallen to a few cents per kWh in many states.</p>
<h2 id="self-consumption">Why self-consumption now matters</h2>
<p>When exports are worth less, every kWh you use yourself is worth more than one you export. Practical ways to use more of your own solar:</p>
<ul><li>Run dishwashers, laundry and pool pumps in the middle of the day with timers.</li><li>Charge an EV at home around midday, or with a solar-aware charger.</li><li>Heat water with a heat pump water heater or a solar diverter.</li><li>Pre-cool or pre-heat the home with a heat pump in the afternoon.</li><li>Add a battery to shift evening use, especially under time-of-use tariffs.</li></ul>
<h2 id="tou">Time-of-use rates</h2>
<p>Many utilities charge more in the late afternoon and evening. West-facing panels produce more in that window and can be worth more per kWh than south-facing ones, even though they produce less in total. A battery charged at noon and drained at 6 pm captures the gap.</p>
<h2 id="sizing">How export rates change sizing</h2>
<p>Under full net metering, cover 100% of annual usage. Under low export rates, size for daytime use, often 60 to 80% of the bill, unless a battery or EV will absorb the surplus. Our <a href="../tools/solar-savings-calculator.html">savings calculator</a> counts only self-used energy by default, which is conservative.</p>
<h2 id="check">How to find your rules</h2>
<ol><li>Search your utility's website for "net metering", "net billing", "export tariff" or "feed-in tariff".</li><li>Note the export rate, any monthly fixed charges for solar customers, and how credits roll over.</li><li>Ask installers to model savings under your exact tariff, not a generic one.</li></ol>
<div class="callout">Rules can change after you install. Many jurisdictions protect existing customers for a set period. Ask whether your terms are guaranteed, and for how long.</div>
""",
"faq": [("Will my utility pay me cash for extra solar?", "Usually you receive bill credits. Some programs pay out surplus credits once a year, often at a low rate. UK SEG payments are made by your export supplier."),
        ("Do I need a new meter?", "Usually, yes: a bidirectional or smart meter that records imports and exports separately. Your utility typically installs it after the system passes inspection.")]
},
]
