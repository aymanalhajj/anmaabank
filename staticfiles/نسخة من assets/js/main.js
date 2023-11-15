/**
 * Template Name: بنك الإنماء - v1.7.0
 * Template URL: https://ibrahim shaher/بنك الإنماء-bootstrap-startup-template/
 * Author: ibrahim shaher
 * License: https://ibrahim shaher/license/
 */


const sliderservicesmobile = () => {
  var servicessection = document.getElementsByClassName("slider-services-js");

  var win = window,
    doc = document,
    docElem = doc.documentElement,
    body = doc.getElementsByTagName('body')[0],
    x = win.innerWidth || docElem.clientWidth || body.clientWidth,
    y = win.innerHeight || docElem.clientHeight || body.clientHeight;
  // alert(x + ' × ' + y);

  // if (!section) return;
  if (
    $(window).width() < 700
  ) {

    Array.prototype.forEach.call(servicessection, function (element) {
      // servicessection.forEach((navbarlink) => {
      // if (!element.hash) return;
      // let section = select(navbarlink.hash);
      // if (!section) return;
      element.classList.add("slider-services-mobile");
      element.classList.remove("slider-services");
      element.classList.remove("swiper-pointer-events");
      element.classList.remove("swiper-backface-hidden");


      // if (element.classList.contains("slider-services") == true) {

      // } else {



      // }

    });
  } else {
    Array.prototype.forEach.call(servicessection, function (element) {
      // servicessection.forEach((navbarlink) => {
      // if (!element.hash) return;
      // let section = select(navbarlink.hash);
      // if (!section) return;
      element.classList.add("slider-services");
      element.classList.remove("slider-services-mobile");
      // if (element.classList.contains("slider-services") == true) {
      element.classList.add("swiper-pointer-events");
      element.classList.add("swiper-backface-hidden");
      // } else {



      // }

    });
    // navbarlink.classList.remove("slider-services-mobile");
    // navbarlink.classList.add("slider-services");
  }

  new Swiper(".slider-services", {
    speed: 500,
    autoplay: {
      delay: 5000,
      // disableOnInteraction: false,
      // reverseDirection: true,

    },

    spaceBetween: 5,

    // effect: "coverflow",
    // "space-between": 0,
    grabCursor: false,
    centeredSlides: true,
    coverflowEffect: {
      rotate: 0,
      depth: 500,
      modifier: 1,
      slideShadows: true
    },
    // "slides-per-view": "auto",
    // slidesPerView: "auto",
    slidesPerView: "2",

    navigation: {
      prevEl: ".services-prev",
      nextEl: ".services-next"
    },
    loop: true,
    pagination: {
      el: ".services-pagination",
      type: "bullets",
      clickable: true,
    },
    breakpoints: {
      // 600: {
      //   slidesPerView: 3,
      //   spaceBetween: 0,
      // },
      // 800: {
      //   slidesPerView: 3,
      //   spaceBetween: 0,

      // },
      // 1200: {
      //   slidesPerView: 3,
      //   spaceBetween: 0,

      // },
      320: {
        slidesPerView: 3,
        spaceBetween: 40,
      },
      // 480: {
      //   slidesPerView: 2,
      //   spaceBetween: 40,
      // },
      // 640: {
      //   slidesPerView: 3,
      //   spaceBetween: 40,
      // },
      992: {
        slidesPerView: 3,
        spaceBetween: 40,
      },
    },
  });
  new Swiper(".coins-slider", {
    speed: 5000,
    loop: true,

    keyboard: {
      enabled: true,
    },

    autoplay: {
      delay: 5000,
      disableOnInteraction: false,
      // delay: 0,
      // disableOnInteraction: true,
      //waitForTransition: false,
      reverseDirection: true,
    },
    // slidesPerView: "auto",
    // reverseDirection: true,
    // direction: 'V',
    slidesPerView: "3",
    direction: "vertical",
    spaceBetween: 0,
    freeMode: true,
    freeModeMomentum: false,
    freeModeMomentumBounce: false,
    // speed: 5000,
    // slidesPerView: "auto",
    // spaceBetween: 30,
    // pagination: {
    //   el: ".swiper-pagination",
    //   type: "bullets",
    //   clickable: true,
    // },

    // clickable: true,
    // },
    navigation: {
      nextEl: '.swiper-slide-next',
      prevEl: '.swiper-slide-prev ',
    },
    // breakpoints: {
    //   320: {
    //     slidesPerView: 2,
    //     spaceBetween: 40,
    //   },
    //   480: {
    //     slidesPerView: 3,
    //     spaceBetween: 40,
    //   },
    //   640: {
    //     slidesPerView: 4,
    //     spaceBetween: 40,
    //   },
    //   992: {
    //     slidesPerView: 6,
    //     spaceBetween: 40,
    //   },
    // },
  });
  new Swiper(".coins-city-slider", {
    speed: 5000,
    loop: true,

    keyboard: {
      enabled: true,
    },

    autoplay: {
      delay: 5000,
      disableOnInteraction: false,
      // delay: 0,
      // disableOnInteraction: true,
      //waitForTransition: false,
      reverseDirection: true,
    },
    // slidesPerView: "auto",
    // reverseDirection: true,
    // direction: 'V',
    slidesPerView: "3",
    direction: "horizontal",
    spaceBetween: 0,
    freeMode: true,
    freeModeMomentum: false,
    freeModeMomentumBounce: false,
    // freeMode: true,
    // freeModeMomentum: false,
    // freeModeMomentumBounce: false,
    // speed: 5000,
    // slidesPerView: "auto",
    // spaceBetween: 30,
    // pagination: {
    //   el: ".swiper-pagination",
    //   type: "bullets",
    //   clickable: true,
    // },

    // clickable: true,
    // },
    navigation: {
      nextEl: '.swiper-slide-duplicate-next',
      prevEl: '.swiper-slide-duplicate-prev ',
    },
    // breakpoints: {
    //   320: {
    //     slidesPerView: 2,
    //     spaceBetween: 40,
    //   },
    //   480: {
    //     slidesPerView: 3,
    //     spaceBetween: 40,
    //   },
    //   640: {
    //     slidesPerView: 4,
    //     spaceBetween: 40,
    //   },
    //   992: {
    //     slidesPerView: 6,
    //     spaceBetween: 40,
    //   },
    // },
  });
  new Swiper(".slider-services-mobile", {
    speed: 600,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false,
      reverseDirection: true,

    },

    spaceBetween: 100,

    // effect: "coverflow",
    // "space-between": 0,
    // grabCursor: false,
    centeredSlides: false,
    // coverflowEffect: {
    //   rotate: 0,
    //   depth: 500,
    //   modifier: 1,
    //   slideShadows: true
    // },
    // "slides-per-view": "auto",
    slidesPerView: "auto",

    navigation: {
      prevEl: ".services-prev",
      nextEl: ".services-next"
    },
    loop: true,
    pagination: {
      el: ".services-pagination",
      type: "bullets",
      clickable: true,
    },
    breakpoints: {

      1000: {
        slidesPerView: 1,
        spaceBetween: 100,
      },

      // 1200: {
      //   slidesPerView: 1,
      // },
    },
  });
};

