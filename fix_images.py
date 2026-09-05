import re

replacements = {
    "02-hotel-luxury-boutique/index.html": [
        ('<div class="img-placeholder" style="--ratio:4/5" data-label="Hero: hotel exterior or lobby at golden hour, vertical crop"></div>',
         '<img src="assets/images/hero-exterior.jpg" alt="Hotel exterior at golden hour" style="aspect-ratio:4/5; object-fit:cover; width:100%;">'),
        ('<div class="img-placeholder" style="--ratio:4/3" data-label="Room interior — bed + window, natural light (single reused room photo)"></div>',
         '<img src="assets/images/room-generic.jpg" alt="Hotel room interior" style="aspect-ratio:4/3; object-fit:cover; width:100%;">'),
        ('<div class="img-placeholder" data-label="Interior/amenity detail — one representative interior shot (single reused detail photo)"></div>',
         '<img src="assets/images/interior-detail.jpg" alt="Hotel interior detail" style="object-fit:cover; width:100%; height:100%;">'),
        ('<div class="img-placeholder" style="--ratio:1/1" data-label="Interior/amenity detail — one representative interior shot (single reused detail photo)"></div>',
         '<img src="assets/images/interior-detail.jpg" alt="Hotel interior detail" style="aspect-ratio:1/1; object-fit:cover; width:100%;">'),
    ],
    "02-hotel-luxury-boutique/room-detail.html": [
        ('<div class="img-placeholder" style="--ratio:4/3" data-label="Room interior — bed + window, natural light (single reused room photo)"></div>',
         '<img src="assets/images/room-generic.jpg" alt="Hotel room interior" style="aspect-ratio:4/3; object-fit:cover; width:100%;">'),
        ('<div class="img-placeholder" style="--ratio:4/3" data-label="Interior/amenity detail — one representative interior shot (single reused detail photo)"></div>',
         '<img src="assets/images/interior-detail.jpg" alt="Hotel interior detail" style="aspect-ratio:4/3; object-fit:cover; width:100%;">'),
    ],
    "02-hotel-luxury-boutique/rooms.html": [
        ('<div class="img-placeholder" style="--ratio:4/3" data-label="Room interior — bed + window, natural light (single reused room photo)"></div>',
         '<img src="assets/images/room-generic.jpg" alt="Hotel room interior" style="aspect-ratio:4/3; object-fit:cover; width:100%;">'),
    ],
    "03-hotel-booking-platform/index.html": [
        ('<div class="img-placeholder" style="--ratio:4/5" data-label="Hero: hotel exterior or lobby at golden hour, vertical crop"></div>',
         '<img src="assets/images/hero-exterior.jpg" alt="Hotel exterior at golden hour" style="aspect-ratio:4/5; object-fit:cover; width:100%;">'),
        ('<div class="img-placeholder" style="--ratio:4/3" data-label="Room interior — bed + window, natural light (single reused room photo)"></div>',
         '<img src="assets/images/room-generic.jpg" alt="Hotel room interior" style="aspect-ratio:4/3; object-fit:cover; width:100%;">'),
        ('<div class="img-placeholder" data-label="Interior/amenity detail — one representative interior shot (single reused detail photo)"></div>',
         '<img src="assets/images/interior-detail.jpg" alt="Hotel interior detail" style="object-fit:cover; width:100%; height:100%;">'),
        ('<div class="img-placeholder" style="--ratio:1/1" data-label="Interior/amenity detail — one representative interior shot (single reused detail photo)"></div>',
         '<img src="assets/images/interior-detail.jpg" alt="Hotel interior detail" style="aspect-ratio:1/1; object-fit:cover; width:100%;">'),
    ],
    "03-hotel-booking-platform/room-detail.html": [
        ('<div class="img-placeholder" style="--ratio:4/3" data-label="Room interior — bed + window, natural light (single reused room photo)"></div>',
         '<img src="assets/images/room-generic.jpg" alt="Hotel room interior" style="aspect-ratio:4/3; object-fit:cover; width:100%;">'),
        ('<div class="img-placeholder" style="--ratio:4/3" data-label="Interior/amenity detail — one representative interior shot (single reused detail photo)"></div>',
         '<img src="assets/images/interior-detail.jpg" alt="Hotel interior detail" style="aspect-ratio:4/3; object-fit:cover; width:100%;">'),
    ],
    "04-hotel-admin-system/account.html": [
        ('<div class="img-placeholder" style="--ratio:1/1" data-label="Room interior — bed + window, natural light (single reused room photo)"></div>',
         '<img src="assets/images/room-generic.jpg" alt="Hotel room interior" style="aspect-ratio:1/1; object-fit:cover; width:100%;">'),
    ],
    "04-hotel-admin-system/index.html": [
        ('<div class="img-placeholder" style="--ratio:4/5" data-label="Hero: hotel exterior or lobby at golden hour, vertical crop"></div>',
         '<img src="assets/images/hero-exterior.jpg" alt="Hotel exterior at golden hour" style="aspect-ratio:4/5; object-fit:cover; width:100%;">'),
        ('<div class="img-placeholder" style="--ratio:4/3" data-label="Room interior — bed + window, natural light (single reused room photo)"></div>',
         '<img src="assets/images/room-generic.jpg" alt="Hotel room interior" style="aspect-ratio:4/3; object-fit:cover; width:100%;">'),
        ('<div class="img-placeholder" data-label="Interior/amenity detail — one representative interior shot (single reused detail photo)"></div>',
         '<img src="assets/images/interior-detail.jpg" alt="Hotel interior detail" style="object-fit:cover; width:100%; height:100%;">'),
        ('<div class="img-placeholder" style="--ratio:1/1" data-label="Interior/amenity detail — one representative interior shot (single reused detail photo)"></div>',
         '<img src="assets/images/interior-detail.jpg" alt="Hotel interior detail" style="aspect-ratio:1/1; object-fit:cover; width:100%;">'),
    ],
    "04-hotel-admin-system/room-detail.html": [
        ('<div class="img-placeholder" style="--ratio:4/3" data-label="Room interior — bed + window, natural light (single reused room photo)"></div>',
         '<img src="assets/images/room-generic.jpg" alt="Hotel room interior" style="aspect-ratio:4/3; object-fit:cover; width:100%;">'),
        ('<div class="img-placeholder" style="--ratio:4/3" data-label="Interior/amenity detail — one representative interior shot (single reused detail photo)"></div>',
         '<img src="assets/images/interior-detail.jpg" alt="Hotel interior detail" style="aspect-ratio:4/3; object-fit:cover; width:100%;">'),
    ],
    "05-cosmetics-corvina/index.html": [
        ('<div class="feature__img img-placeholder" style="--ratio:4/5" data-label="Product in hand or on skin, natural light, no heavy retouching"></div>',
         '<img class="feature__img" src="assets/images/hero-product.jpg" alt="Corvina product on skin" style="aspect-ratio:4/5; object-fit:cover; width:100%;">'),
        ('<div class="break__img img-placeholder" style="--ratio:3/4" data-label="Close-up of a raw ingredient — the plant or material central to the formula"></div>',
         '<img class="break__img" src="assets/images/ingredient-closeup.jpg" alt="Corvina key ingredient close-up" style="aspect-ratio:3/4; object-fit:cover; width:100%;">'),
    ],
    "05-cosmetics-corvina/product.html": [
        ('<div class="product-shot img-placeholder" style="--ratio:1/1" data-label="Calm Serum: product bottle, clean background, studio light"></div>',
         '<img class="product-shot" src="assets/images/product-bottle.jpg" alt="Corvina Calm Serum bottle" style="aspect-ratio:1/1; object-fit:cover; width:100%;">'),
    ],
}

for filepath, subs in replacements.items():
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    original = content
    for old, new in subs:
        count = content.count(old)
        content = content.replace(old, new)
        print(f"{filepath}: replaced {count}x -> {new[:60]}...")
    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

print("\nDone. Review with: git diff --stat")
