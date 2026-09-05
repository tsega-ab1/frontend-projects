function renderResults(rooms) {
  const list = document.getElementById('results-list');
  document.getElementById('results-count').textContent = `${rooms.length} room${rooms.length === 1 ? '' : 's'} match your filters`;
  if (rooms.length === 0) {
    list.innerHTML = '<p style="color:var(--fog-dim); padding:30px 0;">No rooms match those filters. Try widening your price range.</p>';
    return;
  }
  list.innerHTML = rooms.map(r => `
    <article class="result-card">
      <div class="img-placeholder" style="--ratio:4/3" data-label="${r.img}"></div>
      <div class="result-card__body">
        <h3>${r.name}</h3>
        <p class="result-card__meta">${r.guests} Guests · ${r.size} m²</p>
        <div class="result-card__tags">
          ${r.tags.includes('wifi') ? '<span>Free Wi-Fi</span>' : ''}
          ${r.tags.includes('breakfast') ? '<span>Breakfast included</span>' : ''}
          ${r.tags.includes('parking') ? '<span>Free parking</span>' : ''}
        </div>
      </div>
      <div class="result-card__side">
        <p class="result-card__price">$${r.price} <span>/ night</span></p>
        <a href="room-detail.html">View room</a>
      </div>
    </article>
  `).join('');
}

function applyFilters() {
  const maxPrice = +document.getElementById('price-range').value;
  document.getElementById('price-out').textContent = maxPrice;
  const activeTypes = [...document.querySelectorAll('.type-filter:checked')].map(c => c.value);
  const activeAmenities = [...document.querySelectorAll('.amenity-filter:checked')].map(c => c.value);
  const sort = document.getElementById('sort-select').value;

  let filtered = ROOMS.filter(r =>
    r.price <= maxPrice &&
    activeTypes.includes(r.type) &&
    activeAmenities.every(a => r.tags.includes(a))
  );

  if (sort === 'price-asc') filtered.sort((a, b) => a.price - b.price);
  if (sort === 'price-desc') filtered.sort((a, b) => b.price - a.price);

  renderResults(filtered);
}

document.addEventListener('DOMContentLoaded', applyFilters);
