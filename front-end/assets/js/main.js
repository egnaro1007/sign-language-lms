(function ($, window) {
	// Open and close the mobile menu
	$(".header .header__toggleItem").on("click", function () {
		menu_open_sp();
	});

	$(".mainBodyContent").on("click", function () {
		if (!$(this).hasClass("menu__openSp")) return;
		menu_open_sp();
	});

	function menu_open_sp() {
		$("body").toggleClass("mobile-menu-open");
		$(".header__menusp").toggleClass("active");
		$(".header__toggleItem").toggle();
		$(".mainBodyContent").toggleClass("menu__openSp");
	}
	// end mobile menu

	// wpadminbar
	if ($("#wpadminbar").length > 0) {
		$(".header").css("margin-top", $("#wpadminbar").outerHeight(true));
	}
})(jQuery, window);
