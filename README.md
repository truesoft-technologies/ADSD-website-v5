# ADSD Steel Technical Services Contracting L.L.C — website

Static, dependency-free-at-build site. 16 pages, no framework, no build step
required to deploy — upload the folder.

```
index.html                  single-page home (13 sections)
services/*.html             9 service pages
products/*.html             6 product pages
assets/css/main.css         design system + all section styles
assets/js/app.js            interaction layer
assets/js/hero-frame.js     Three.js hero (ES module)
assets/img/                 68 photographs (800w + 1400w) + logos + OG card
build.py                    content model + templates — the source of truth
sitemap.xml, robots.txt     generated
CONTENT-NOTES.md            what came from the PDF, what needs client sign-off
```

## Design system

The concept is **the shop drawing** — the client's own working vernacular.

- **Grid rails.** Fixed vertical hairlines at the container columns with
  circled grid marks (A / B / C), the way a structural drawing labels its
  column grid. They invert automatically over dark bands.
- **Dimension lines.** Section dividers are drafting dimension lines with
  extension ticks and a mono span label.
- **Red index blocks.** Each section is numbered in a red chip, echoing the red
  callout boxes in the printed profile.
- **Signature.** The hero is a procedural steel portal frame that *erects
  itself* in the real sequence a crew would follow: setting-out grid → columns
  and base plates → rafters and haunches → eave beams and ridge → purlins →
  bracing. Built as one `BufferGeometry` and revealed with `setDrawRange`.

### Tokens

| | |
|---|---|
| Ink | `#0B1014` `#111A20` `#1A252D` |
| Paper | `#F6F7F8` `#ECEFF1` `#FFFFFF` |
| Brand cyan | `#00A9E8` (sampled from the logo) |
| Cyan for text | `#0079AE` (darkened to clear AA) |
| Lime `#6CD800` | live-status marks only |
| Red `#D71F29` | section index chips only |

Type: **Archivo** for display (condensed heavy caps echo the logo's tagline
lockup), **Inter** for body, **IBM Plex Mono** for labels, data and drawing
annotations. Radii are 2–5 px throughout — engineered, not rounded.

## Libraries (all from CDN, all `defer`)

GSAP 3.12.5 + ScrollTrigger · Lenis 1.0.42 · SplitType 0.3.4 ·
Motion One 10.18 (magnetic-button springs) · Three.js 0.160 (ES module via
import map).

**Framer Motion was specified but this is vanilla HTML/JS, not React** — Motion
One is the same team's non-React library and does the same job.

## Animation inventory

Loading sequence with counter and curtain wipe · hero word-by-word split reveal ·
Three.js frame erection · scroll-triggered section reveals · staggered card
groups · animated statistics · clip-path image reveals · parallax on hero,
CTA and figure images · floating gradient glows · infinite client marquee ·
magnetic buttons · custom cursor (ring + dot, blend-difference) · service rows
with a cursor-following preview thumbnail · industry rows with hover image
reveal · process bars · table row cascade · accordion · lightbox with keyboard
nav · glassmorphic nav on scroll with hide-on-scroll-down.

## Performance & accessibility

- Every effect is gated behind `prefers-reduced-motion` **and** a
  `(hover: hover) and (pointer: fine)` check. Verified: with reduced motion the
  loader is removed, nothing stays hidden, cursor and preview are disabled.
- Three.js: quality tiers by viewport, `devicePixelRatio` capped, render loop
  gated on `IntersectionObserver` **and** `visibilitychange`, debounced resize.
- All images `loading="lazy"` + `decoding="async"` with explicit
  `width`/`height` and `srcset`/`sizes`. Hero banners use `fetchpriority="high"`.
- Semantic landmarks, skip link, visible focus rings, `aria-expanded` on the
  burger and accordion, `aria-current` section spy, labelled form fields with
  inline errors, keyboard-operable gallery and lightbox.
- **Verified 0 WCAG AA contrast failures** and **0 heading-order jumps** across
  desktop / tablet / mobile / 320 px. No horizontal overflow at any width.
- No `localStorage` / `sessionStorage` anywhere.

## SEO

Per-page `title`, `description`, canonical, Open Graph and Twitter cards.
JSON-LD: `Organization` + `LocalBusiness` + `GeneralContractor` with licence
identifiers, TRN and a nine-item `OfferCatalog` on the home page; `FAQPage`;
`Service` + `BreadcrumbList` on each service page; `Product` + `Offer` +
`BreadcrumbList` on each product page. Generated `sitemap.xml` and `robots.txt`.

## Before deploying

1. Set the real domain in `build.py` (`SITE = ...`) and run `python3 build.py`.
2. Read `CONTENT-NOTES.md` — the testimonials are invented and must be replaced
   or removed, and the vision statement needs sign-off.
3. Wire the contact form to a real endpoint (currently `mailto:`).
4. Serve over HTTPS with long `Cache-Control` on `/assets/` and Brotli on
   HTML/CSS/JS.
