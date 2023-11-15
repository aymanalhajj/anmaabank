import { I as K, a as Q } from "./IconAppStore.ee785a59.js";
import { I as Y } from "./IconArrowDown.39f6c6c8.js";
import { I as P } from "./IconArrowLeft.2c09fcb5.js";
import { I } from "./IconArrowRight.c6c737f3.js";
import "./IconCalendar.5f75d21a.js";
import { I as V } from "./IconMap.f474cfa7.js";
import { _ as U } from "./NewsCard.1ec18a42.js";
import { N as J } from "./NewsCardSkeleton.9ebef2d8.js";
import { _ as Z } from "./PartnerCard.8a09a006.js";
import { _ as O } from "./ServiceCard.9be2c1e3.js";
import { S as G } from "./ServiceCardSkeleton.c663eea4.js";
import { F as W, S as X } from "./SuccessStoryBox.b7903ba4.js";
import { i as $, r as A, l as B, n as C, S as D, b as F, q as L, p as M, u as N, v as R, g as T, t as _, a as e, d as f, F as g, m as j, c as n, f as o, e as p, _ as q, o as t, w as v, j as w, h as y, x as z } from "./index.2ab10854.js";
const ee = {
    getHomeData() {
        return j.call({
            path: "home",
            method: "GET"
        })
    }
}
    , se = M("HomeStore", {
        state: () => ({
            home: {},
            isHomeLoading: !1,
            options: {
                currencyRate: null,
                ads: null,
                services: null,
                news: null,
                apps: null,
                statistics: null,
                successStories: null,
                servicePoints: null,
                faq: null,
                partners: null
            }
        }),
        getters: {},
        actions: {
            async fetchHome() {
                return this.isHomeLoading = !0,
                    await ee.getHomeData().then(s => {
                        this.home = s.data.data,
                            this.assignSectionsOptions()
                    }
                    ).catch(s => {
                        throw s
                    }
                    ).finally(() => {
                        this.isHomeLoading = !1
                    }
                    )
            },
            assignSectionsOptions() {
                this.home.home_sections_settings.forEach(s => {
                    switch (s.section_key) {
                        case "currency_rates":
                            this.options.currencyRate = s;
                            break;
                        case "ads":
                            this.options.ads = s;
                            break;
                        case "services":
                            this.options.services = s;
                            break;
                        case "news":
                            this.options.news = s;
                            break;
                        case "bank_application":
                            this.options.apps = s;
                            break;
                        case "our_successes":
                            this.options.statistics = s;
                            break;
                        case "success_stories":
                            this.options.successStories = s;
                            break;
                        case "services_points":
                            this.options.servicePoints = s;
                            break;
                        case "faq":
                            this.options.faq = s;
                            break;
                        case "partners":
                            this.options.partners = s;
                            break;
                        default:
                            console.log("false");
                            break
                    }
                }
                )
            }
        }
    })
    , te = {}
    , ne = {
        width: "24",
        height: "15",
        viewBox: "0 0 24 15",
        fill: "none",
        xmlns: "http://www.w3.org/2000/svg"
    }
    , ie = e("path", {
        d: "M16.93 13.5352L23 7.46516L16.93 1.39516",
        stroke: "currentColor",
        "stroke-width": "1.5",
        "stroke-miterlimit": "10",
        "stroke-linecap": "round",
        "stroke-linejoin": "round"
    }, null, -1)
    , oe = e("path", {
        d: "M0.999999 7.53515L23 7.53516",
        stroke: "currentColor",
        "stroke-width": "1.5",
        "stroke-miterlimit": "10",
        "stroke-linecap": "round",
        "stroke-linejoin": "round"
    }, null, -1)
    , ae = [ie, oe];
function ce(s, i) {
    return t(),
        n("svg", ne, ae)
}
const le = q(te, [["render", ce]])
    , re = {}
    , de = {
        width: "24",
        height: "15",
        viewBox: "0 0 24 15",
        fill: "none",
        xmlns: "http://www.w3.org/2000/svg"
    }
    , ue = e("path", {
        d: "M7.07 1.39453L1 7.46453L7.07 13.5345",
        stroke: "currentColor",
        "stroke-width": "1.5",
        "stroke-miterlimit": "10",
        "stroke-linecap": "round",
        "stroke-linejoin": "round"
    }, null, -1)
    , _e = e("path", {
        d: "M23 7.39453H1",
        stroke: "currentColor",
        "stroke-width": "1.5",
        "stroke-miterlimit": "10",
        "stroke-linecap": "round",
        "stroke-linejoin": "round"
    }, null, -1)
    , pe = [ue, _e];
function he(s, i) {
    return t(),
        n("svg", de, pe)
}
const ve = q(re, [["render", he]])
    , ge = {
        class: "ads-swiper"
    }
    , me = {
        class: "hero-item-img"
    }
    , ke = ["src"]
    , ye = {
        class: "hero-content"
    }
    , fe = {
        class: "container"
    }
    , $e = {
        class: "title"
    }
    , we = ["innerHTML"]
    , be = {
        class: "hero-control-container"
    }
    , xe = {
        class: "container"
    }
    , Le = {
        class: "hero-slider-buttons"
    }
    , Se = {
        class: "slider-button hero-prev"
    }
    , qe = {
        class: "slider-button hero-next"
    }
    , Ee = e("div", {
        class: "hero-pagination"
    }, null, -1)
    , Ce = e("div", {
        class: "mouse"
    }, [e("div", {
        class: "wheel"
    })], -1)
    , Ae = [Ce]
    , Ie = {
        __name: "HeroSlider",
        props: {
            hero: Array
        },
        setup(s) {
            function i() {
                window.scrollTo({
                    left: 0,
                    top: document.querySelector("#home-body").getBoundingClientRect().top,
                    behavior: "smooth"
                })
            }
            const a = () => {
                document.querySelectorAll(".hero-swiper .swiper-slide .hero-item").forEach(u => {
                    u.classList.remove("hero-animate")
                }
                ),
                    document.querySelector(".hero-swiper .swiper-slide-active .hero-item").classList.add("hero-animate")
            }
                ;
            return (h, d) => {
                const u = f("swiper-slide")
                    , c = f("swiper");
                return t(),
                    n("section", ge, [o(c, {
                        "slides-per-view": 1,
                        effect: "fade",
                        navigation: {
                            prevEl: ".hero-prev",
                            nextEl: ".hero-next"
                        },
                        rewind: !0,
                        autoplay: {
                            delay: 7e3
                        },
                        pagination: {
                            el: ".hero-pagination",
                            clickable: !0,
                            renderBullet: (l, r) => `
                            <div class=${r}><span></span></div>
                        `
                        },
                        onSlideChangeTransitionStart: d[0] || (d[0] = l => a()),
                        class: "hero-swiper"
                    }, {
                        default: v(() => [(t(!0),
                            n(g, null, y(s.hero, (l, r) => (t(),
                                $(u, {
                                    key: l.id
                                }, {
                                    default: v(() => [e("div", {
                                        class: C(["hero-item", r == 0 ? "hero-animate" : ""])
                                    }, [e("div", me, [e("img", {
                                        alt: "hero item",
                                        src: l.img
                                    }, null, 8, ke)]), e("div", ye, [e("div", fe, [e("h2", $e, _(l.title), 1), e("p", {
                                        innerHTML: l.description
                                    }, null, 8, we)])])], 2)]),
                                    _: 2
                                }, 1024))), 128))]),
                        _: 1
                    }, 8, ["navigation", "pagination"]), e("div", be, [e("div", xe, [e("div", Le, [e("div", Se, [o(ve)]), e("div", qe, [o(le)])]), Ee])]), e("div", {
                        class: "mouse-scroll",
                        onClick: d[1] || (d[1] = l => i())
                    }, Ae)])
            }
        }
    }
    , Pe = "/assets/currency.06a9ea03.png"
    , Be = {
        name: "CurrencyCard",
        props: {
            coin: Object
        },
        setup() {
            return {}
        }
    }
    , He = {
        class: "currency-card"
    }
    , Oe = {
        class: "currency-icon"
    }
    , Ve = ["src", "alt"]
    , Re = {
        class: "currency-info name"
    }
    , je = {
        class: "currency-info currency"
    }
    , Me = {
        class: "currency-info currency"
    };
