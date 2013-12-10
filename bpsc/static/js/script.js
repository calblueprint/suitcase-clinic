$(document).ready(function() {
	$('#Grid').mixitup( {
		easing: 'smooth',
		sortOnLoad: ['data-date','asc'], 
		transitionSpeed: 500,
	});


});

var ratingsArray = $('.review-content:has(.review_service:contains("Housing"))').children('rating').text().split('');

