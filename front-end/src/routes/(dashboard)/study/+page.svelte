<script>
	import Splide from "../../../lib/components/Splide.svelte";

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
		<Splide />
		<div class="dashboard__topic">
			<div class="dashboard__topic--heading">
				<h2>Chủ đề học tập</h2>
				<h3>Tất cả</h3>
			</div>
			<div class="dashboard__topic--list">
				<a href="/topic">
					<div class="dashboard__topic__item">
						<img src="/images/topic.png" />
						<h3>Giao tiếp cơ bản</h3>
					</div>
				</a>
				<a href="/learning/1">
					<div class="dashboard__topic__item">
						<img src="/images/topic.png" />
						<h3>Gia đình</h3>
					</div>
				</a>
				<a href="/">
					<div class="dashboard__topic__item">
						<img src="/images/topic.png" />
						<h3>Các hành tinh</h3>
					</div>
				</a>
				<a href="/">
					<div class="dashboard__topic__item">
						<img src="/images/topic.png" />
						<h3>Các hành tinh</h3>
					</div>
				</a>
			</div>
		</div>
	</div>
</div>