function Te(s, i, a, h, d, u) {
    return t(),
        n("div", He, [e("div", Oe, [e("img", {
            src: a.coin.coin_icon,
            alt: a.coin.name
        }, null, 8, Ve)]), e("span", Re, _(a.coin.name), 1), e("span", je, _(a.coin.sale), 1), e("span", Me, _(a.coin.buy), 1)])
}
const Fe = q(Be, [["render", Te]])
    , Ne = {
        class: "lavalamp-menu"
    }
    , De = e("div", {
        class: "bg-active"
    }, null, -1)
    , ze = {
        __name: "LavalampMenu",
        props: {
            menuItems: Array
        },
        emits: ["active-exchange-rates"],
        setup(s, { emit: i }) {
            function a(h) {
                i("active-exchange-rates", h.realIndex)
            }
            return (h, d) => {
                const u = f("swiper-slide")
                    , c = f("swiper");
                return t(),
                    n("ul", Ne, [o(c, {
                        slidesPerView: "3",
                        loop: !0,
                        "centered-slides": !0,
                        "slide-to-clicked-slide": !0,
                        onSlideChange: a
                    }, {
                        default: v(() => [(t(!0),
                            n(g, null, y(s.menuItems, l => (t(),
                                $(u, {
                                    key: l
                                }, {
                                    default: v(() => [T(_(l), 1)]),
                                    _: 2
                                }, 1024))), 128))]),
                        _: 1
                    }), De])
            }
        }
    }
    , Ge = {
        key: 0,
        class: "container"
    }
    , Ue = F('<div class="section-heading"><h2 class="skeleton skeleton-title has-bg"></h2><p class="skeleton skeleton-text has-bg"></p></div><div class="exchange-rates-container"><div class="currency-card-skeleton skeleton has-bg"></div><div class="currency-card-head-skeleton"></div><div class="list-box-skeleton"><div class="currency-card-skeleton skeleton has-bg"></div><div class="currency-card-skeleton skeleton has-bg"></div><div class="currency-card-skeleton skeleton has-bg"></div></div></div>', 2)
    , Je = [Ue]
    , Ke = {
        key: 1,
        class: "container"
    }
    , Qe = {
        class: "section-heading text-white"
    }
    , We = {
        class: "section-title"
    }
    , Xe = e("img", {
        src: Pe,
        alt: "currency-img",
        class: "currency-img"
    }, null, -1)
    , Ye = {
        class: "exchange-rates-container"
    }
    , Ze = {
        class: "currency-card-head"
    }
    , es = e("div", {
        class: "currency-icon"
    }, null, -1)
    , ss = e("span", {
        class: "currency-info name"
    }, null, -1)
    , ts = {
        class: "currency-info currency"
    }
    , ns = {
        class: "currency-info currency"
    }
    , is = {
        class: "list-box"
    }
    , os = {
        __name: "CurrenciesSection",
        props: {
            exchangeRates: Array,
            isLoading: Boolean,
            options: Object
        },
        setup(s) {
            function i(d) {
                let u = [];
                return d.forEach(c => {
                    u.push(c.name)
                }
                ),
                    u
            }
            const a = A(0);
            function h(d) {
                a.value = d
            }
            return (d, u) => {
                var r, m;
                const c = f("swiper-slide")
                    , l = f("swiper");
                return s.isLoading || ((r = s.options) == null ? void 0 : r.is_active) ? (t(),
                    n("section", {
                        key: 0,
                        style: L({
                            order: ((m = s.options) == null ? void 0 : m.order) || 1
                        }),
                        class: "currencies-section"
                    }, [s.isLoading ? (t(),
                        n("div", Ge, Je)) : (t(),
                            n("div", Ke, [e("div", Qe, [e("h2", We, _(s.options.title), 1), e("p", null, _(s.options.description), 1)]), Xe, e("div", Ye, [o(ze, {
                                menuItems: i(s.exchangeRates),
                                onActiveExchangeRates: h
                            }, null, 8, ["menuItems"]), e("div", Ze, [es, ss, e("span", ts, _(d.$t("sale")), 1), e("span", ns, _(d.$t("buy")), 1)]), e("div", is, [(t(!0),
                                n(g, null, y(s.exchangeRates, (b, x) => (t(),
                                    $(l, {
                                        key: x,
                                        autoplay: {
                                            delay: 5e3,
                                            disableOnInteraction: !1
                                        },
                                        slidesPerView: "3",
                                        direction: "vertical",
                                        "space-between": 8,
                                        loop: !0,
                                        class: C(["coins-slider", a.value == x ? "active" : ""])
                                    }, {
                                        default: v(() => [(t(!0),
                                            n(g, null, y(s.exchangeRates[x].exchange_rate, E => (t(),
                                                $(c, {
                                                    key: E.id
                                                }, {
                                                    default: v(() => [o(Fe, {
                                                        coin: E
                                                    }, null, 8, ["coin"])]),
                                                    _: 2
                                                }, 1024))), 128))]),
                                        _: 2
                                    }, 1032, ["class"]))), 128))])])]))], 4)) : w("", !0)
            }
        }
    }
    , as = {
        class: "ad-card"
    }
    , cs = ["href"]
    , ls = ["src", "alt"]
    , rs = {
        key: 1,
        class: "ad-image"
    }
    , ds = ["src", "alt"]
    , us = {
        __name: "AdsCard",
        props: {
            ad: Object
        },
        setup(s) {
            return (i, a) => (t(),
                n("div", as, [s.ad.link ? (t(),
                    n("a", {
                        key: 0,
                        class: "ad-image",
                        href: s.ad.link
                    }, [e("img", {
                        src: s.ad.img,
                        alt: s.ad.title
                    }, null, 8, ls)], 8, cs)) : (t(),
                        n("div", rs, [e("img", {
                            src: s.ad.img,
                            alt: s.ad.title
                        }, null, 8, ds)]))]))
        }
    }
    , _s = {
        __name: "AdsSection",
        props: {
            ads: Array,
            isLoading: Boolean,
            options: Object
        },
        setup(s) {
            return (i, a) => {
                var u, c;
                const h = f("swiper-slide")
                    , d = f("swiper");
                return !s.isLoading || ((u = s.options) == null ? void 0 : u.is_active) ? (t(),
                    n(g, {
                        key: 0
                    }, [s.ads.length ? (t(),
                        n("section", {
                            key: 0,
                            style: L({
                                order: ((c = s.options) == null ? void 0 : c.order) || 2
                            }),
                            class: "ads-section"
                        }, [s.isLoading ? w("", !0) : (t(),
                            $(d, {
                                key: 0,
                                class: "ads-slider",
                                spaceBetween: 12,
                                loop: !0,
                                "centered-slides": !1,
                                autoplay: {
                                    delay: 5e3,
                                    pauseOnMouseEnter: !0,
                                    disableOnInteraction: !1
                                },
                                breakpoints: {
                                    0: {
                                        slidesPerView: 1
                                    },
                                    768: {
                                        slidesPerView: 2
                                    },
                                    1400: {
                                        slidesPerView: 3
                                    }
                                }
                            }, {
                                default: v(() => [(t(!0),
                                    n(g, null, y(s.ads, l => (t(),
                                        $(h, {
                                            key: l.id
                                        }, {
                                            default: v(() => [o(us, {
                                                ad: l
                                            }, null, 8, ["ad"])]),
                                            _: 2
                                        }, 1024))), 128))]),
                                _: 1
                            }))], 4)) : w("", !0)], 64)) : w("", !0)
            }
        }
    }
    , ps = {
        class: "container"
    }
    , hs = {
        key: 0,
        class: "section-heading"
    }
    , vs = e("h2", {
        class: "skeleton skeleton-title skeleton-center"
    }, null, -1)
    , gs = e("p", {
        class: "skeleton skeleton-text skeleton-center"
    }, null, -1)
    , ms = [vs, gs]
    , ks = {
        key: 1,
        class: "section-heading text-primary text-center"
    }
    , ys = {
        class: "section-title"
    }
    , fs = {
        class: "services-section-container"
    }
    , $s = {
        class: "container"
    }
    , ws = e("div", {
        class: "services-pagination custom-pagination"
    }, null, -1)
    , bs = {
        class: "services-slider-buttons slider-buttons"
    }
    , xs = {
        class: "slider-button services-prev"
    }
    , Ls = {
        class: "slider-button services-next"
    }
    , Ss = {
        __name: "ServicesSection",
        props: {
            services: Array,
            isLoading: Boolean,
            options: Object
        },
        setup(s) {
            let i = A("desktop");
            function a() {
                window.matchMedia("(max-width: 768px)").matches ? i.value = "mobile" : i.value = "desktop"
            }
            return a(),
                window.addEventListener("resize", a),
                R(() => {
                    window.removeEventListener("resize", a)
                }
                ),
                (h, d) => {
                    var l, r;
                    const u = f("swiper-slide")
                        , c = f("swiper");
                    return s.isLoading || ((l = s.options) == null ? void 0 : l.is_active) ? (t(),
                        n("section", {
                            key: 0,
                            style: L({
                                order: ((r = s.options) == null ? void 0 : r.order) || 3
                            }),
                            class: "services-section-home"
                        }, [e("div", ps, [s.isLoading ? (t(),
                            n("div", hs, ms)) : (t(),
                                n("div", ks, [e("h2", ys, _(s.options.title), 1), e("p", null, _(s.options.description), 1)]))]), e("div", fs, [e("div", $s, [s.isLoading ? (t(),
                                    $(c, {
                                        key: 0,
                                        effect: "coverflow",
                                        "space-between": 0,
                                        grabCursor: !0,
                                        centeredSlides: !0,
                                        coverflowEffect: {
                                            rotate: 0,
                                            depth: 500,
                                            modifier: 1,
                                            slideShadows: !1
                                        },
                                        "slides-per-view": "auto",
                                        navigation: {
                                            prevEl: ".services-prev",
                                            nextEl: ".services-next"
                                        },
                                        loop: !0,
                                        class: "slider-services"
                                    }, {
                                        default: v(() => [(t(),
                                            n(g, null, y(8, m => o(u, {
                                                key: m
                                            }, {
                                                default: v(() => [o(G)]),
                                                _: 2
                                            }, 1024)), 64))]),
                                        _: 1
                                    }, 8, ["navigation"])) : (t(),
                                        n(g, {
                                            key: 1
                                        }, [p(i) == "desktop" ? (t(),
                                            $(c, {
                                                key: 0,
                                                effect: "coverflow",
                                                "space-between": 0,
                                                grabCursor: !0,
                                                centeredSlides: !0,
                                                speed: 500,
                                                coverflowEffect: {
                                                    rotate: 0,
                                                    depth: 500,
                                                    modifier: 1,
                                                    slideShadows: !1
                                                },
                                                loop: !0,
                                                "slides-per-view": "auto",
                                                autoplay: {
                                                    delay: 3e4,
                                                    pauseOnMouseEnter: !0,
                                                    disableOnInteraction: !1
                                                },
                                                navigation: {
                                                    prevEl: ".services-prev",
                                                    nextEl: ".services-next"
                                                },
                                                pagination: {
                                                    el: ".services-pagination",
                                                    clickable: !0
                                                },
                                                class: "slider-services"
                                            }, {
                                                default: v(() => [(t(!0),
                                                    n(g, null, y(s.services, m => (t(),
                                                        $(u, {
                                                            key: m.id
                                                        }, {
                                                            default: v(() => [o(O, {
                                                                service: m
                                                            }, null, 8, ["service"])]),
                                                            _: 2
                                                        }, 1024))), 128))]),
                                                _: 1
                                            }, 8, ["navigation", "pagination"])) : (t(),
                                                $(c, {
                                                    key: 1,
                                                    "space-between": 16,
                                                    grabCursor: !0,
                                                    speed: 500,
                                                    loop: !0,
                                                    "slides-per-view": "auto",
                                                    autoplay: {
                                                        delay: 3e4,
                                                        pauseOnMouseEnter: !0,
                                                        disableOnInteraction: !1
                                                    },
                                                    navigation: {
                                                        prevEl: ".services-prev",
                                                        nextEl: ".services-next"
                                                    },
                                                    pagination: {
                                                        el: ".services-pagination",
                                                        clickable: !0
                                                    },
                                                    class: "slider-services-mobile"
                                                }, {
                                                    default: v(() => [(t(!0),
                                                        n(g, null, y(s.services, m => (t(),
                                                            $(u, {
                                                                key: m.id
                                                            }, {
                                                                default: v(() => [o(O, {
                                                                    service: m
                                                                }, null, 8, ["service"])]),
                                                                _: 2
                                                            }, 1024))), 128))]),
                                                    _: 1
                                                }, 8, ["navigation", "pagination"])), ws], 64)), e("div", bs, [e("div", xs, [o(P)]), e("div", Ls, [o(I)])])])])], 4)) : w("", !0)
                }
        }
    }
    , qs = {
        class: "container"
    }
    , Es = {
        key: 0,
        class: "section-heading"
    }
    , Cs = e("h2", {
        class: "skeleton skeleton-title skeleton-center"
    }, null, -1)
    , As = e("p", {
        class: "skeleton skeleton-text skeleton-center"
    }, null, -1)
    , Is = [Cs, As]
    , Ps = {
        key: 1,
        class: "section-heading text-center text-white"
    }
    , Bs = {
        class: "section-title"
    }
    , Hs = {
        class: "last-news-section-container slider-container"
    }
    , Os = {
        class: "last-news-slider-buttons slider-buttons"
    }
    , Vs = {
        class: "slider-button news-prev"
    }
    , Rs = {
        class: "slider-button news-next"
    }
    , js = e("div", {
        class: "news-pagination custom-pagination"
    }, null, -1)
    , Ms = {
        __name: "LastNewsSection",
        props: {
            news: Array,
            isLoading: Boolean,
            options: Object
        },
        setup(s) {
            return (i, a) => {
                var u, c, l, r;
                const h = f("swiper-slide")
                    , d = f("swiper");
                return s.isLoading || ((u = s.options) == null ? void 0 : u.is_active) ? (t(),
                    n("section", {
                        key: 0,
                        style: L({
                            order: ((c = s.options) == null ? void 0 : c.order) || 4
                        }),
                        class: "last-news-section"
                    }, [e("div", qs, [s.isLoading ? (t(),
                        n("div", Es, Is)) : (t(),
                            n("div", Ps, [e("h2", Bs, _((l = s.options) == null ? void 0 : l.title), 1), e("p", null, _((r = s.options) == null ? void 0 : r.description), 1)])), e("div", Hs, [s.isLoading ? (t(),
                                $(d, {
                                    key: 0,
                                    class: "last-news-slider",
                                    spaceBetween: 16,
                                    breakpoints: {
                                        0: {
                                            slidesPerView: "auto"
                                        },
                                        768: {
                                            slidesPerView: 2
                                        },
                                        1199: {
                                            slidesPerView: 4
                                        }
                                    },
                                    navigation: {
                                        prevEl: ".news-prev",
                                        nextEl: ".news-next"
                                    },
                                    pagination: {
                                        el: ".news-pagination",
                                        clickable: !0
                                    }
                                }, {
                                    default: v(() => [(t(),
                                        n(g, null, y(5, m => o(h, {
                                            key: m
                                        }, {
                                            default: v(() => [o(J)]),
                                            _: 2
                                        }, 1024)), 64))]),
                                    _: 1
                                }, 8, ["navigation", "pagination"])) : (t(),
                                    $(d, {
                                        key: 1,
                                        class: "last-news-slider",
                                        spaceBetween: 16,
                                        autoplay: {
                                            delay: 3e3,
                                            pauseOnMouseEnter: !0,
                                            disableOnInteraction: !1
                                        },
                                        breakpoints: {
                                            0: {
                                                slidesPerView: "auto"
                                            },
                                            768: {
                                                slidesPerView: 2
                                            },
                                            1199: {
                                                slidesPerView: 4
                                            }
                                        },
                                        navigation: {
                                            prevEl: ".news-prev",
                                            nextEl: ".news-next"
                                        },
                                        pagination: {
                                            el: ".news-pagination",
                                            clickable: !0
                                        }
                                    }, {
                                        default: v(() => [(t(!0),
                                            n(g, null, y(s.news, m => (t(),
                                                $(h, {
                                                    key: m.id
                                                }, {
                                                    default: v(() => [o(U, {
                                                        news: m
                                                    }, null, 8, ["news"])]),
                                                    _: 2
                                                }, 1024))), 128))]),
                                        _: 1
                                    }, 8, ["navigation", "pagination"])), e("div", Os, [e("div", Vs, [o(P)]), e("div", Rs, [o(I)])]), js])])], 4)) : w("", !0)
            }
        }
    }
    , Ts = {
        class: "container"
    }
    , Fs = {
        key: 0,
        class: "apps-section-container"
    }
    , Ns = {
        class: "apps-slider"
    }
    , Ds = {
        class: "features-app-box"
    }
    , zs = e("div", {
        class: "skeleton skeleton-text"
    }, null, -1)
    , Gs = e("div", {
        class: "skeleton skeleton-paragraph"
    }, null, -1)
    , Us = e("div", {
        class: "skeleton skeleton-paragraph-s app-description"
    }, null, -1)
    , Js = {
        class: "features-list"
    }
    , Ks = e("h6", {
        class: "skeleton skeleton skeleton-paragraph-s"
    }, null, -1)
    , Qs = e("div", {
        class: "skeleton skeleton-paragraph-s"
    }, null, -1)
    , Ws = [Qs]
    , Xs = {
        class: "app-device"
    }
    , Ys = e("div", {
        class: "app-img"
    }, null, -1)
    , Zs = [Ys]
    , et = {
        key: 1,
        class: "apps-section-container"
    }
    , st = ["data-img-id"]
    , tt = {
        class: "app-icon"
    }
    , nt = ["src"]
    , it = {
        class: "app-name"
    }
    , ot = {
        class: "app-description"
    }
    , at = {
        class: "features-list"
    }
    , ct = {
        class: "features-list-title"
    }
    , lt = {
        class: "app-footer"
    }
    , rt = {
        class: "qr-code-scan"
    }
    , dt = {
        class: "qr-code-txt"
    }
    , ut = {
        class: "qr-code"
    }
    , _t = ["data-img-id", "src"]
    , pt = {
        key: 0,
        class: "list-app-link-container"
    }
    , ht = {
        class: "list-app-link-title"
    }
    , vt = {
        class: "list-app-link"
    }
    , gt = ["href"]
    , mt = ["href"]
    , kt = {
        key: 1,
        class: "list-system-link-container"
    }
    , yt = ["href"]
    , ft = {
        class: "app-device"
    }
    , $t = {
        class: "app-img"
    }
    , wt = ["src", "id"]
    , bt = {
        class: "apps-slider-buttons slider-buttons buttons-outline"
    }
    , xt = {
        class: "slider-button apps-prev"
    }
    , Lt = {
        class: "slider-button apps-next"
    }
    , St = {
        __name: "AppSection",
        props: {
            apps: Array,
            isLoading: Boolean,
            options: Object
        },
        setup(s) {
            const i = s
                , a = N()
                , h = A(null)
                , d = A("phone-screen");
            B(() => {
                h.value = new D(".apps-slider")
            }
            );
            const u = () => {
                let r = document.querySelector(".apps-slider .swiper-slide-active .features-app-box");
                document.querySelectorAll(".app-imgs img").forEach(x => {
                    x.classList.remove("active")
                }
                );
                let b = document.getElementById(r.getAttribute("data-img-id"));
                b && b.classList.add("active")
            }
                ;
            function c(r) {
                d.value = i.apps[r.realIndex].type_app === "app" ? "phone-screen" : "wide-screen"
            }
            function l(r) {
                h.value.slideTo(r),
                    u()
            }
            return z(() => a.app_selected_id, () => {
                console.log("settingStore.app_selected_id: ", a.app_selected_id),
                    l(a.app_selected_id)
            }
            ),
                (r, m) => {
                    var E, H;
                    const b = f("swiper-slide")
                        , x = f("swiper");
                    return s.isLoading || ((E = s.options) == null ? void 0 : E.is_active) ? (t(),
                        n("section", {
                            key: 0,
                            style: L({
                                order: ((H = s.options) == null ? void 0 : H.order) || 5
                            }),
                            id: "apps",
                            class: "apps-section"
                        }, [e("div", Ts, [s.apps ? (t(),
                            n("div", et, [o(x, {
                                "slides-per-view": 1,
                                spaceBetween: 16,
                                loop: !0,
                                grabCursor: !0,
                                autoHeight: !0,
                                centeredSlides: !0,
                                pagination: {
                                    el: ".apps-pagination",
                                    clickable: !0,
                                    renderBullet: (k, S) => `
                            <div class=${S}><span></span></div>
                        `
                                },
                                onSlideChangeTransitionStart: m[0] || (m[0] = k => u()),
                                navigation: {
                                    prevEl: ".apps-prev",
                                    nextEl: ".apps-next"
                                },
                                onSlideChange: c,
                                class: "apps-slider"
                            }, {
                                default: v(() => [(t(!0),
                                    n(g, null, y(s.apps, k => (t(),
                                        $(b, {
                                            key: k.id
                                        }, {
                                            default: v(() => [e("div", {
                                                class: "features-app-box",
                                                "data-img-id": `app-img-${k.id}`
                                            }, [e("div", tt, [e("img", {
                                                alt: "app-icon",
                                                src: k.app_logo
                                            }, null, 8, nt)]), e("h5", it, _(k.title), 1), e("p", ot, _(k.description), 1), e("div", at, [e("h6", ct, _(k.type_app === "app" ? r.$t("app_features") : r.$t("system_features")) + " : ", 1), e("ul", null, [(t(!0),
                                                n(g, null, y(k.application_advantages, S => (t(),
                                                    n("li", {
                                                        key: S.id
                                                    }, [e("span", null, _(S.title), 1)]))), 128))])]), e("div", lt, [e("div", rt, [e("span", dt, _(r.$t("scan_here")), 1), e("div", ut, [e("img", {
                                                        "data-img-id": `app-img-${k.id}`,
                                                        src: `data:image/svg+xml;base64,${k.qr}`
                                                    }, null, 8, _t)])]), k.type_app === "app" ? (t(),
                                                        n("div", pt, [e("span", ht, _(r.$t("or_download_app_via")) + " :", 1), e("div", vt, [k.google_play_link ? (t(),
                                                            n("a", {
                                                                key: 0,
                                                                href: k.google_play_link,
                                                                target: "_blank"
                                                            }, [o(K)], 8, gt)) : w("", !0), k.app_store_link ? (t(),
                                                                n("a", {
                                                                    key: 1,
                                                                    href: k.app_store_link,
                                                                    target: "_blank"
                                                                }, [o(Q)], 8, mt)) : w("", !0)])])) : (t(),
                                                                    n("div", kt, [e("span", null, _(r.$t("or_visit_website")), 1), e("a", {
                                                                        href: k.web_link,
                                                                        target: "_blank"
                                                                    }, _(r.$t("by_clicking_here")), 9, yt)]))])], 8, st)]),
                                            _: 2
                                        }, 1024))), 128))]),
                                _: 1
                            }, 8, ["pagination", "navigation"]), e("div", ft, [e("div", {
                                class: C(["app-imgs", d.value])
                            }, [e("div", $t, [(t(!0),
                                n(g, null, y(s.apps, (k, S) => (t(),
                                    n("img", {
                                        alt: "app-img",
                                        key: k.id,
                                        src: k.app_img,
                                        id: `app-img-${k.id}`,
                                        class: C(S == 0 ? "active" : "")
                                    }, null, 10, wt))), 128))])], 2)])])) : (t(),
                                        n("div", Fs, [e("div", Ns, [e("div", Ds, [zs, Gs, Us, e("div", Js, [Ks, e("ul", null, [(t(),
                                            n(g, null, y(8, k => e("li", {
                                                key: k
                                            }, Ws)), 64))])])])]), e("div", Xs, [e("div", {
                                                class: C(["app-imgs", d.value])
                                            }, Zs, 2)])])), e("div", bt, [e("div", xt, [o(P)]), e("div", Lt, [o(I)])])])], 4)) : w("", !0)
                }
        }
    }
    , qt = {
        class: "container"
    }
    , Et = {
        key: 0,
        class: "section-heading statistics-section-heading"
    }
    , Ct = e("h2", {
        class: "skeleton skeleton-title skeleton-center"
    }, null, -1)
    , At = e("p", {
        class: "skeleton skeleton-text skeleton-center"
    }, null, -1)
    , It = [Ct, At]
    , Pt = {
        key: 1,
        class: "section-heading statistics-section-heading"
    }
    , Bt = {
        class: "section-title"
    }
    , Ht = {
        key: 2,
        class: "list-statistics"
    }
    , Ot = e("span", {
        class: "skeleton has-bg skeleton-text"
    }, null, -1)
    , Vt = e("span", {
        class: "skeleton has-bg skeleton-paragraph"
    }, null, -1)
    , Rt = [Ot, Vt]
    , jt = e("span", {
        class: "number"
    }, "+", -1)
    , Mt = ["data-val"]
    , Tt = {
        class: "txt"
    }
    , Ft = {
        __name: "StatisticsSection",
        props: {
            statistics: Array,
            isLoading: Boolean,
            options: Object
        },
        setup(s) {
            const i = s;
            let a = A(null);
            B(() => {
                document.addEventListener("scroll", h)
            }
            ),
                R(() => {
                    document.removeEventListener("scroll", h)
                }
                );
            function h() {
                if (!i.isLoading && a.value && a.value.getBoundingClientRect().top < window.innerHeight) {
                    let d = document.querySelectorAll(".counter")
                        , u = 400;
                    d.forEach(c => {
                        const l = () => {
                            const r = +c.getAttribute("data-val")
                                , m = +c.innerText
                                , b = r / u;
                            m < r ? (c.innerText = Math.ceil(m + b),
                                setTimeout(l, 1)) : c.innerText = r
                        }
                            ;
                        l()
                    }
                    ),
                        document.removeEventListener("scroll", h)
                }
            }
            return (d, u) => {
                var c, l;
                return s.isLoading || ((c = s.options) == null ? void 0 : c.is_active) ? (t(),
                    n("section", {
                        key: 0,
                        style: L({
                            order: ((l = s.options) == null ? void 0 : l.order) || 6
                        }),
                        class: "statistics-section"
                    }, [e("div", qt, [s.isLoading ? (t(),
                        n("div", Et, It)) : (t(),
                            n("div", Pt, [e("h2", Bt, _(s.options.title), 1), e("p", null, _(s.options.description), 1)])), s.isLoading ? (t(),
                                n("div", Ht, [(t(),
                                    n(g, null, y(6, r => e("div", {
                                        class: "statistic-box",
                                        key: r
                                    }, Rt)), 64))])) : (t(),
                                        n("div", {
                                            key: 3,
                                            ref_key: "list",
                                            ref: a,
                                            class: "list-statistics"
                                        }, [(t(!0),
                                            n(g, null, y(s.statistics, r => (t(),
                                                n("div", {
                                                    class: "statistic-box",
                                                    key: r.id
                                                }, [e("div", null, [jt, e("span", {
                                                    class: "number counter",
                                                    "data-val": r.number
                                                }, "0", 8, Mt)]), e("span", Tt, _(r.title), 1)]))), 128))], 512))])], 4)) : w("", !0)
            }
        }
    }
    , Nt = {
        class: "container"
    }
    , Dt = {
        class: "our-points-content"
    }
    , zt = {
        key: 0,
        class: "section-heading our-points-heading"
    }
    , Gt = e("h2", {
        class: "skeleton skeleton-title has-bg"
    }, null, -1)
    , Ut = e("p", {
        class: "skeleton skeleton-text has-bg"
    }, null, -1)
    , Jt = [Gt, Ut]
    , Kt = {
        key: 1,
        class: "section-heading text-primary"
    }
    , Qt = {
        class: "section-title"
    }
    , Wt = {
        class: "service-point-numbers"
    }
    , Xt = {
        key: 0
    }
    , Yt = {
        class: "num"
    }
    , Zt = {
        __name: "ServicePointSection",
        props: {
            servicePoints: Array,
            isLoading: Boolean,
            options: Object
        },
        setup(s) {
            return (i, a) => {
                var d, u;
                const h = f("RouterLink");
                return s.isLoading || ((d = s.options) == null ? void 0 : d.is_active) ? (t(),
                    n("section", {
                        key: 0,
                        style: L({
                            order: ((u = s.options) == null ? void 0 : u.order) || 8
                        }),
                        class: "our-points"
                    }, [e("div", Nt, [e("div", Dt, [s.isLoading ? (t(),
                        n("div", zt, Jt)) : (t(),
                            n("div", Kt, [e("h2", Qt, _(s.options.title), 1), e("p", null, _(s.options.description), 1)])), o(h, {
                                class: "btn btn-primary",
                                to: i.$i18nRoute({
                                    name: "servicePoint"
                                })
                            }, {
                                default: v(() => [o(V), e("span", null, _(i.$t("show_our_points_desc")), 1)]),
                                _: 1
                            }, 8, ["to"])]), e("div", Wt, [s.isLoading ? w("", !0) : (t(),
                                n("ul", Xt, [(t(!0),
                                    n(g, null, y(s.servicePoints, c => (t(),
                                        n("li", {
                                            key: c.id
                                        }, [e("span", Yt, _(c.count), 1), e("span", null, _(c.name), 1)]))), 128))])), o(h, {
                                            class: "btn btn-primary",
                                            to: i.$i18nRoute({
                                                name: "servicePoint"
                                            })
                                        }, {
                                            default: v(() => [o(V), e("span", null, _(i.$t("show_our_points_desc")), 1)]),
                                            _: 1
                                        }, 8, ["to"])])])], 4)) : w("", !0)
            }
        }
    }
    , en = {
        name: "FaqCardSkeleton",
        props: {},
        setup() { },
        methods: {},
        components: {
            IconArrowDown: Y
        }
    }
    , sn = {
        class: "faq-card"
    }
    , tn = {
        class: "question"
    }
    , nn = e("h5", {
        class: "skeleton skeleton-text m-0"
    }, null, -1)
    , on = {
        class: "icon"
    }
    , an = e("div", {
        class: "answer"
    }, null, -1);
