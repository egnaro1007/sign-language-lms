<script>
	export let searchPlaceholder = 'Tìm kiếm chủ đề, từ vựng...';
	import {page} from '$app/stores';
	let sign;
	$: sign = $page.params.id;
</script>

<header class="header">
	<div class="container">
		<div class="header__left">
			<a href="/"> <img src="/images/logo.png" alt="Logo" /></a>
			<input type="text" placeholder={searchPlaceholder} style="" />
		</div>
		{#if sign}
			<div class="header__right">
				<h4>Nguyễn Đình Tuấn Anh</h4>
				<img src="/images/userz.png" alt="user" >
			</div>
		{:else}
		<div class="header__right">
			<h4>Đăng nhập</h4>
			<h4>Đăng ký</h4>
		</div>
		{/if}
	</div>
</header>
