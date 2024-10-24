(function ($, window) {
	if (window.location.hash) {
		scrollSmooth(window.location.hash);
	}

	$(document).on("click", "#header ul.menu a", function () {
		let link = $(this).attr("href");

		if (link.includes("#")) {
			let hash = link.split("#")[1];
			let target = "#" + hash;

			if ($(target).length > 0) {
				if ($(window).width() < 992) {
					$(".header__toggle").click();
				}
				scrollSmooth(target);
			}
		}
	});

	function scrollSmooth(target) {
		var targetElement = $(target);
		if (targetElement.length > 0) {
			$("html, body").animate(
				{
					scrollTop: targetElement.offset().top - $("#header").outerHeight(true) + 50,
				},
				1000
			);
		}
	}
})(jQuery, window);