function cn(s, i, a, h, d, u) {
    const c = f("IconArrowDown");
    return t(),
        n("div", sn, [e("div", tn, [nn, e("div", on, [o(c)])]), an])
}
const ln = q(en, [["render", cn]])
    , rn = {
        name: "FaqSection",
        components: {
            FaqCard: W,
            FaqCardSkeleton: ln
        },
        props: {
            faqs: Array,
            isLoading: Boolean,
            options: Object
        },
        setup() {
            B(() => {
                document.querySelectorAll(".list-faqs .faq-card").forEach(i => {
                    i.addEventListener("click", () => {
                        i.classList.toggle("open");
                        let a = i.querySelector(".answer");
                        a.style.maxHeight ? a.style.maxHeight = null : a.style.maxHeight = a.scrollHeight + "px"
                    }
                    )
                }
                )
            }
            )
        }
    }
    , dn = {
        class: "container"
    }
    , un = {
        key: 0,
        class: "section-heading faqs-sections-heading"
    }
    , _n = e("h2", {
        class: "skeleton skeleton-title skeleton-center has-bg"
    }, null, -1)
    , pn = e("p", {
        class: "skeleton skeleton-text skeleton-center has-bg"
    }, null, -1)
    , hn = [_n, pn]
    , vn = {
        key: 1,
        class: "section-heading text-center text-white"
    }
    , gn = {
        class: "section-title"
    }
    , mn = {
        key: 2,
        class: "list-faqs"
    }
    , kn = {
        key: 3,
        class: "list-faqs"
    }
    , yn = {
        class: "list-faq-col"
    }
    , fn = {
        class: "list-faq-col"
    };
