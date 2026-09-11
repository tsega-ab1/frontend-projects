# ZURIA — Ethiopian Couture (Habesha Kemis Boutique)

A six-page static site for a handwoven habesha kemis boutique: `index.html` (home), `shop.html`, `product.html`, `our-craft.html`, `custom-order.html`, `contact.html`.

## Design notes

- **Palette:** raw cotton ivory `#F8F3EA`, deep wine maroon `#6B1F2A`, metallic gold `#B8912E`, forest green `#34483A`, near-black charcoal `#241D18` — drawn from traditional tilet (woven border) coloring.
- **Type:** Cormorant Garamond (headings — bridal/couture editorial serif) + Jost (body/UI — clean geometric sans), both from Google Fonts.
- **Layout:** a full-bleed portrait hero since the garment itself is the product; a horizontal "collections" rail instead of a square grid; a pure-CSS woven-border divider (`.tilet-rule`) that needs no source image; and a craft/heritage section that treats the weaving process as a real, numbered sequence.

## No placeholder images included

Per your request, this build does **not** include placeholder photography — every `<img>` tag already points to the correct filename and folder (`assets/images/`), so once you generate or shoot the real photos, dropping them in with these exact names is all that's needed. No HTML or CSS changes required.

### Image prompts (for ChatGPT's image tool or similar)

Generate one at a time. Each is written to match the brand palette and avoid text/logos baked into the image.

**1. `hero-model.jpg`** — homepage hero, portrait 4:5
```
An elegant editorial fashion photograph of a woman wearing a handwoven ivory Ethiopian habesha kemis with an intricate gold and maroon tilet border, standing in soft natural light against a warm neutral studio or outdoor backdrop. Premium bridal-editorial photography style, graceful pose, fabric detail clearly visible. Vertical 4:5 portrait crop, no visible logos or text, no other people.
```

**2. `collection-wedding.jpg`** — bridal collection card, portrait 3:4
```
An editorial fashion photograph of a bride wearing a fully embroidered ivory habesha kemis with a wide gold tilet border, veil optional, soft romantic natural light, neutral or softly blurred background. Premium bridal photography style, fabric and embroidery detail in sharp focus. Vertical 3:4 crop, no visible text or logos.
```

**3. `collection-holiday.jpg`** — holiday collection card, portrait 3:4
```
An editorial fashion photograph of a woman wearing a colorful habesha kemis in deep maroon and gold, styled for an Ethiopian holiday celebration (Meskel or Timkat), warm afternoon light, outdoor or festive setting softly blurred in the background. Premium fashion-editorial style, not touristic or staged-looking. Vertical 3:4 crop, no text or logos.
```

**4. `collection-modern.jpg`** — modern fusion collection card, portrait 3:4
```
An editorial fashion photograph of a woman wearing a modern fusion dress that reinterprets the habesha kemis silhouette with a narrow gold tilet accent trim, contemporary tailored cut, clean minimal background, soft studio lighting. Premium modern-boutique fashion photography. Vertical 3:4 crop, no text or logos.
```

**5. `collection-netela.jpg`** — accessories collection card, portrait 3:4 or square
```
A clean product photograph of a folded Ethiopian netela (shawl) with a woven gold and maroon tilet border, laid on a neutral linen surface with soft natural side light, minimal styling. Premium product photography, not a lifestyle shot. Vertical 3:4 or square crop, no text or logos.
```

**6. `craft-weaving.jpg`** — craft/heritage section, landscape 4:3
```
A documentary-style editorial photograph of an artisan's hands weaving a colorful tilet pattern on a traditional Ethiopian wooden shuttle loom, threads in gold, maroon and green visible, warm workshop lighting, shallow depth of field. Premium craft-documentary photography style, not staged or overly polished. Horizontal 4:3 crop, no visible text, no clearly visible faces required.
```

**7. `craft-detail.jpg`** — weaving pattern macro, square 1:1 (used twice: Our Craft page and product gallery thumbnail)
```
An extreme close-up macro photograph of a hand-woven Ethiopian tilet pattern — geometric gold, maroon and forest green threads interlocking on raw cotton fabric — filling the entire frame, soft natural light showing thread texture. Premium textile-editorial photography. Square 1:1 crop, no text or logos.
```

**8. `lookbook-1.jpg`** — lookbook editorial, portrait/tall (roughly 3:4)
```
A candid editorial lifestyle photograph of a woman wearing a habesha kemis during a traditional Ethiopian coffee ceremony, seated on a low stool, incense smoke softly visible, warm indoor light, shallow depth of field. Premium lifestyle-editorial photography, warm and authentic rather than posed. Vertical crop close to 3:4, no text or logos, face can be partially turned away.
```

**9. `lookbook-2.jpg`** — lookbook editorial, landscape/wide (roughly 4:3)
```
A close-up editorial styling photograph showing the neckline and shoulder detail of a habesha kemis paired with traditional Ethiopian gold jewelry, soft window light, warm neutral tones. Premium fashion-editorial detail shot. Horizontal crop close to 4:3, no visible face required, no text or logos.
```

**10. `custom-order-hero.jpg`** — Custom Order page hero, landscape 4:3
```
An editorial photograph of a tailor measuring ivory habesha kemis fabric with a measuring tape on a wooden work table, spools of gold and maroon thread nearby, warm natural workshop light. Premium bespoke-tailoring editorial photography. Horizontal 4:3 crop, no text or logos, face not required to be visible.
```

**11. `storefront.jpg`** — Contact page, landscape 4:3
```
An editorial photograph of a small boutique storefront exterior in Addis Ababa with a simple elegant sign, warm late-afternoon light, a few habesha kemis pieces visible through the window display. Premium boutique-editorial photography, clean and inviting, not touristic. Horizontal 4:3 crop, no readable text or logos on the sign itself (leave signage blank or blurred).
```

**12. `product-alt-1.jpg`** — product detail secondary thumbnail, square 1:1
```
An editorial fashion photograph showing the back view of an ivory habesha kemis with gold tilet border detail, worn, soft studio lighting, neutral background. Premium bridal-editorial photography, consistent with a matching front-view shot. Square 1:1 crop, no text or logos.
```

### Tips

- If a result comes back with text, signage, or a logo baked in, add `"absolutely no text, no signage, no logos anywhere in the image"` to the end of the prompt and regenerate.
- Keep the color instructions (ivory, maroon, gold, forest green) in every prompt so the photos feel like one cohesive shoot rather than 12 unrelated images.
- Once downloaded, rename each to the exact filename above and drop it into `assets/images/` — no code changes needed.

## What else to update before launch

- Phone, email, and address (`+251 91 123 4567`, `hello@zuria.example`, Bole Road) are placeholders.
- Prices on `shop.html` and `product.html` are placeholder figures.
- All forms (newsletter, custom order, contact) are front-end only — wire them to your email service or booking system.

## Structure

```
zuria-couture/
├── index.html
├── shop.html
├── product.html
├── our-craft.html
├── custom-order.html
├── contact.html
├── css/style.css
├── js/main.js
├── assets/images/   (empty — see image prompts above)
└── README.md
```
