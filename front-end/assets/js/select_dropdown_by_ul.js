(function ($, window) {
	var selectDropdownCat = $(".selectDropdownCat ul");
	if (selectDropdownCat.length > 0) {
		let category_label = $(".categoryBlock").data("label");

		selectDropdownCat.each(function () {
			let li_first_child = $(this).find("li").has("a.active");
			let htmlDropdown = "";

			if (li_first_child.length === 0) {
				htmlDropdown = $("<a href='javascript:void(0);'></a>")
					.html(contentCategory)
					.addClass("categoryBlock__link selected active");
			} else {
				let content = li_first_child.find("a.active").text();
				htmlDropdown = $("<a href='javascript:void(0);'></a>")
					.html(content)
					.addClass("categoryBlock__link selected active");
			}

			let first_option = $("<li></li>", {
				class: "categoryBlock__item init",
			});

			let label = '<span class="label"><span>' + category_label + "</span></span>";
			$(this).prepend(first_option.append(htmlDropdown.prepend(label)));
		});

		selectDropdownCat.on("click", ".init", function () {
			$(this).closest("ul").children("li:not(.init)").toggle();
			$(this).toggleClass("active");
		});

		selectDropdownCat.on("click", "li:not(.init)", function () {
			let allOptions = $(this).closest("ul").children("li:not(.init)");
			allOptions.removeClass("selected");
			$(this).addClass("selected");
		});

		$(document).on("click", function (event) {
			if (!$(event.target).closest(selectDropdownCat).length) {
				selectDropdownCat.find("li:not(.init)").hide();
				selectDropdownCat.find(".init").removeClass("active");
			}
		});
	}
})(jQuery, window);