function $n(s, i, a, h, d, u) {
    var r, m;
    const c = f("FaqCardSkeleton")
        , l = f("FaqCard");
    return a.isLoading || ((r = a.options) == null ? void 0 : r.is_active) ? (t(),
        n("section", {
            key: 0,
            style: L({
                order: ((m = a.options) == null ? void 0 : m.order) || 9
            }),
            class: "faqs-sections"
        }, [e("div", dn, [a.isLoading ? (t(),
            n("div", un, hn)) : (t(),
                n("div", vn, [e("h2", gn, _(a.options.title), 1), e("p", null, _(a.options.description), 1)])), a.isLoading ? (t(),
                    n("div", mn, [(t(),
                        n(g, null, y(6, b => o(c, {
                            key: b
                        })), 64))])) : (t(),
                            n("div", kn, [e("div", yn, [(t(!0),
                                n(g, null, y(a.faqs, (b, x) => (t(),
                                    n(g, {
                                        key: b.id
                                    }, [x % 2 === 0 ? (t(),
                                        $(l, {
                                            key: 0,
                                            faq: b
                                        }, null, 8, ["faq"])) : w("", !0)], 64))), 128))]), e("div", fn, [(t(!0),
                                            n(g, null, y(a.faqs, (b, x) => (t(),
                                                n(g, {
                                                    key: b.id
                                                }, [x % 2 !== 0 ? (t(),
                                                    $(l, {
                                                        key: 0,
                                                        faq: b
                                                    }, null, 8, ["faq"])) : w("", !0)], 64))), 128))])]))])], 4)) : w("", !0)
}
const wn = q(rn, [["render", $n]])
    , bn = {
        class: "container"
    }
    , xn = {
        key: 0,
        class: "section-heading faqs-sections-heading"
    }
    , Ln = e("h2", {
        class: "skeleton skeleton-title skeleton-center"
    }, null, -1)
    , Sn = e("p", {
        class: "skeleton skeleton-text skeleton-center"
    }, null, -1)
    , qn = [Ln, Sn]
    , En = {
        key: 1,
        class: "section-heading text-primary text-center"
    }
    , Cn = {
        class: "section-title"
    }
    , An = {
        key: 2,
        class: "list-partners"
    }
    , In = {
        key: 3,
        class: "list-partners-container"
    }
    , Pn = {
        class: "partners-slider-buttons slider-buttons"
    }
    , Bn = {
        class: "slider-button partners-prev"
    }
    , Hn = {
        class: "slider-button partners-next"
    }
    , On = e("div", {
        class: "partners-pagination custom-pagination"
    }, null, -1)
    , Vn = {
        __name: "PartnerSection",
        props: {
            partners: Array,
            isLoading: Boolean,
            options: Object
        },
        setup(s) {
            return B(() => { }
            ),
                (i, a) => {
                    var u, c;
                    const h = f("swiper-slide")
                        , d = f("swiper");
                    return s.isLoading || ((u = s.options) == null ? void 0 : u.is_active) ? (t(),
                        n("section", {
                            key: 0,
                            style: L({
                                order: ((c = s.options) == null ? void 0 : c.order) || 10
                            }),
                            class: "partners-sections"
                        }, [e("div", bn, [s.isLoading ? (t(),
                            n("div", xn, qn)) : (t(),
                                n("div", En, [e("h2", Cn, _(s.options.title), 1), e("p", null, _(s.options.description), 1)])), s.isLoading ? (t(),
                                    n("div", An)) : (t(),
                                        n("div", In, [o(d, {
                                            class: "list-partners-slider",
                                            spaceBetween: 16,
                                            navigation: {
                                                prevEl: ".partners-prev",
                                                nextEl: ".partners-next"
                                            },
                                            breakpoints: {
                                                0: {
                                                    slidesPerView: "auto"
                                                },
                                                768: {
                                                    slidesPerView: 2
                                                },
                                                1199: {
                                                    slidesPerView: 4
                                                }
                                            },
                                            pagination: {
                                                el: ".partners-pagination",
                                                clickable: !0
                                            }
                                        }, {
                                            default: v(() => [(t(!0),
                                                n(g, null, y(s.partners, l => (t(),
                                                    $(h, {
                                                        key: l.id
                                                    }, {
                                                        default: v(() => [o(Z, {
                                                            partner: l
                                                        }, null, 8, ["partner"])]),
                                                        _: 2
                                                    }, 1024))), 128))]),
                                            _: 1
                                        }, 8, ["navigation", "pagination"]), e("div", Pn, [e("div", Bn, [o(P)]), e("div", Hn, [o(I)])])])), On])], 4)) : w("", !0)
                }
        }
    }
    , Rn = {}
    , jn = {
        class: "skeleton news-card"
    };
