function detectMiniMob() {
  return ( ( window.innerWidth <= 768 ));
}

$(document).ready(function(e){

  $('.header__burger').click(function(event){
    $('.header__burger,.burger_menu').toggleClass('active')
  })

  
  $('.pop_up_click').click(function(event) {
    $('.pop-up_block').toggleClass('active');
  });

  // $('.dropbtn').click(function(event) {
  //   event.preventDefault()
  //   $(this).parent().find('.dropdown-contentt').toggleClass('active');
  // });

  if(detectMiniMob()){
    
    
  }
  $('.header__burger').click(function(event) {
    $('.dropdown-menu').removeClass('show')
  });
  

  $('.certificate_main').click(function(event) {
    $('.certificate_main').removeClass('active')
    $(this).toggleClass('active');
  });

  $("[name=user_phone]").inputmask({"mask": "+7(999) 999-99-99"});

  // $('.brand_item ').click(function(event) {
  //   $(this).toggleClass('active');
  // });

  $('.image-popup-vertical-fit').magnificPopup({
		type: 'image',
		closeOnContentClick: true,
		mainClass: 'mfp-img-mobile',
		image: {
			verticalFit: true
		}
		
	});

	$('.image-popup-fit-width').magnificPopup({
		type: 'image',
		closeOnContentClick: true,
		image: {
			verticalFit: false
		}
	});

	$('.image-popup-no-margins').magnificPopup({
		type: 'image',
		closeOnContentClick: true,
		closeBtnInside: false,
		fixedContentPos: true,
		mainClass: 'mfp-no-margins mfp-with-zoom', // class to remove default margin from left and right side
		image: {
			verticalFit: true
		},
		zoom: {
			enabled: true,
			duration: 300 // don't foget to change the duration also in CSS
		}
	});

  lightGallery(document.getElementById('lightgallery'), {
    plugins: [lgZoom, lgThumbnail],
    licenseKey: 'your_license_key',
    speed: 500,
    // ... other settings
  });

  lightGallery(document.getElementById('lightgallery2'), {
    plugins: [lgZoom, lgThumbnail],
    licenseKey: 'your_license_key',
    speed: 500,
    // ... other settings
  });

 
});

new Swiper('.gallery_slider', {
    // Optional parameters
    direction: 'horizontal',
    loop: true,
    slidesPerView: 2,
    // If we need pagination
    pagination: {
      el: false,
    },
  
    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
    breakpoints:{
        320: {
            slidesPerView: 1,
            spaceBetween: 20
          },
          // when window width is >= 480px
          480: {
            slidesPerView: 1,
            spaceBetween: 30
          },
          // when window width is >= 640px
          640: {
            slidesPerView: 1.4,
            spaceBetween: 25,
            centeredSlides:true,
          },
          // when window width is >= 640px
          1200: {
            slidesPerView: 2.1,
            spaceBetween: 25,
            centeredSlides:true,
          }
    },
    // And if we need scrollbar
    scrollbar: {
      el: false,
    },
});


new Swiper('.work_slider', {
  // Optional parameters
  direction: 'horizontal',
  loop: true,
  slidesPerView: 2,
  // If we need pagination
  pagination: {
    el: false,
  },

  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  breakpoints:{
      320: {
          slidesPerView: 1,
          spaceBetween: 20
        },
        // when window width is >= 480px
        480: {
          slidesPerView: 1,
          spaceBetween: 30
        },
        // when window width is >= 640px
        640: {
          slidesPerView: 3,
          spaceBetween: 25,
       
        },
        // when window width is >= 640px
        1200: {
          slidesPerView: 4,
          spaceBetween: 25,

        }
  },
  // And if we need scrollbar
  scrollbar: {
    el: false,
  },
});

new Swiper('.worker_slider', {
  // Optional parameters
  direction: 'horizontal',
  loop: true,
  slidesPerView: 2,
  // If we need pagination
  pagination: {
    el: false,
  },

  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  breakpoints:{
    320: {
        slidesPerView: 1,
        spaceBetween: 20
      },
      768: {
        slidesPerView: 2,
        spaceBetween: 25,
      },
      // when window width is >= 640px
      1200: {
        slidesPerView: 2,
        spaceBetween: 25,
      }
},
  // And if we need scrollbar
  scrollbar: {
    el: false,
  },
});

const commentsSlider = new Swiper('.comment_slider', {
  // Optional parameters
  direction: 'horizontal',
  loop: true,
  slidesPerView: 2,
  // If we need pagination
  pagination: {
    el: false,
  },

  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  breakpoints:{
    320: {
        slidesPerView: 1,
        spaceBetween: 20
      },
      768: {
        slidesPerView: 1,
        spaceBetween: 25,
      },
      // when window width is >= 640px
      992: {
        slidesPerView: 2,
        spaceBetween: 25,
      }
  },
  // And if we need scrollbar
  scrollbar: {
    el: false,
  },
  on: {
    reachEnd: function () {

      let nextTabLink = $('.clients .nav-link.active').data('nextlink')
      let nextTabBody = $('.clients .nav-link.active').data('nexttab')

      // clear all comment tabs
      $('.clients .nav-link').removeClass('active');
      // clear all comment tab bodies
      $('.clients .tab-pane').removeClass('active').removeClass('show');

      $("#" + nextTabLink).addClass('active');
      $("#" + nextTabBody).addClass('active show');
      commentsSlider.slideTo(0, 300, true)
    },
  }

  
 
});

function detectMob() {
  return ( ( window.innerWidth <= 993 ));
}


function removeYmap(){
  if( detectMob()){
    $('#ymapp').remove()
  }
}


removeYmap()