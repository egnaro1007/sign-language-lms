<script>
	import VideoCard from '$lib/components/VideoCard.svelte';

	let isFlipped = false;

	function toggleCard() {
		isFlipped = !isFlipped;
	}
</script>

<div class="flashcard centered">
	<div class="flashcard__container">
		<div class="flashcard__center">
			<div class="flashcard__card" on:click={toggleCard}>
				<div class="flashcard__inner {isFlipped ? 'flipped' : ''}">
					<div class="flashcard__side flashcard__front">
						<img src="/earth.jpg" alt="Trái Đất" />
						<p>Trái Đất</p>
					</div>
					<div class="flashcard__side flashcard__back">
						<VideoCard />
					</div>
				</div>
			</div>
		</div>
		<div class="flashcard__actions">
			<button class="flashcard__button">Thẻ trước</button>
			<button class="flashcard__button">Thẻ sau</button>
		</div>
	</div>
</div>
