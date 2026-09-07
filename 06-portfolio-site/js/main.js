// Single deliberate motion moment: nav gains a hairline border once the page scrolls.
const nav = document.querySelector('.nav');
const onScroll = () => {
  if (window.scrollY > 8) {
    nav.style.borderBottom = '1px solid rgba(243,239,230,0.12)';
  } else {
    nav.style.borderBottom = '1px solid transparent';
  }
};
window.addEventListener('scroll', onScroll, { passive: true });
onScroll();
