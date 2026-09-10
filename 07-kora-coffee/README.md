# KORA Coffee

A production-ready static site for KORA Coffee, a single-origin Ethiopian coffee brand. Three pages: `index.html` (home), `shop.html` (product grid), `product.html` (product detail).

## Design notes

- **Palette:** forest green `#1B3D2F`, coffee brown `#4E3427`, muted gold `#D4AF37`, cream `#F8F4E9`, terracotta `#C96B3D` — pulled from the brand's own color system.
- **Type:** Playfair Display (headlines) + Montserrat (body/UI), loaded from Google Fonts.
- **Layout idea:** an asymmetric split hero (angled image edge, echoing the brand's off-center monogram) instead of a centered hero; a horizontal "shelf" of featured coffees with staggered heights instead of a uniform card grid; a numbered process strip (justified, since brewing really is a sequence); alternating cream/forest section backgrounds for rhythm.
- All interactive elements have visible keyboard focus states, `prefers-reduced-motion` is respected, and the mobile nav collapses under 760px.

## What to swap before launch

- **Images** — every photo in `assets/images/` is a labeled placeholder. Replace with real photography at the same filenames to avoid touching the HTML:
  - `hero-coffee.jpg` — farmer with cherries, 4:5 crop
  - `origin-farm.jpg` — highland farm landscape, 4:3
  - `process-bean-cup.jpg` — currently unused on the homepage; wire in if you add a process gallery
  - `featured-bag.jpg` — reused packaging shot across all four product cards (each gets a CSS tint via `.tint-forest` / `.tint-terracotta` / `.tint-gold` classes — swap for real per-SKU photography and remove the tint classes once you have them)
  - `journal-1.jpg`, `journal-2.jpg` — journal post thumbnails
- **Copy** — product names, prices, tasting notes, testimonials, and stats (`120+ partner farms`, `18% above market`) are placeholder content written to match the brand brief. Replace with real figures.
- **Cart/checkout** — the "Add to cart" button and newsletter form are front-end only (no backend). Wire up to your commerce platform of choice (Shopify, Snipcart, a custom API, etc.) before launch.
- **Contact details** — email, phone, and address in the footer are placeholders.

## Structure

```
kora-coffee/
├── index.html
├── shop.html
├── product.html
├── css/style.css
├── js/main.js
├── assets/images/
└── README.md
```
