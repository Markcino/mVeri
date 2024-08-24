$("[data-countdown]").each(function () {
  const n = $(this);
  const s = $(this).data("countdown");
  n.countdown(s, function (n) {
    $(this).html(
      n.strftime(
        '<div class="coming-box">%D <span>Days</span></div> <div class="coming-box">%H <span>Hours</span></div> <div class="coming-box">%M <span>Minutes</span></div> <div class="coming-box">%S <span>Seconds</span></div> ',
      ),
    );
  });
});
