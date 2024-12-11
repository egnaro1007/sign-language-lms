<script>
	import Splide from '../../../lib/components/Splide.svelte';
	import { fade } from 'svelte/transition';
	let showAll = false;

	function toggleShowAll() {
		showAll = !showAll;
	}
</script>

<!-- <div class="lessons">
	<div class="lessons__heading">
		<h1>Học tập</h1>
		<p>Hãy thử sức với các bài học này nhé</p>
	</div>
	<div class="lessons__list">
		<a href="/learning/flashcard">
			<div class="lessons__item lesson__item--left row">
				<img src="assets/images/6268080.png" alt="card" width="80px" class="col-3" />
				<div class="lessons__content col-9">
					<h2>Flashcard</h2>
					<p>Luyện tập từ vựng với những tấm thẻ</p>
				</div>
			</div>
		</a>
		<a href="/learning/1">
			<div class="lessons__item lessons__item--right row">
				<div class="lessons__content col-9">
					<h2>Sắp xếp</h2>
					<p>Sắp xếp các chữ cái để tạo thành câu</p>
				</div>
				<img src="assets/images/6268080.png" alt="card" width="80px" class="col-3" />
			</div>
		</a>
		<a href="/">
			<div class="lessons__item lesson__item--left row">
				<img src="assets/images/6268080.png" alt="card" width="80px" class="col-3" />
				<div class="lessons__content col-9">
					<h2>Sắp xếp</h2>
					<p>Sắp xếp các chữ cái để tạo thành câu</p>
				</div>
			</div>
		</a>
	</div>
</div> -->
<div class="dashboard">
	<div class="container">
		{#if !showAll}
			<Splide />
		{/if}
		<div class="dashboard__topic">
			<div class="dashboard__topic--heading">
				<h2>Chủ đề học tập</h2>
				{#if showAll}
					<button on:click={toggleShowAll}>Thu gọn</button>
				{:else}
					<button on:click={toggleShowAll}>Tất cả</button>
				{/if}
			</div>
			<div class="dashboard__topic--list">
				<a href="/topics/1">
					<div class="dashboard__topic__item">
						<img src="/images/topic com.jpg" />
						<h3>Giao tiếp cơ bản</h3>
					</div>
				</a>
				<a href="/topics/2">
					<div class="dashboard__topic__item">
						<img src="/images/topic family.jpg" />
						<h3>Gia đình</h3>
					</div>
				</a>
				<a href="/topics/3">
					<div class="dashboard__topic__item">
						<img src="/images/topic school.jpg" />
						<h3>Trường học</h3>
					</div>
				</a>
				<a href="/topics/4">
					<div class="dashboard__topic__item">
						<img src="/images/topic weather.jpg" />
						<h3>Thời tiết</h3>
					</div>
				</a>
				{#if showAll}
					<a href="/topics/5">
						<div class="dashboard__topic__item">
							<img src="/images/topic com.jpg" />
							<h3>Giao tiếp cơ bản</h3>
						</div>
					</a>
					<a href="/">
						<div class="dashboard__topic__item">
							<img src="/images/topic family.jpg" />
							<h3>Gia đình</h3>
						</div>
					</a>
					<a href="/">
						<div class="dashboard__topic__item">
							<img src="/images/topic school.jpg" />
							<h3>Trường học</h3>
						</div>
					</a>
				{/if}
			</div>
		</div>
	</div>
</div>
