const nav = document.querySelector('.nav');
if (nav) {
  const onScroll = () => {
    nav.style.borderBottom = window.scrollY > 8 ? '1px solid rgba(28,35,33,0.12)' : '1px solid transparent';
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}
