# ADSD Steel — content provenance & replacement notes

Everything below is split into **verbatim from the company profile PDF** and
**written for the build**. Anything in the second list should be reviewed by
ADSD before the site goes live.

---

## 1. Taken directly from the PDF (do not change without checking)

| Item | Source |
|---|---|
| Company name, `ADSD Steel Technical Services Contracting L.L.C` | Dubai licence, p.13 |
| Phone `+971 56 996 8611` | Page footer, all 13 pages |
| Email `ads.techdxb@gmail.com` | Page footer, all 13 pages |
| `P.O. Box 282615, Dubai, UAE` | Page footer, all 13 pages |
| `TRN 104023207400003` | Page footer, all 13 pages |
| Dubai licence no. `1050680`, Dept. of Economy & Tourism, issued 31/03/2022, "Technical Services Works", Active | p.13 |
| Sharjah industrial licence no. `502971`, issued 25-10-1999 (Al Dhabi Steel L.L.C) | p.12 |
| The nine service names | p.1 and p.2 |
| Mission statement wording (Supply Service page + About) | p.2, verbatim |
| Building-maintenance wording ("without outsourcing or sub contracting") | p.2, verbatim |
| "Extensive experience in the industry has been fundamental…" | p.1, verbatim |
| All 10 reference projects, contractors and clients | p.5 table |
| All 34 photographs | pp.1–2 and 7–11, cropped from the page rasters |
| Brand colours — cyan `#00A9E8`, lime `#6CD800`, red `#D71F29`, navy `#1F4E9C` | pixel-sampled from the logo and callout boxes |
| Logo | rebuilt from the page header as transparent PNGs |

**Deliberately excluded:** page 12 of the PDF lists the partners' passport /
Emirates ID numbers. These were **not** used anywhere on the site. Only the
company licence numbers and TRN — which already appear on ADSD's own
letterhead footer — have been published.

---

## 2. Written for the build — please review

### Needs ADSD sign-off
1. **Vision statement** (`index.html`, About section) — the PDF contains a
   mission but no vision. Placeholder written to match the mission's tone.
2. **Three testimonials** (`index.html`, "What site teams say") — **invented**.
   Attributions are deliberately generic ("Project Manager, main contractor,
   Abu Dhabi") and the section states that named references are supplied with
   quotations. **Replace with real quotes or delete the section.**
3. **Service and product body copy** — the PDF gives only a one-line name for
   each service. All descriptions, feature lists, benefits and specification
   tables are industry-standard copy written to be accurate for a UAE steel
   fabricator. Check for anything ADSD does *not* actually offer, in particular:
   - stainless-steel pipe spooling
   - intumescent coating (listed as "through applicators")
   - standing-seam roofing
   - PIR / PUR / EPS / mineral-wool panel cores
   - spring hangers
4. **Six product families** — the PDF names no products. These were derived
   from the gallery photography and the "Miscellaneous Metal Work" line.
   Confirm the range, then confirm sizes/grades in each spec table.
5. **Six industries** — inferred from the project list (SEWA → utilities,
   Khalid Port → ports, CMW → cement, ICAD/Kizad → manufacturing).
6. **Five-step process** — a reasonable fabricator's sequence, not documented
   in the PDF. Confirm it matches how ADSD actually works.
7. **FAQ answers** — grounded in PDF facts but the wording is ours.
8. **Project statuses** — the PDF marks project 10 as "Not Yet started"; the
   other nine are shown as *Completed*, which the PDF does not state
   explicitly. Confirm or change in `build.py` → `PROJECTS`.

### Placeholder / configuration
9. **Domain** — `SITE = 'https://www.adsdsteel.ae'` in `build.py` is a guess.
   Set the real domain and rebuild; it feeds all canonical URLs, Open Graph
   tags, `sitemap.xml` and `robots.txt`.
10. **Contact form has no backend.** It validates client-side and then opens
    the visitor's mail client via `mailto:`. For a real submission pipeline,
    point the form at Formspree / Web3Forms / an ERPNext webhook and remove the
    `mailto:` fallback in `assets/js/app.js` → `initForm()`.
11. **Favicon** is the logo PNG. A proper `.ico` / 512 px maskable PNG set
    would be better.
12. **No social profiles** were in the PDF, so the footer has no social links.
13. **`sameAs` in the Organization schema is absent** — add social/Google
    Business Profile URLs when available; it materially helps local SEO.

### Photography that should be re-shot
The PDF is rasterised, so every photo was recovered by cropping page images.
They are usable but not high-resolution. Priority replacements:

| Where used | Why |
|---|---|
| `fabrication-welding`, `steel-cutting`, `supply-team` | These are **stock photos** in the original PDF, not ADSD's own work. Replace with real workshop photography. |
| `building-maintenance` | Stock, and the crop still carries a red text panel from the PDF layout. **Replace first.** |
| All gallery images | Genuine ADSD project photos, but only ~475 px in the source. Ask for the originals. |
| Handrails / balustrades product page | No true handrail photo exists in the PDF — platform steel is standing in. |
| `og-cover.jpg` | Generated from a project photo. A designed 1200×630 card would be better. |

---

## 3. Rebuilding

All content lives in `build.py` as plain Python dictionaries — `SERVICES`,
`PRODUCTS`, `PROJECTS`, `INDUSTRIES`, `PROCESS`, `WHY`, `FAQ`, `CLIENTS`.
Edit those, then:

```bash
python3 build.py
```

This regenerates all 16 HTML pages, `sitemap.xml` and `robots.txt`. Never edit
the generated HTML directly — it will be overwritten.
