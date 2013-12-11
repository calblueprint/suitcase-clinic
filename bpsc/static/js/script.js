$(document).ready(function() {
	$('#Grid').mixitup( {
		easing: 'smooth',
		sortOnLoad: ['data-date','asc'], 
		transitionSpeed: 500,
	});

	var clearStars = function() {
	$('.average').slideUp();;
	};

	$('#housing-filter').click(function() {
		clearStars();
		$('#Housing_Average').slideDown();	
	});

	$('#employment-filter').click(function() {
		clearStars();
		$('#Employment_Average').slideDown();	
	});

	$('#community-filter').click(function() {
		clearStars();
		$('#Community_Average').slideDown();	
	});

	$('#legal-filter').click(function() {
		clearStars();
		$('#Legal_Average').slideDown();	
	});

	$('#dental-filter').click(function() {
		clearStars();
		$('#Dental_Average').slideDown();	
	});

	$('#optometry-filter').click(function() {
		clearStars();
		$('#Optometry_Average').slideDown();	
	});

	$('#medical-filter').click(function() {
		clearStars();
		$('#Medical_Average').slideDown();	
	});

	$('#all-filter').click(function() {
		clearStars();
	});


});