sliderservicesmobile();

(function () {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {

    el = el.trim();
    if (all) {
      return [...document.querySelectorAll(el)];
    } else {
      return document.querySelector(el);
    }
  };

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    if (all) {
      select(el, all).forEach((e) => e.addEventListener(type, listener));
    } else {
      select(el, all).addEventListener(type, listener);
    }
  };

  /**
   * Easy on scroll event listener
   */
  const onscroll = (el, listener) => {
    el.addEventListener("scroll", listener);
  };

  /**
   * Navbar links active state on scroll
   */


  let navbarlinks = select("#navbar .scrollto", true);
  const navbarlinksActive = () => {
    let position = window.scrollY + 200;
    navbarlinks.forEach((navbarlink) => {
      if (!navbarlink.hash) return;
      let section = select(navbarlink.hash);
      if (!section) return;
      if (
        position >= section.offsetTop &&
        position <= section.offsetTop + section.offsetHeight
      ) {
        navbarlink.classList.add("active");
      } else {
        navbarlink.classList.remove("active");
      }
    });
  };
  window.addEventListener("load", navbarlinksActive);
  onscroll(document, navbarlinksActive);

  /**
   * Scrolls to an element with header offset
   */
  const scrollto = (el) => {
    let header = select("#header");
    let offset = header.offsetHeight;

    if (!header.classList.contains("header-scrolled")) {
      offset -= 10;
    }

    let elementPos = select(el).offsetTop;
    window.scrollTo({
      top: elementPos - offset,
      behavior: "smooth",
    });
  };

  /**
   * Toggle .header-scrolled class to #header when page is scrolled
   */
  let selectHeader = select("#header");
  if (selectHeader) {
    const headerScrolled = () => {
      if (window.scrollY > 100) {
        selectHeader.classList.add("header-scrolled");
      } else {
        selectHeader.classList.remove("header-scrolled");
      }
    };
    window.addEventListener("load", headerScrolled);
    onscroll(document, headerScrolled);
  }
  var navitemmobile = document.getElementsByClassName("nav-item-mobile");

  Array.prototype.forEach.call(navitemmobile, function (element) {
    // element.classList.remove("show");
    element.style.display = "none";

    // element.setAttribute("style", "{display : none !important;}");
  });
  /**
   * Back to top button
   */
  let backtotop = select(".back-to-top");
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add("active");
      } else {
        backtotop.classList.remove("active");
      }
    };
    window.addEventListener("load", toggleBacktotop);
    onscroll(document, toggleBacktotop);
  }

  /**
   * Mobile nav toggle
   */
  on("click", ".mobile-nav-toggle", function (e) {



    select("#navbar").classList.toggle("navbar-mobile");
    var els = document.getElementsByClassName("sub-sub-header-container");

    console.log(select(".mobile-menu-close").classList.contains("show"))
    if (select(".mobile-menu-close").classList.contains("show") == true) {
      var open = document.getElementsByClassName("mobile-menu-open");
      var close = document.getElementsByClassName("mobile-menu-close");
      Array.prototype.forEach.call(open, function (element) {
        // element.classList.remove("show");
        element.classList.add("show");
      });
      Array.prototype.forEach.call(close, function (element) {
        element.classList.remove("show");
        // element.classList.add("show");
      });
      // remove_item_navbar("open-account-navbar")
      // remove_item_navbar("news-navbar")
      // remove_item_navbar("events-navbar")
      // remove_item_navbar("blog-navbar")
      // remove_item_navbar("jop-navbar")
      var navitemmobile = document.getElementsByClassName("nav-item-mobile");

      Array.prototype.forEach.call(navitemmobile, function (element) {
        // element.classList.remove("show");
        element.style.display = "none";

        // element.setAttribute("style", "{display : none  !important;}");
      });
    }
    else {

      var open = document.getElementsByClassName("mobile-menu-open");
      var close = document.getElementsByClassName("mobile-menu-close");
      Array.prototype.forEach.call(close, function (element) {
        // element.classList.remove("show");
        element.classList.add("show");
      });
      Array.prototype.forEach.call(open, function (element) {
        element.classList.remove("show");
        // element.classList.add("show");
      });

      var navitemmobile = document.getElementsByClassName("nav-item-mobile");
      Array.prototype.forEach.call(navitemmobile, function (element) {
        // element.classList.remove("show");
        // element.classList.("style", "{display :'' !important;}");
        element.style.display = "";
      });
      // add_item_navbar("طلب تمويل", "/open-account", "open-account-navbar")
      // add_item_navbar("اخبار البنك", "/news", "news-navbar")
      // add_item_navbar("الفعاليات", "/events", "events-navbar")
      // add_item_navbar("المدونة", "/blogs", "blog-navbar")
      // add_item_navbar("الوظائف", "/jop", "jop-navbar")
    }
    Array.prototype.forEach.call(els, function (element) {
      element.classList.remove("row");
      element.classList.remove("gy-3");
    });

    // add_item("طلب تمويل", "#")

    // this.classList.toggle("bi-list");
    // this.classList.toggle("bi-x");
  });

  /**
   * Mobile nav dropdowns activate
   */
  on(
    "click",
    ".navbar .dropdown > a",
    function (e) {
      if (select("#navbar").classList.contains("navbar-mobile")) {
        var open = document.getElementsByClassName("mobile-menu-open");
        var close = document.getElementsByClassName("mobile-menu-close");
        Array.prototype.forEach.call(open, function (element) {
          // element.classList.remove("show");
          element.classList.add("show");
        });
        Array.prototype.forEach.call(close, function (element) {
          element.classList.remove("show");
          // element.classList.add("show");
        });
        e.preventDefault();
        this.nextElementSibling.classList.toggle("dropdown-active");
      }
    },
    true
  );

  /**
   * Scrool with ofset on links with a class name .scrollto
   */
  on(
    "click",
    ".scrollto",
    function (e) {
      if (select(this.hash)) {
        e.preventDefault();
        sliderservicesmobile();

        let navbar = select("#navbar");
        if (navbar.classList.contains("navbar-mobile")) {
          var els = document.getElementsByClassName("sub-sub-header-container");


          Array.prototype.forEach.call(els, function (element) {
            element.classList.add("row");
            element.classList.add("gy-3");
          });

          navbar.classList.remove("navbar-mobile");
          let navbarToggle = select(".mobile-nav-toggle");
          navbarToggle.classList.toggle("bi-list");
          navbarToggle.classList.toggle("bi-x");
        }
        scrollto(this.hash);
      }
    },
    true
  );

  /**
   * Scroll with ofset on page load with hash links in the url
   */
  window.addEventListener("load", () => {
    if (window.location.hash) {
      if (select(window.location.hash)) {
        scrollto(window.location.hash);
      }
    }
  });

  /**
   * Clients Slider
   */
  /**
   * Clients Slider
   */
  // new Swiper(".clients-slider", {
  //   speed: 200,

  //   loop: true,
  //   autoplay: {
  //     delay: 2000,
  //     disableOnInteraction: true,
  //     // delay: 0,
  //     // disableOnInteraction: true,
  //     //waitForTransition: false,
  //     reverseDirection: true,
  //   },
  //   // slidesPerView: "auto",
  //   slidesPerView: "auto",
  //   // slidesPerView: 'auto',
  //   direction: 'horizontal',
  //   spaceBetween: 0,
  //   freeMode: true,
  //   freeModeMomentum: false,
  //   freeModeMomentumBounce: false,

  //   // spaceBetween: 30,
  //   pagination: {
  //     el: ".swiper-pagination",
  //     type: "bullets",
  //     clickable: true,
  //   },
  //   breakpoints: {
  //     320: {
  //       slidesPerView: 2,
  //       spaceBetween: 40,
  //     },
  //     480: {
  //       slidesPerView: 3,
  //       spaceBetween: 40,
  //     },
  //     640: {
  //       slidesPerView: 4,
  //       spaceBetween: 40,
  //     },
  //     992: {
  //       slidesPerView: 6,
  //       spaceBetween: 40,
  //     },
  //   },
  // });


  new Swiper(".clients-slider", {
    speed: 200,
    loop: true,

    keyboard: {
      enabled: true,
    },

    autoplay: {
      delay: 2000,
      disableOnInteraction: true,
      // delay: 0,
      // disableOnInteraction: true,
      //waitForTransition: false,
      reverseDirection: true,
    },
    slidesPerView: "auto",
    // reverseDirection: true,
    direction: 'horizontal',
    spaceBetween: 0,
    freeMode: true,
    freeModeMomentum: false,
    freeModeMomentumBounce: false,
    // speed: 5000,
    // slidesPerView: "auto",
    // spaceBetween: 30,
    pagination: {
      el: ".clients-swiper-pagination",
      type: "bullets",
      clickable: true,
    },
    breakpoints: {
      320: {
        slidesPerView: 2,
        spaceBetween: 40,
      },
      480: {
        slidesPerView: 3,
        spaceBetween: 40,
      },
      640: {
        slidesPerView: 4,
        spaceBetween: 40,
      },
      992: {
        slidesPerView: 6,
        spaceBetween: 40,
      },
    },
  });
  /**
* Clients Slider. coins-slider
*/
  new Swiper(".partners-slider", {
    speed: 200,
    loop: true,

    keyboard: {
      enabled: true,
    },

    autoplay: {
      delay: 2000,
      disableOnInteraction: true,
      // delay: 0,
      // disableOnInteraction: true,
      //waitForTransition: false,
      reverseDirection: true,
    },
    slidesPerView: "auto",
    // reverseDirection: true,
    direction: 'horizontal',
    spaceBetween: 0,
    freeMode: true,
    freeModeMomentum: false,
    freeModeMomentumBounce: false,
    // speed: 5000,
    // slidesPerView: "auto",
    // spaceBetween: 30,
    pagination: {
      el: ".swiper-pagination",
      type: "bullets",
      clickable: true,
    },
    breakpoints: {
      320: {
        slidesPerView: 2,
        spaceBetween: 40,
      },
      480: {
        slidesPerView: 3,
        spaceBetween: 40,
      },
      640: {
        slidesPerView: 4,
        spaceBetween: 40,
      },
      992: {
        slidesPerView: 6,
        spaceBetween: 40,
      },
    },
  });
  /**
   * Porfolio isotope and filter
   */
  window.addEventListener("load", () => {

    let portfolioContainer = select(".portfolio-container");
    if (portfolioContainer) {
      let portfolioIsotope = new Isotope(portfolioContainer, {
        itemSelector: ".portfolio-item",
        layoutMode: "fitRows",
      });

      let portfolioFilters = select("#portfolio-flters li", true);

      on(
        "click",
        "#portfolio-flters li",
        function (e) {
          e.preventDefault();
          portfolioFilters.forEach(function (el) {
            el.classList.remove("filter-active");
          });
          this.classList.add("filter-active");

          portfolioIsotope.arrange({
            filter: this.getAttribute("data-filter"),
          });
          aos_init();
        },
        true
      );
    }
  });

  /**
   * Initiate portfolio lightbox
   */
  const portfolioLightbox = GLightbox({
    selector: ".portfokio-lightbox",
  });
  /**
    * Portfolio details slider
    */
  new Swiper(".last-news-section-swiper", {
    speed: 400,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false,
      reverseDirection: true,

    },

    loop: true,

    keyboard: {
      enabled: true,
    },
    // navigation: {
    //   nextEl: '.swiper-button-next',
    //   prevEl: '.swiper-button-prev',

    // },class="swiper-wrapper align-items-center"
    // news-pagination custom-pagination swiper-pagination-clickable swiper-pagination-bullets swiper-pagination-horizontal
    slidesPerView: "auto",
    // slidesNeView: "auto",

    // slidesPerView: 'auto',
    direction: 'horizontal',
    spaceBetween: 0,
    freeMode: true,
    freeModeMomentum: false,
    freeModeMomentumBounce: false,

    // spaceBetween: 30,
    pagination: {
      el: ".news-pagination",
      type: "bullets",
      clickable: true,
    },
    navigation: {
      nextEl: '.news-next',
      prevEl: '.news-prev',
    },

    breakpoints: {
      320: {
        slidesPerView: 2,
        spaceBetween: 40,
      },
      480: {
        slidesPerView: 3,
        spaceBetween: 40,
      },
      // 640: {
      //   slidesPerView: 4,
      //   spaceBetween: 40,
      // },
      // 992: {
      //   slidesPerView: 6,
      //   spaceBetween: 40,
      // },
    },
  });
  // new Swiper(".serveses-section-swiper", {
  //   speed: 400,
  //   autoplay: {
  //     delay: 5000,
  //     disableOnInteraction: false,
  //     reverseDirection: true,

  //   },
  //   centeredSlides: true,
  //   coverflowEffect: {
  //     rotate: 0,
  //     depth: 500,
  //     modifier: 1,
  //     slideShadows: true
  //   },
  //   loop: true,
  //   // center:true
  //   effect: "coverflow",
  //   // "fade",

  //   keyboard: {
  //     enabled: true,
  //   },
  //   // navigation: {
  //   //   nextEl: '.swiper-button-next',
  //   //   prevEl: '.swiper-button-prev',

  //   // },class="swiper-wrapper align-items-center"
  //   // news-pagination custom-pagination swiper-pagination-clickable swiper-pagination-bullets swiper-pagination-horizontal
  //   slidesPerView: "right",
  //   slidesNeView: "left",

  //   // slidesPerView: 'auto',
  //   direction: 'horizontal',
  //   spaceBetween: 100,
  //   // freeMode: true,
  //   // freeModeMomentum: true,
  //   // freeModeMomentumBounce: true,

  //   // spaceBetween: 30,
  //   pagination: {
  //     el: ".serveses-pagination",
  //     type: "bullets",
  //     clickable: true,
  //   },
  //   navigation: {
  //     nextEl: '.serveses-next',
  //     prevEl: '.serveses-prev',
  //   },

  //   breakpoints: {
  //     280: {
  //       slidesPerView: 3,
  //       // slidesNeView: 3,
  //       spaceBetween: 100,
  //     },
  //     480: {
  //       slidesPerView: 3,

  //       // slidesPerView: 2,
  //       spaceBetween: 100,
  //     },
  //     680: {
  //       slidesPerView: 3,

  //       spaceBetween: 100,
  //     },
  //     // 480: {
  //     //   slidesPerView: 3,
  //     //   spaceBetween: 40,
  //     // },
  //     // 640: {
  //     //   slidesPerView: 4,
  //     //   spaceBetween: 40,
  //     // },
  //     // 992: {
  //     //   slidesPerView: 6,
  //     //   spaceBetween: 40,
  //     // },
  //   },
  // });

  /**
   * Portfolio details slider
   */
  new Swiper(".portfolio-details-slider", {
    speed: 400,
    autoplay: {
      delay: 5000,
      disableOnInteraction: true,
    },
    loop: true,

    keyboard: {
      enabled: true,
    },

    // navigation: {
    //   nextEl: '.swiper-button-next',
    //   prevEl: '.swiper-button-prev',

    // },

    pagination: {
      el: ".hero-pagination ",
      type: "bullets",
      clickable: true,
    },

    // clickable: true,
    // },
    navigation: {
      nextEl: '.hero-next',
      prevEl: '.hero-prev ',
    },


  });

  new Swiper(".hero-slider", {
    speed: 400,
    autoplay: {
      delay: 4000,
      disableOnInteraction: true,
    },
    loop: true,

    keyboard: {
      enabled: true,
    },
    pagination: {
      el: ".hero-pagination ",
      type: "bullets",
      clickable: true,
    },

    // clickable: true,
    // },
    navigation: {
      nextEl: '.hero-next',
      prevEl: '.hero-prev ',
    },

  });
  /**
   * Testimonials slider
   */
  new Swiper(".testimonials-slider", {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false,
    },
    slidesPerView: "auto",
    pagination: {
      el: ".swiper-pagination",
      type: "bullets",
      clickable: true,
    },
    breakpoints: {
      320: {
        slidesPerView: 1,
        spaceBetween: 40,
      },

      1200: {
        slidesPerView: 3,
      },
    },
  });
  new Swiper(".adsheader-slider", {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 4000,
      disableOnInteraction: false,
    },
    slidesPerView: "auto",
    pagination: {
      el: ".swiper-pagination",
      type: "bullets",
      clickable: true,
    },
    breakpoints: {
      320: {
        slidesPerView: 1,
        spaceBetween: 40,
      },

      1200: {
        slidesPerView: 3,
      },
    },
  });




  /**
* Clients Slider. 
*/

  /**
   * Porfolio isotope and filter
   */
  /**
   * Animation on scroll
   */
  function remove_item_navbar(id) {
    var ul = document.getElementById(id);
    ul.remove()
  }
  function add_item_navbar(name, link, id) {
    var ul = document.getElementById("navbar-main");

    var li = document.createElement("li");
    li.setAttribute("id", id)

    var a = document.createElement("a");
    a.setAttribute("class", "nav-link scrollto")
    a.setAttribute("href", link)

    // a.appendChild(document.createTextNode("طلب تمويل"));

    a.appendChild(document.createTextNode(name));

    li.appendChild(a);
    ul.appendChild(li);
  }

})();




