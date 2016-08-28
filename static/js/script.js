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
    

});