function Mn(s, i) {
    return t(),
        n("div", jn)
}
const Tn = q(Rn, [["render", Mn]])
    , Fn = {
        class: "container"
    }
    , Nn = {
        key: 0,
        class: "section-heading success-stories-section-heading"
    }
    , Dn = e("h2", {
        class: "skeleton skeleton-title skeleton-center"
    }, null, -1)
    , zn = e("p", {
        class: "skeleton skeleton-text skeleton-center"
    }, null, -1)
    , Gn = [Dn, zn]
    , Un = {
        key: 1,
        class: "section-heading text-center text-primary"
    }
    , Jn = {
        class: "section-title"
    }
    , Kn = {
        class: "slider-container"
    }
    , Qn = {
        class: "success-story-slider-buttons slider-buttons"
    }
    , Wn = {
        class: "slider-button success-story-prev"
    }
    , Xn = {
        class: "slider-button success-story-next"
    }
    , Yn = e("div", {
        class: "success-story-pagination custom-pagination"
    }, null, -1)
    , Zn = {
        __name: "SuccessStoriesSection",
        props: {
            successStories: Array,
            isLoading: Boolean,
            options: Object
        },
        setup(s) {
            return (i, a) => {
                var u, c;
                const h = f("swiper-slide")
                    , d = f("swiper");
                return s.isLoading || ((u = s.options) == null ? void 0 : u.is_active) ? (t(),
                    n("section", {
                        key: 0,
                        style: L({
                            order: ((c = s.options) == null ? void 0 : c.order) || 7
                        }),
                        class: "success-stories-section"
                    }, [e("div", Fn, [s.isLoading ? (t(),
                        n("div", Nn, Gn)) : (t(),
                            n("div", Un, [e("h2", Jn, _(s.options.title), 1), e("p", null, _(s.options.description), 1)])), e("div", Kn, [s.isLoading ? (t(),
                                $(d, {
                                    key: 0,
                                    spaceBetween: 16,
                                    rewind: !1,
                                    autoplay: {
                                        delay: 4e3,
                                        pauseOnMouseEnter: !0,
                                        disableOnInteraction: !1
                                    },
                                    breakpoints: {
                                        0: {
                                            slidesPerView: "auto"
                                        },
                                        768: {
                                            slidesPerView: 2
                                        },
                                        1199: {
                                            slidesPerView: 4
                                        }
                                    },
                                    navigation: {
                                        prevEl: ".success-story-prev",
                                        nextEl: ".success-story-next"
                                    },
                                    pagination: {
                                        el: ".success-story-pagination",
                                        clickable: !0
                                    }
                                }, {
                                    default: v(() => [(t(),
                                        n(g, null, y(8, l => o(h, {
                                            key: l
                                        }, {
                                            default: v(() => [o(Tn)]),
                                            _: 2
                                        }, 1024)), 64))]),
                                    _: 1
                                }, 8, ["navigation", "pagination"])) : (t(),
                                    $(d, {
                                        key: 1,
                                        spaceBetween: 16,
                                        rewind: !0,
                                        autoplay: {
                                            delay: 4e3,
                                            pauseOnMouseEnter: !0,
                                            disableOnInteraction: !1
                                        },
                                        breakpoints: {
                                            0: {
                                                slidesPerView: "auto"
                                            },
                                            768: {
                                                slidesPerView: 2
                                            },
                                            1199: {
                                                slidesPerView: 4
                                            }
                                        },
                                        navigation: {
                                            prevEl: ".success-story-prev",
                                            nextEl: ".success-story-next"
                                        },
                                        pagination: {
                                            el: ".success-story-pagination",
                                            clickable: !0
                                        }
                                    }, {
                                        default: v(() => [(t(!0),
                                            n(g, null, y(s.successStories, l => (t(),
                                                $(h, {
                                                    key: l.id
                                                }, {
                                                    default: v(() => [o(X, {
                                                        story: l
                                                    }, null, 8, ["story"])]),
                                                    _: 2
                                                }, 1024))), 128))]),
                                        _: 1
                                    }, 8, ["navigation", "pagination"])), e("div", Qn, [e("div", Wn, [o(P)]), e("div", Xn, [o(I)])]), Yn])])], 4)) : w("", !0)
            }
        }
    }
    , ei = {
        id: "home-body"
    }
    , hi = {
        __name: "HomeView",
        setup(s) {
            const i = se();
            return i.fetchHome(),
                (a, h) => (t(),
                    n("main", null, [o(Ie, {
                        hero: p(i).home.heroes
                    }, null, 8, ["hero"]), e("div", ei, [o(Ss, {
                        services: p(i).home.services,
                        isLoading: p(i).isHomeLoading,
                        options: p(i).options.services
                    }, null, 8, ["services", "isLoading", "options"]), o(os, {
                        "exchange-rates": p(i).home.exchange_rates,
                        isLoading: p(i).isHomeLoading,
                        options: p(i).options.currencyRate
                    }, null, 8, ["exchange-rates", "isLoading", "options"]), o(_s, {
                        ads: p(i).home.ads,
                        isLoading: p(i).isHomeLoading,
                        options: p(i).options.ads
                    }, null, 8, ["ads", "isLoading", "options"]), o(Ms, {
                        news: p(i).home.news,
                        isLoading: p(i).isHomeLoading,
                        options: p(i).options.news
                    }, null, 8, ["news", "isLoading", "options"]), o(St, {
                        apps: p(i).home.apps,
                        isLoading: p(i).isHomeLoading,
                        options: p(i).options.apps
                    }, null, 8, ["apps", "isLoading", "options"]), o(Ft, {
                        isLoading: p(i).isHomeLoading,
                        statistics: p(i).home.statistics,
                        options: p(i).options.statistics
                    }, null, 8, ["isLoading", "statistics", "options"]), o(Zn, {
                        "is-loading": p(i).isHomeLoading,
                        "success-stories": p(i).home.success_stories,
                        options: p(i).options.successStories
                    }, null, 8, ["is-loading", "success-stories", "options"]), o(Zt, {
                        isLoading: p(i).isHomeLoading,
                        servicePoints: p(i).home.services_points,
                        options: p(i).options.servicePoints
                    }, null, 8, ["isLoading", "servicePoints", "options"]), o(wn, {
                        isLoading: p(i).isHomeLoading,
                        faqs: p(i).home.faqs,
                        options: p(i).options.faq
                    }, null, 8, ["isLoading", "faqs", "options"]), o(Vn, {
                        isLoading: p(i).isHomeLoading,
                        partners: p(i).home.partners,
                        options: p(i).options.partners
                    }, null, 8, ["isLoading", "partners", "options"])])]))
        }
    };
export { hi as default };

