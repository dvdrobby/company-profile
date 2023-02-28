const humberger = document.querySelector("#humberger");
const navbar = document.querySelector("#navbar");

window.onscroll = () => {
  const header = document.querySelector("header");
  const nav = header.offsetTop;

  if (window.pageYOffset > nav) {
    header.classList.add("nav-fixed");
  } else {
    header.classList.remove("nav-fixed");
  }
};

humberger.addEventListener("click", () => {
  humberger.classList.toggle("active");
  navbar.classList.toggle("hidden");
});

var swiper = new Swiper(".mySwiper", {
  slidesPerView: 3,
  spaceBetween: 30,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
});
