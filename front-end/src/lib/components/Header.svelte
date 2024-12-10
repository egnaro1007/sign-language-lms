<script>
	export let searchPlaceholder = 'Tìm kiếm chủ đề, từ vựng...';
</script>

<header class="header">
	<div class="container">
		<div class="header__left">
			<img src="/path/to/logo.png" alt="Logo" />
			<!-- <h1 style="font-size: 16px; margin: 0; padding: 0; font-family: Arial, sans-serif; font-weight: bold;">Thẻ ghi nhớ</h1> -->
			<input
				type="text"
				placeholder={searchPlaceholder}
				style=""
			/>
		</div>


		<!-- Right Section -->
		<div class= "header__right" >
			<div style="display: flex; align-items: center;">
				<img src="/path/to/book-icon.png" alt="Học" style="height: 24px; margin-right: 5px;" />
			</div>
			<div style="display: flex; align-items: center;">
				<img src="/path/to/bee-icon.png" alt="Luyện tập" style="height: 24px; margin-right: 5px;" />
			</div>
		</div>
	</div>
</header>
