!(function (n) {
  "use strict";
  function s() {
    for (
      let e = document
          .getElementById("topnav-menu-content")
          .getElementsByTagName("a"),
        t = 0,
        n = e.length;
      t < n;
      t++
    ) {
      e[t].parentElement.getAttribute("class") === "nav-item dropdown active" &&
        (e[t].parentElement.classList.remove("active"),
        e[t].nextElementSibling.classList.remove("show"));
    }
  }
  function t(e) {
    n("#light-mode-switch").prop("checked") == 1 && e === "light-mode-switch"
      ? (n("html").removeAttr("dir"),
        n("#dark-mode-switch").prop("checked", !1),
        n("#rtl-mode-switch").prop("checked", !1),
        n("#bootstrap-style").attr("href", "assets/css/bootstrap.min.css"),
        n("#app-style").attr("href", "assets/css/app.min.css"),
        sessionStorage.setItem("is_visited", "light-mode-switch"))
      : n("#dark-mode-switch").prop("checked") == 1 && e === "dark-mode-switch"
        ? (n("html").removeAttr("dir"),
          n("#light-mode-switch").prop("checked", !1),
          n("#rtl-mode-switch").prop("checked", !1),
          n("#bootstrap-style").attr(
            "href",
            "assets/css/bootstrap-dark.min.css",
          ),
          n("#app-style").attr("href", "assets/css/app-dark.min.css"),
          sessionStorage.setItem("is_visited", "dark-mode-switch"))
        : n("#rtl-mode-switch").prop("checked") == 1 &&
          e === "rtl-mode-switch" &&
          (n("#light-mode-switch").prop("checked", !1),
          n("#dark-mode-switch").prop("checked", !1),
          n("#bootstrap-style").attr(
            "href",
            "assets/css/bootstrap-rtl.min.css",
          ),
          n("#app-style").attr("href", "assets/css/app-rtl.min.css"),
          n("html").attr("dir", "rtl"),
          sessionStorage.setItem("is_visited", "rtl-mode-switch"));
  }
  function e() {
    document.webkitIsFullScreen ||
      document.mozFullScreen ||
      document.msFullscreenElement ||
      (console.log("pressed"), n("body").removeClass("fullscreen-enable"));
  }
  let a;
  n("#side-menu").metisMenu(),
    n("#vertical-menu-btn").on("click", function (e) {
      e.preventDefault(),
        n("body").toggleClass("sidebar-enable"),
        n(window).width() >= 992
          ? n("body").toggleClass("vertical-collpsed")
          : n("body").removeClass("vertical-collpsed");
    }),
    n("body,html").click(function (e) {
      const t = n("#vertical-menu-btn");
      t.is(e.target) ||
        t.has(e.target).length !== 0 ||
        e.target.closest("div.vertical-menu") ||
        n("body").removeClass("sidebar-enable");
    }),
    n("#sidebar-menu a").each(function () {
      const e = window.location.href.split(/[?#]/)[0];
      this.href == e &&
        (n(this).addClass("active"),
        n(this).parent().addClass("mm-active"),
        n(this).parent().parent().addClass("mm-show"),
        n(this).parent().parent().prev().addClass("mm-active"),
        n(this).parent().parent().parent().addClass("mm-active"),
        n(this).parent().parent().parent().parent().addClass("mm-show"),
        n(this)
          .parent()
          .parent()
          .parent()
          .parent()
          .parent()
          .addClass("mm-active"));
    }),
    n(".navbar-nav a").each(function () {
      const e = window.location.href.split(/[?#]/)[0];
      this.href == e &&
        (n(this).addClass("active"),
        n(this).parent().addClass("active"),
        n(this).parent().parent().addClass("active"),
        n(this).parent().parent().parent().addClass("active"),
        n(this).parent().parent().parent().parent().addClass("active"),
        n(this)
          .parent()
          .parent()
          .parent()
          .parent()
          .parent()
          .addClass("active"));
    }),
    n(document).ready(function () {
      let e;
      n("#sidebar-menu").length > 0 &&
        n("#sidebar-menu .mm-active .active").length > 0 &&
        (e = n("#sidebar-menu .mm-active .active").offset().top) > 300 &&
        ((e -= 300),
        n(".vertical-menu .simplebar-content-wrapper").animate(
          { scrollTop: e },
          "slow",
        ));
    }),
    n('[data-toggle="fullscreen"]').on("click", function (e) {
      e.preventDefault(),
        n("body").toggleClass("fullscreen-enable"),
        document.fullscreenElement ||
        document.mozFullScreenElement ||
        document.webkitFullscreenElement
          ? document.cancelFullScreen
            ? document.cancelFullScreen()
            : document.mozCancelFullScreen
              ? document.mozCancelFullScreen()
              : document.webkitCancelFullScreen &&
                document.webkitCancelFullScreen()
          : document.documentElement.requestFullscreen
            ? document.documentElement.requestFullscreen()
            : document.documentElement.mozRequestFullScreen
              ? document.documentElement.mozRequestFullScreen()
              : document.documentElement.webkitRequestFullscreen &&
                document.documentElement.webkitRequestFullscreen(
                  Element.ALLOW_KEYBOARD_INPUT,
                );
    }),
    document.addEventListener("fullscreenchange", e),
    document.addEventListener("webkitfullscreenchange", e),
    document.addEventListener("mozfullscreenchange", e),
    n(".right-bar-toggle").on("click", function (e) {
      n("body").toggleClass("right-bar-enabled");
    }),
    n(document).on("click", "body", function (e) {
      n(e.target).closest(".right-bar-toggle, .right-bar").length > 0 ||
        n("body").removeClass("right-bar-enabled");
    }),
    (function () {
      if (document.getElementById("topnav-menu-content")) {
        for (
          let e = document
              .getElementById("topnav-menu-content")
              .getElementsByTagName("a"),
            t = 0,
            n = e.length;
          t < n;
          t++
        ) {
          e[t].onclick = function (e) {
            e.target.getAttribute("href") === "#" &&
              (e.target.parentElement.classList.toggle("active"),
              e.target.nextElementSibling.classList.toggle("show"));
          };
        }
        window.addEventListener("resize", s);
      }
    })(),
    [].slice
      .call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
      .map(function (e) {
        return new bootstrap.Tooltip(e);
      }),
    [].slice
      .call(document.querySelectorAll('[data-bs-toggle="popover"]'))
      .map(function (e) {
        return new bootstrap.Popover(e);
      }),
    n(window).on("load", function () {
      n("#status").fadeOut(), n("#preloader").delay(350).fadeOut("slow");
    }),
    window.sessionStorage &&
      ((a = sessionStorage.getItem("is_visited"))
        ? (n(".right-bar input:checkbox").prop("checked", !1),
          n("#" + a).prop("checked", !0),
          t(a))
        : sessionStorage.setItem("is_visited", "light-mode-switch")),
    n("#light-mode-switch, #dark-mode-switch, #rtl-mode-switch").on(
      "change",
      function (e) {
        t(e.target.id);
      },
    ),
    Waves.init();
})(jQuery);
