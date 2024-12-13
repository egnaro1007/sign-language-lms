<script>
	import Splide from '../../../lib/components/Splide.svelte';
	import { fade } from 'svelte/transition';
	let showAll = false;

	function toggleShowAll() {
		showAll = !showAll;
	}
</script>


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
						<img class="topic-img" src="/images/abc.png" />
						<h3>Bảng chữ cái</h3>
						<div class="stars">
							<img class="star" src="/images/star.png" alt="Star" />
						</div>
					</div>
				</a>
				<a href="/topics/2">
					<div class="dashboard__topic__item">
						<img class="topic-img" src="/images/chat.png" />
						<h3>Giao tiếp</h3>
						<div class="stars">
							<img class="star" src="/images/star.png" alt="Star" />
							<img class="star" src="/images/star.png" alt="Star" />
						</div>
					</div>
				</a>
				<a href="/topics/3">
					<div class="dashboard__topic__item">
						<img class="topic-img" src="/images/family.png" />
						<h3>Gia đình</h3>
						<div class="stars">
							<img class="star" src="/images/star.png" alt="Star" />
							<img class="star" src="/images/star.png" alt="Star" />
						</div>
					</div>
				</a>
				<a href="/topics/4">
						<div class="dashboard__topic__item">
							<img class="topic-img" src="/images/hobby.png" />
							<h3>Sở thích</h3>
							<div class="stars">
								<img class="star" src="/images/star.png" alt="Star" />
								<img class="star" src="/images/star.png" alt="Star" />
							</div>
						</div>
					</a>

				{#if showAll}
					<a href="/topics/5">
					<div class="dashboard__topic__item">
						<img class="topic-img" src="/images/emotional.png" />
						<h3>Cảm xúc</h3>
						<div class="stars">
							<img class="star" src="/images/star.png" alt="Star" />
							<img class="star" src="/images/star.png" alt="Star" />
							<img class="star" src="/images/star.png" alt="Star" />
						</div>
					</div>
				</a>
					<a href="/">
						<div class="dashboard__topic__item">
							<img class="topic-img" src="/images/school.png" />
							<h3>Trường học</h3>
							<div class="stars">
								<img class="star" src="/images/star.png" alt="Star" />
								<img class="star" src="/images/star.png" alt="Star" />
								<img class="star" src="/images/star.png" alt="Star" />
							</div>
						</div>
					</a>
				{/if}
			</div>
		</div>
	</div>
</div>
