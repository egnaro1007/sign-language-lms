(function ($, window) {
	// Create a custom method to add a box
	WOW.prototype.addBox = function (element) {
		this.boxes.push(element);
	};

	// Automatically add the fadeInUp class and default duration, delay attributes
	$(".wow").each(function () {
		// Always add the 'fadeInUp' class
		$(this).addClass("fadeInUp");
		// Add default duration
		$(this).attr("data-wow-duration", $(this).attr("data-wow-duration") || "0.8s");
		// Add default delay
		$(this).attr("data-wow-delay", $(this).attr("data-wow-delay") || "0.1s");
	});

	// Initialize WOW.js
	new WOW().init();
})(jQuery, window);
