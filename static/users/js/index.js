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

var abt = document.getElementById('scrollBtn')

abt.onclick = function () {
	$('html, body').animate({
		scrollTop: window.pageYOffset + document.getElementById('about').offsetTop - 40
	}, 1300);
}

var images = [
    'https://cybersandbox.ca/resources/new-like.png',
    'https://cybersandbox.ca/resources/new-heart.png'
];


function createParticle (x, y) {

	const particle = document.createElement('particle');
	document.querySelector('#button').appendChild(particle);
  
	// Calculate a random size from 10px to 30px
	const size = Math.floor(Math.random() * 20 + 10);
	particle.style.width = `${size}px`;
	particle.style.height = `${size}px`;
	particle.style.backgroundImage = 'url(' + images[Math.floor(Math.random() * images.length)] + ')';
  
	// Generate a random x & y destination within a distance of 75px from the mouse
	const destinationX = x + (Math.random() - 0.5) * 2 * 90;
	const destinationY = y + (Math.random() - 0.5) * 2 * 90;
	// Store the animation in a variable because we will need it later
	const animation = particle.animate([
	  {
		// Set the origin position of the particle
		// We offset the particle with half its size to center it around the mouse
		transform: `translate(${x - (size / 2)}px, ${y - (size / 2)}px)`,
		opacity: 1
	  },
	  {
		opacity: 1
	  },
	  {
		// We define the final coordinates as the second keyframe
		transform: `translate(${destinationX}px, ${destinationY}px)`,
		opacity: 0
	  }
	], {
	  // Set a random duration from 1000 to 2000ms
	  duration: 1000 + Math.random() * 1000,
	  easing: 'cubic-bezier(0, .9, .57, 1)',
	  // Delay every particle with a random value from 0ms to 200ms
	  delay: Math.random() * 200
	});
	
	// When the animation is complete, remove the element from the DOM
	animation.onfinish = () => {
	  particle.remove();
	};
  }