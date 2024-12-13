<script>
	import { page } from '$app/stores';
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';

	const learningID = $page.params.id;
	let currentIndex = 0;
	let topicData = {};
	let isFlipped = false;

	function toggleCard() {
		isFlipped = !isFlipped;
	}

	function nextCard() {
		currentIndex = Math.min(currentIndex + 1, topicData.flashcards.length - 1);
		isFlipped = false;
	}

	function previousCard() {
		currentIndex = Math.max(currentIndex - 1, 0);
		isFlipped = false;
	}

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
						text: 'e',
						image: '/images/letter-e.png',
						video: 'https://qipedc.moet.gov.vn/videos/D0496.mp4'
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
		console.log(topicData.flashcards[0].text);
	});
</script>

{#if topicData.flashcards}
	<div class="flashcard centered">
		<div class="flashcard__container">
			<div class="flashcard__header">
				<button on:click={goto(`/topics/${learningID}`)}
					><img src="/images/out.png" alt="quaylai" /></button
				>
				<h3>Thẻ {currentIndex + 1}/{topicData.flashcards.length}</h3>
			</div>
			<div class="flashcard__center">
				<div class="flashcard__card" on:click={toggleCard}>
					<div class="flashcard__inner {isFlipped ? 'flipped' : ''}">
						<div class="flashcard__side flashcard__front">
							<img src={topicData.flashcards[currentIndex].image} alt="Trái Đất" />
							<h2>{topicData.flashcards[currentIndex].text}</h2>
						</div>
						<div class="flashcard__side flashcard__back">
							{#key currentIndex}
								<video
									style="width: 100%; height: 100%; object-fit: cover; border-radius: 15px;"
									loop
									autoplay
								>
									<source src={topicData.flashcards[currentIndex].video} type="video/mp4" />
									<track kind="captions" srclang="vi" label="Vietnamese" style="display: none;" />
								</video>
							{/key}
						</div>
					</div>
				</div>
			</div>
			<div class="flashcard__actions">
				<button
					class="flashcard__button flashcard__button--back"
					disabled={currentIndex === 0}
					on:click={previousCard}><img src="/images/back.png" alt="lui" /></button
				>
				<button
					class="flashcard__button flashcard__button--next"
					disabled={currentIndex === topicData.flashcards.length - 1}
					on:click={nextCard}><img src="/images/next.png" alt="tiep" /></button
				>
			</div>
		</div>
	</div>
{/if}
