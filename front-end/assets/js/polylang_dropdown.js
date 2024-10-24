(function ($, window) {
	var switchLang = $(".switchLang .switchLang__list");
	if (switchLang.length > 0) {
		switchLang.each(function () {
			let htmlDropdown = null;
			let switchLang_item = $(this);
			let current_lang = switchLang_item.find("li.current-lang");

			let content = current_lang.find("a").html();
			htmlDropdown = $("<a href='javascript:void(0);'></a>")
				.html(content)
				.addClass("switchLang__link selected current-lang");

			let first_option = $("<li></li>", {
				class: "switchLang__item init",
			});

			switchLang_item.prepend(first_option.append(htmlDropdown));

			current_lang.remove();

			var top = 0;
			switchLang_item.children("li:not(.init)").each(function () {
				$(this).css("top", "calc(100% + " + top + "px)");
				top = top + $(this).outerHeight();
			});
		});

		switchLang.on("click", ".init", function () {
			$(this).closest("ul").children("li:not(.init, .current-lang)").toggle();
			$(this).toggleClass("current-lang");
		});

		switchLang.on("click", "li:not(.init)", function () {
			let allOptions = $(this).closest("ul").children("li:not(.init)");
			allOptions.removeClass("selected");
			$(this).addClass("selected");
		});

		$(document).on("click", function (event) {
			if (!$(event.target).closest(switchLang).length) {
				switchLang.find("li:not(.init)").hide();
				switchLang.find(".init").removeClass("current-lang");
			}
		});
	}
})(jQuery, window);
