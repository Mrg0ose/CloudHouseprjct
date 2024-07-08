var swiper = new Swiper(".mySwiper", {
      spaceBetween: 30,
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
      mousewheel: true,
      keyboard: true,
       autoplay: {
    delay: 4000,
    disableOnInteraction: false,
  },
  loop: true,
    });