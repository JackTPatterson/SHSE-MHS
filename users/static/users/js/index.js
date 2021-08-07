/* Please ❤ this if you like it! */

(function($) {
	"use strict";

	$(function() {
		var header = $(".start-style");
		$(window).scroll(function() {
			var scroll = $(window).scrollTop();

			if (scroll >= 10) {
				header.removeClass("start-style").addClass("scroll-on");
			} else {
				header.removeClass("scroll-on").addClass("start-style");
			}
		});
	});

	//Animation

	$(document).ready(function() {
		$("body.hero-anime").removeClass("hero-anime");
	});

	//Menu On Hover

	$("body").on("mouseenter mouseleave", ".nav-item", function(e) {
		if ($(window).width() > 750) {
			var _d = $(e.target).closest(".nav-item");
			_d.addClass("show");
			setTimeout(function() {
				_d[_d.is(":hover") ? "addClass" : "removeClass"]("show");
			}, 1);
		}
	});

	//Switch light/dark

	$("#switch").on("click", function() {
		if ($("body").hasClass("dark")) {
			$("body").removeClass("dark");
			$("#switch").removeClass("switched");
		} else {
			$("body").addClass("dark");
			$("#switch").addClass("switched");
		}
	});
})(jQuery);

$(function() {
	if ($(window).width() < 440) {
		$('#divider1').css({'display': 'none'});
		$('#spacer').remove();
	}
});

$(document).ready(function(){"use strict";
	
//Scroll back to top

var progressPath = document.querySelector('.progress-wrap path');
var pathLength = progressPath.getTotalLength();
progressPath.style.transition = progressPath.style.WebkitTransition = 'none';
progressPath.style.strokeDasharray = pathLength + ' ' + pathLength;
progressPath.style.strokeDashoffset = pathLength;
progressPath.getBoundingClientRect();
progressPath.style.transition = progressPath.style.WebkitTransition = 'stroke-dashoffset 10ms linear';		
var updateProgress = function () {
	var scroll = $(window).scrollTop();
	var height = $(document).height() - $(window).height();
	var progress = pathLength - (scroll * pathLength / height);
	progressPath.style.strokeDashoffset = progress;
}
updateProgress();
$(window).scroll(updateProgress);	
var offset = 50;
var duration = 550;
jQuery(window).on('scroll', function() {
	if (jQuery(this).scrollTop() > offset) {
		jQuery('.progress-wrap').addClass('active-progress');
	} else {
		jQuery('.progress-wrap').removeClass('active-progress');
	}
});				
jQuery('.progress-wrap').on('click', function(event) {
	event.preventDefault();
	jQuery('html, body').animate({scrollTop: 0}, duration);
	return false;
})


});