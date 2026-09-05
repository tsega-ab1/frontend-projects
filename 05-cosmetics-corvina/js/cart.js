function getCart() {
  try { return JSON.parse(localStorage.getItem('corvina-cart')) || []; }
  catch { return []; }
}
function saveCart(cart) {
  localStorage.setItem('corvina-cart', JSON.stringify(cart));
  updateBadge();
}
function updateBadge() {
  const badge = document.getElementById('cart-badge');
  if (!badge) return;
  const count = getCart().reduce((sum, i) => sum + i.qty, 0);
  badge.textContent = count;
}
function addItemToCart(item) {
  const cart = getCart();
  const existing = cart.find(i => i.name === item.name && i.size === item.size);
  if (existing) existing.qty += item.qty;
  else cart.push(item);
  saveCart(cart);
  const btn = document.querySelector('.add-to-bag');
  if (btn) {
    const original = btn.textContent;
    btn.textContent = 'Added ✓';
    setTimeout(() => { btn.textContent = original; }, 1200);
  }
}
document.addEventListener('DOMContentLoaded', updateBadge);
