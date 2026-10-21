# Be.Solar

Independent solar calculators, guides, incentive tracker and installer quote marketplace for be.solar. Static site that runs free on GitHub Pages.

- **Live (GitHub Pages):** https://webworksa1.github.io/be-solar/
- **Build prompt and strategy:** [BUILD-PROMPT.md](BUILD-PROMPT.md)

## Structure
| Path | What it is |
|---|---|
| `index.html` | Home with the interactive sun-dial estimator |
| `get-quotes.html` | 5-step lead-generation wizard with live estimate and lead score |
| `tools/` | Savings, system size, battery and payback calculators |
| `guides/` | 16 original guides |
| `incentives.html`, `glossary.html`, `videos.html` | Reference pages |
| `support.html`, `contests.html`, `careers.html`, `partners.html` | Donations, contests, hiring, installer partners and advertising |
| `privacy.html`, `terms.html`, `disclaimer.html` | Legal pages, including the trademark and copyright disclosure |
| `assets/` | CSS, JS and icon |
| `_build/` | Python generator. Edit content there, then run `python3 _build/build.py` |

## Forms
All forms post through FormSubmit's AJAX endpoint. The destination address is assembled at runtime in `assets/js/site.js` and never appears in page markup. The first submission triggers a one-time FormSubmit activation email that must be confirmed.

## Custom domain
To serve on be.solar:
1. Add a `CNAME` file containing `be.solar`.
2. Point the apex A records to GitHub Pages: 185.199.108.153, .109.153, .110.153 and .111.153.
3. Enable HTTPS in Settings → Pages.

## Trademark
Be.Solar is not affiliated with any company or mark named "BeSolar", "Be Solar" or similar. See `disclaimer.html`.

© 2026 Be.Solar / Webworks Media Network.
