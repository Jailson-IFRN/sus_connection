var swiperOptions = {
    spaceBetween: 30,
    loop: true,
    loopFillGroupWithBlank: true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  };
  
  // Verifique o tamanho da tela e ajuste slidesPerView com base no tamanho da tela
  if (window.innerWidth >= 780) {
    swiperOptions.slidesPerView = 3;
    swiperOptions.slidesPerGroup = 3;
  } else if (window.innerWidth >= 768) {
    swiperOptions.slidesPerView = 2;
    swiperOptions.slidesPerGroup = 2;
  } else {
    swiperOptions.slidesPerView = 1;
    swiperOptions.slidesPerGroup = 1;
  }
  
  var swiper = new Swiper(".slide-content", swiperOptions);
  
  // Atualize o Swiper quando a tela for redimensionada
  window.addEventListener("resize", function () {
    // Verifique novamente o tamanho da tela e ajuste slidesPerView com base no tamanho da tela
    if (window.innerWidth >= 780) {
      swiper.params.slidesPerView = 3;
      swiper.params.slidesPerGroup = 3;
    } else if (window.innerWidth >= 450) {
      swiper.params.slidesPerView = 2;
      swiper.params.slidesPerGroup = 2;
    } else {
      swiper.params.slidesPerView = 1;
      swiper.params.slidesPerGroup = 1;
    }
  
    // Atualize o Swiper
    swiper.update();
  });
  