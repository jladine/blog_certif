$(document).ready(function(){
  $('.one-time').slick({
      autoplay: true,
      autoplaySpeed: 2000,
  });
  $('.three-time').slick({
      autoplay: true,
      autoplaySpeed: 2000,
      slidesToShow: 3,
    //   slidesToScroll: 3,
  });
  $(function(){
		$('#menu').slicknav();
	});

    setInterval(function() {
        var time = 3;
        $("#redirection").text("Redirection dans " + time + " secondes.");
        if (time === 0) {
            window.location.href = '/';
        }
        time--;
    }, 1000);
});
