"""Guides, part B: technology, process, protection."""

GUIDES_B = [
{
"slug": "how-solar-panels-work",
"title": "How solar panels work, from photon to power socket",
"desc": "A clear walkthrough of solar cells, inverters, meters and the grid, without the jargon.",
"cat": "How solar works",
"body": """
<p>A home solar system has four working parts: panels that turn light into direct current, an inverter that turns it into household alternating current, a meter that records what flows to and from the grid, and the wiring and protection devices that keep it safe.</p>
<h2 id="cells">Inside a solar cell</h2>
<p>Most panels use crystalline silicon cells. Each cell is a thin wafer treated so one side has extra electrons and the other has spaces for them. Where those layers meet, an electric field forms. When light strikes the cell, its energy knocks electrons loose; the field pushes them one way, creating a current. This is the photovoltaic effect.</p>
<p>A single cell produces about half a volt. Panels wire 54 to 72 cells (or twice as many half-cut cells) in series to reach useful voltages. A modern residential panel is rated around 400 to 450 watts under standard test conditions.</p>
<h2 id="efficiency">Efficiency and why it matters less than you think</h2>
<p>Efficiency is the share of sunlight hitting a panel that becomes electricity. Mainstream panels in 2026 convert roughly 20 to 23%. Higher efficiency means more watts per square metre, which matters on a small roof but barely matters if you have space. Price per watt and warranty usually matter more.</p>
<p>Heat lowers output. The temperature coefficient (around −0.3% per °C for good panels) tells you how much power drops on hot days.</p>
<h2 id="inverters">Inverters</h2>
<ul><li><strong>String inverter:</strong> one box converts power from a series of panels. Cheapest, but the weakest panel can limit the string.</li><li><strong>Optimisers:</strong> small units on each panel tune its output before a central inverter. Good for partial shade.</li><li><strong>Microinverters:</strong> one inverter per panel; each works independently and is monitored individually.</li><li><strong>Hybrid inverter:</strong> also manages a battery.</li></ul>
<h2 id="grid">Connection to the grid</h2>
<p>Inverter output feeds your main electrical panel. Your home uses solar power first; the surplus flows out to the grid and is recorded by the meter. At night you draw from the grid as normal.</p>
<p>Grid-tied inverters shut down automatically during a power cut to protect line workers. That's why panels alone don't keep the lights on in an outage. Backup requires a battery or a specific inverter with an isolated backup mode.</p>
<h2 id="monitoring">Monitoring</h2>
<p>Most systems include an app showing production in real time. Check it monthly. A sudden drop compared with the same month last year can signal a tripped breaker, a failed inverter or heavy soiling.</p>
<div class="video" style="margin:1.4em 0"><button class="yt-facade" data-yt="xKxrkht7CpY" aria-label="Play: How do solar panels work? (TED-Ed)"></button></div>
<p class="small muted">Video: TED-Ed, "How do solar panels work?" by Richard Komp, embedded from YouTube.</p>
""",
"faq": [("Do solar panels need direct sunlight?", "They produce most in direct sun but also generate under diffuse light on overcast days, just less."),
        ("What's the difference between kW and kWh?", "kW measures power, the rate of flow at a moment. kWh measures energy, power over time. A 7 kW system making full power for one hour produces 7 kWh.")]
},
{
"slug": "home-battery-guide",
"title": "Home solar batteries: are they worth it, and what size?",
"desc": "When storage pays, when it's just insurance, and how to size a battery for backup or savings.",
"cat": "Batteries",
"body": """
<p>Batteries are now attached to a large and growing share of new residential solar systems. US national lab data show storage paired with more than a third of 2025 installs. Popularity doesn't make them right for every home. Decide by which job you need the battery to do.</p>
<h2 id="jobs">Three jobs a battery can do</h2>
<ol><li><strong>Backup power.</strong> Keep essentials running during outages. Value depends on how often your power fails and what an outage costs you.</li><li><strong>Self-consumption.</strong> Store daytime solar for the evening instead of exporting it cheaply. Pays where export rates are low.</li><li><strong>Rate arbitrage and grid services.</strong> Charge when power is cheap, discharge at peak, or join a virtual power plant that pays for access to your battery.</li></ol>
<h2 id="pays">When batteries pay for themselves</h2>
<p>Storage has the best financial case where export rates are far below import rates, where time-of-use tariffs have a large peak-to-off-peak gap, or where a subsidy covers a big share of the cost. Australia's federal Cheaper Home Batteries program, for instance, has given roughly a 30% upfront discount through certificates since July 2025, with the discount tapering for larger batteries and falling over time.</p>
<p>Where full net metering is available, a battery rarely pays back on savings alone: the grid already "stores" your surplus at full value.</p>
<h2 id="size">Sizing</h2>
<ul><li><strong>Capacity (kWh)</strong> is how much energy it holds. For evening self-consumption, size near your evening and overnight use, often 8 to 15 kWh.</li><li><strong>Power (kW)</strong> is how much it can deliver at once. Starting a well pump or air conditioner needs a high peak rating.</li><li><strong>Usable capacity</strong> matters more than nominal. Lithium iron phosphate batteries usually allow 90–100% to be used.</li></ul>
<p>Try the <a href="../tools/battery-backup-calculator.html">battery backup calculator</a> to size for your loads.</p>
<h2 id="chemistry">Chemistry and lifespan</h2>
<p>Lithium iron phosphate (LFP) dominates new home batteries thanks to safety and long cycle life, often warranted for 10 years and thousands of cycles with at least 60 to 70% capacity retained. Check the warranty's throughput limit (total MWh) as well as years.</p>
<h2 id="install">Installation notes</h2>
<ul><li>Batteries must be installed to fire codes, often in garages or outside walls rather than living spaces.</li><li>Whole-home backup may need an automatic transfer switch and a main panel upgrade; critical-loads backup is cheaper.</li><li>Adding a battery to existing solar is possible. AC-coupled batteries work with almost any inverter.</li></ul>
<div class="callout">If outages are rare and your export credit is fair, skip the battery for now and leave space and wiring to add one later.</div>
""",
"faq": [("How long will a battery power my home?", "Divide usable kWh by your hourly load. A 13.5 kWh battery running 1 kW of essentials lasts about 13 hours, longer if solar recharges it during the day."),
        ("Can I go completely off-grid?", "Possible, but it needs far more storage and panels to cover winter, often plus a generator. For most connected homes, staying grid-tied is much cheaper.")]
},
{
"slug": "solar-installation-process-timeline",
"title": "The solar installation process: what happens and how long it takes",
"desc": "From first quote to switching on: site survey, design, permits, installation, inspection and grid approval.",
"cat": "Buying",
"body": """
<p>The physical installation of a home solar system usually takes one to three days. The whole process, from signing to switching on, typically takes one to three months, mostly spent on paperwork. Knowing the steps helps you spot delays and ask the right questions.</p>
<h2 id="steps">The steps, in order</h2>
<ol>
<li><strong>Quotes and contract (1–3 weeks).</strong> Compare at least three. Read the contract for payment milestones; avoid paying most of the price before installation.</li>
<li><strong>Site survey (a day).</strong> A technician inspects the roof structure, measures, checks the main electrical panel and confirms shading.</li>
<li><strong>Engineering and design (1–2 weeks).</strong> Final panel layout, structural calculations and electrical drawings. Ask to approve the layout before permitting.</li>
<li><strong>Permits and utility application (2–8 weeks).</strong> The installer applies for building or electrical permits and, in most places, permission to connect to the grid. Some jurisdictions use instant online permitting; others take months.</li>
<li><strong>Installation (1–3 days).</strong> Racking, panels, inverter, wiring and any battery. Expect some noise and a short power shut-off.</li>
<li><strong>Inspection (1–3 weeks).</strong> A local inspector checks the work against code.</li>
<li><strong>Permission to operate (1–4 weeks).</strong> The utility approves connection and may swap your meter. Don't switch the system on before this unless your installer confirms it's allowed.</li>
</ol>
<h2 id="country">Country-specific notes</h2>
<ul><li><strong>UK:</strong> most domestic systems are permitted development and need no planning permission (listed buildings and conservation areas differ). Use an MCS-certified installer if you want export payments.</li><li><strong>Australia:</strong> use an accredited installer to receive STCs; the retailer or distributor must approve the connection.</li><li><strong>India:</strong> for PM Surya Ghar, apply through the national portal, use a registered vendor, and the subsidy is paid after inspection and net-meter installation.</li><li><strong>US:</strong> timelines vary widely by town and utility; ask installers how long recent local projects took.</li></ul>
<h2 id="prepare">How to prepare</h2>
<ul><li>Clear access to the roof, attic and main panel.</li><li>Tell your home insurer before installation.</li><li>Check homeowners' association rules where applicable.</li><li>Photograph the roof and ceilings beforehand as a record.</li></ul>
<h2 id="after">After switch-on</h2>
<p>Install the monitoring app, record the commissioning date and serial numbers, and file warranties. Compare the first full year of production with the installer's estimate.</p>
""",
"faq": [("Will installation damage my roof?", "A competent installer seals every penetration and warrants workmanship, usually for 10 years or more. Ask how roof penetrations are flashed and who covers leaks."),
        ("Do I need to be home during installation?", "Usually only at the start and end, and when power is switched off. Installers need access to the electrical panel.")]
},
{
"slug": "solar-scams-red-flags",
"title": "Solar scams and red flags: how to protect yourself",
"desc": "The sales tactics, contract traps and fake 'government programs' to watch for, and what to do if things go wrong.",
"cat": "Consumer protection",
"body": """
<p>Most solar companies are honest, but the industry's fast growth and large ticket sizes attract aggressive sellers and outright fraud. Consumer agencies in several countries have warned about misleading solar sales. These warning signs cover most of the problems.</p>
<h2 id="pitch">Red flags in the pitch</h2>
<ul>
<li><strong>"Free solar" or "a new government program."</strong> There is no program that installs panels for free. Usually it's a lease, PPA or loan.</li>
<li><strong>Same-day pressure.</strong> Discounts that vanish if you don't sign now.</li>
<li><strong>Your bill will be "zero".</strong> Most connected homes still pay fixed grid charges.</li>
<li><strong>Outdated incentives.</strong> A US seller promising a 30% tax credit on an owned system installed after 2025 is wrong.</li>
<li><strong>Asking for utility login details</strong> or signing documents on a tablet without giving you time to read.</li>
<li><strong>Impersonating your utility</strong> or claiming to be partnered with it.</li>
</ul>
<h2 id="contract">Red flags in the contract</h2>
<ul>
<li>Large deposits before any work, beyond a modest booking fee.</li>
<li>Payment escalators above typical utility increases.</li>
<li>No production estimate or performance guarantee.</li>
<li>Vague equipment ("tier-1 panels") instead of model numbers.</li>
<li>Loan terms with a price much higher than the cash price, signalling hidden fees.</li>
<li>Liens or fixture filings on your property not explained to you.</li>
</ul>
<h2 id="check">Five checks before signing</h2>
<ol><li>Verify the contractor licence with your local licensing board.</li><li>Check certification: NABCEP, MCS, SAA or MNRE empanelment as relevant.</li><li>Read independent reviews from more than one site, sorted by most recent.</li><li>Ask for three local references with systems at least two years old.</li><li>Confirm your cooling-off period. Many jurisdictions give a few days to cancel door-to-door sales.</li></ol>
<h2 id="wrong">If something goes wrong</h2>
<ul><li>Raise the issue in writing with the company and keep copies.</li><li>Escalate to the panel or inverter manufacturer for product faults; warranties often survive the installer.</li><li>Complain to the relevant regulator: state attorney general or consumer protection office in the US, Trading Standards or the relevant consumer code body in the UK, your state fair trading office in Australia, or consumer forums in India.</li><li>If your installer has closed, look for a third-party warranty provider or another installer who services orphaned systems.</li></ul>
""",
"faq": [("Are door-to-door solar sellers always bad?", "No, but the format favours pressure. Treat any doorstep offer as one quote among three and never sign on the spot."),
        ("How do I know if an incentive is real?", "Check official government or utility sites directly rather than links provided by a seller. Our incentives pages link to official sources.")]
},
{
"slug": "community-solar-renters-plug-in-solar",
"title": "Solar for renters and apartments: community solar and plug-in kits",
"desc": "No roof of your own? Community solar subscriptions, balcony panels and landlord deals can still cut your bill.",
"cat": "Getting started",
"body": """
<p>Rooftop solar has mostly been for detached homeowners. If you rent, live in an apartment or have an unsuitable roof, there are still ways in.</p>
<h2 id="community">Community solar</h2>
<p>A community solar project is a shared solar farm, typically in your utility territory. You subscribe to a share of its output and receive credits on your electricity bill, usually at a discount of 5 to 15% off what that power would cost. No installation, and many plans let you cancel with notice. Availability depends on state or regional programs; in the US, a number of states have active programs.</p>
<p><strong>What to check:</strong> the guaranteed discount, the contract length and cancellation fees, whether payments rise over time, and what happens if you move.</p>
<h2 id="plug-in">Plug-in and balcony solar</h2>
<p>Small kits of one to four panels with a microinverter that plugs into a wall socket are popular in Germany, where millions are registered. They typically produce a few hundred kWh a year, enough to cover a home's constant background load. Rules differ by country: some limit output or require registration, others don't yet allow plug-in connection. Check local rules before buying.</p>
<h2 id="landlord">Working with a landlord</h2>
<p>Some landlords will install solar if the numbers are clear. Share a calculator estimate and a quote. Arrangements include the landlord owning the system and charging a modest rent increase, or a shared-savings agreement. For apartment buildings, a common-area system can cut service charges, and in India the PM Surya Ghar scheme offers support for housing societies' common facilities.</p>
<h2 id="other">Other ways to cut your bill</h2>
<ul><li>Choose a green or time-of-use tariff and shift use to cheaper hours.</li><li>Switch to LED lighting and efficient appliances.</li><li>Use smart plugs to kill standby loads.</li></ul>
<div class="callout">Planning to buy a home later? Run the <a href="../tools/solar-savings-calculator.html">savings calculator</a> on listings you're considering. A south-facing, unshaded roof is a real long-term asset.</div>
""",
"faq": [("Can I take community solar with me if I move?", "Often yes within the same utility territory; otherwise most contracts allow cancellation, sometimes with notice or a fee."),
        ("Is plug-in solar safe?", "Certified kits designed for plug-in use shut off when unplugged and are limited in output. Use only certified equipment and follow local rules.")]
},
{
"slug": "solar-panel-maintenance-cleaning",
"title": "Solar panel maintenance and cleaning: what's actually needed",
"desc": "How to keep a system producing for 25+ years with minimal effort, and when cleaning is worth paying for.",
"cat": "Ownership",
"body": """
<p>Solar panels have no moving parts and need little care. A few habits keep a system near its expected output for decades.</p>
<h2 id="monitor">Watch the numbers</h2>
<p>Your monitoring app is the best maintenance tool. Compare each month's production with the same month last year. A drop of more than 10% without obvious weather reasons deserves a look. Microinverter systems show each panel separately, making faults easy to locate.</p>
<h2 id="cleaning">Cleaning</h2>
<p>Rain cleans most tilted panels well enough. Studies of soiling losses generally find a few percent in typical climates, but much more in dry, dusty regions, near farms, deserts or construction, and under bird droppings. Practical guidance:</p>
<ul><li>Clean when you can see dirt or production has dipped, not on a fixed schedule.</li><li>Use soft water and a soft brush or sponge from the ground with an extension pole. Avoid pressure washers, abrasive cleaners and walking on panels.</li><li>Clean in early morning or evening; cold water on hot glass can stress it.</li><li>In dusty climates such as north India or inland Australia, monthly cleaning in the dry season can pay for itself.</li></ul>
<h2 id="checks">Annual checks</h2>
<ul><li>Look for cracked glass, discoloured cells or loose wiring visible from the ground.</li><li>Trim trees that have grown into the sun path.</li><li>Check under the array for nesting birds or rodents; mesh guards are inexpensive.</li><li>Look at inverter lights or error codes.</li></ul>
<h2 id="pro">When to call a professional</h2>
<ul><li>Inverter faults or errors that don't clear on restart.</li><li>Any burning smell, scorch marks or damaged cables.</li><li>After major storms or roof work.</li><li>A professional inspection every few years is sensible for older systems.</li></ul>
<h2 id="lifespan">Expected lifespan</h2>
<p>Panels typically degrade around 0.3 to 0.5% a year. String inverters often need replacing after 10 to 15 years; microinverters often carry 25-year warranties. Budget for one inverter replacement over the life of a string system.</p>
""",
"faq": [("Does snow damage panels?", "Panels are rated for snow loads, and snow usually slides off tilted panels within days. Don't scrape them with metal tools."),
        ("Can I use a garden hose?", "Yes, with soft water from the ground. Hard water can leave spots; a final rinse with deionised water helps.")]
},
]
