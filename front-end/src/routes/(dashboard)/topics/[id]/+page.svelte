<script>
	import { page } from '$app/stores';
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';

	const learningID = $page.params.id;

	let topicData = {};
	onMount(() => {
		if (learningID == 1) {
			topicData = {
				id: 1,
				img: '/images/abc.png',
				title: 'Bảng chữ cái',
				description: '',
				flashcards: [
					{
						text: 'a',
						image: '/images/letter-a.png',
						video: 'https://qipedc.moet.gov.vn/videos/D0489.mp4'
					},
					{
						text: 'b',
						image: '/images/letter-b.png',
						video: 'https://qipedc.moet.gov.vn/videos/D0492.mp4'
					},
					{
						text: 'c',
						image: '/images/letter-c.png',
						video: 'https://qipedc.moet.gov.vn/videos/D0493.mp4'
					},
					{
						text: 'd',
						image: '/images/letter-d.png',
						video: 'https://qipedc.moet.gov.vn/videos/D0494.mp4'
					},
					{
						text: 'g',
						image: '/images/letter-g.png',
						video: 'https://qipedc.moet.gov.vn/videos/D0498N.mp4'
					},
					{
						text: 'h',
						image: '/images/letter-h.png',
						video: 'https://qipedc.moet.gov.vn/videos/D0500N.mp4'
					},
					{
						text: 'i',
						image: '/images/letter-i.png',
						video: 'https://qipedc.moet.gov.vn/videos/D0501.mp4'
					},
					{
						text: 'k',
						image: '/images/letter-k.png',
						video: 'https://qipedc.moet.gov.vn/videos/D0502.mp4'
					},
					{
						text: 'l',
						image: '/images/letter-l.png',
						video: 'https://qipedc.moet.gov.vn/videos/D0503.mp4'
					},
					{
						text: 'm',
						image: '/images/letter-m.png',
						video: 'https://qipedc.moet.gov.vn/videos/D0504.mp4'
					}
				]
			};
		} else if (learningID == 2) {
			topicData = {
				id: 2,
				img: '/images/chat.png',
				title: 'Giao tiếp',
				description: 'Chủ đề về giao tiếp hàng ngày',
				flashcards: [
					{
						text: 'Xin chào',
						image: '/images/hello.png',
						video: 'https://qipedc.moet.gov.vn/videos/W00489.mp4'
					},
					{
						text: 'Tên',
						image: '/images/user.png',
						video: 'https://qipedc.moet.gov.vn/videos/W03130N.mp4'
					},
					{
						text: 'Tuổi',
						image: '/images/growth.png',
						video: 'https://qipedc.moet.gov.vn/videos/W02502.mp4'
					},
					{
						text: 'Làm quen',
						image: '/images/conversation.png',
						video: 'https://qipedc.moet.gov.vn/videos/W01925B.mp4'
					},
					{
						text: 'Tạm biệt',
						image: '/images/goodbye.png',
						video: 'https://qipedc.moet.gov.vn/videos/W03075.mp4'
					}
				]
			};
		}
	});
</script>

<div class="topic">
	<div class="topic__left">
		<div class="topic__img">
			<img src={topicData.img} alt={topicData.title} />
		</div>
		<h1>{topicData.title}</h1>
		<p>{topicData.description}</p>
		<div class="topic__buttons">
			<button on:click={goto(`/flashcard/${learningID}`)} class="topic__button"
				><img src="/images/learning.png" alt="hoc" />Học</button
			>
			<button on:click={goto(`/learning/${learningID}`)} class="topic__button"
				><img src="/images/luyentap.png" alt="luyentap" />Luyện tập</button
			>
		</div>
		<div class="topic__mien">
			<button disabled>Miền Bắc</button>
			<button>Miền Nam</button>
		</div>
	</div>
	<div class="topic__right">
		<h2>Danh sách thẻ</h2>
		<div class="topic__list">
			{#each topicData.flashcards as fl}
				<div class="topic__item">
					<div class="topic__item--front">
						<img src={fl.image} alt="flashcard image" />
						<p>{fl.text}</p>
					</div>
					<div class="topic__item--back">
						<video
							style="width: 100%; height: auto; max-width: 100%; max-height: 100%;"
							loop
							autoplay
						>
							<source src={fl.video} type="video/mp4" />
							<track kind="captions" srclang="vi" label="Vietnamese" style="display: none;" />
						</video>
					</div>
				</div>
			{/each}
		</div>
	</div>
</div>
