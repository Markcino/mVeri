const defaultOptions = {};
$('[data-bs-toggle="touchspin"]').each(function (t, a) {
  const n = $.extend({}, defaultOptions, $(a).data());
  $(a).TouchSpin(n);
});
