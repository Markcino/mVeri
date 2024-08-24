$(document).ready(function () {
  $("#checkout-nav-pills-wizard").bootstrapWizard({
    tabClass: "nav nav-pills nav-justified",
  });
});
const triggerTabList = [].slice.call(
  document.querySelectorAll(".twitter-bs-wizard-nav .nav-link"),
);
triggerTabList.forEach(function (t) {
  const a = new bootstrap.Tab(t);
  t.addEventListener("click", function (t) {
    t.preventDefault(), a.show();
  });
});
