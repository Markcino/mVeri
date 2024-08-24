$(document).ready(function () {
  $("#basic-pills-wizard").bootstrapWizard({
    tabClass: "nav nav-pills nav-justified",
  }),
    $("#progrss-wizard").bootstrapWizard({
      onTabShow: function (a, r, i) {
        const t = ((i + 1) / r.find("li").length) * 100;
        $("#progrss-wizard")
          .find(".progress-bar")
          .css({ width: t + "%" });
      },
    });
});
const triggerTabList = [].slice.call(
  document.querySelectorAll(".twitter-bs-wizard-nav .nav-link"),
);
triggerTabList.forEach(function (a) {
  const r = new bootstrap.Tab(a);
  a.addEventListener("click", function (a) {
    a.preventDefault(), r.show();
  });
});
