<script>
	import { onMount } from 'svelte';

	// Dữ liệu flashcards (lấy từ API hoặc dữ liệu tĩnh)
	let flashcards = [
		{ id: 1, word: 'Mèo', image: '/static/images/meo.jpg', video: '/static/videos/meo.mp4' },
		
	];

	// Theo dõi trạng thái lật của từng thẻ
	let flipped = new Set();

	const flipCard = (id) => {
		if (flipped.has(id)) {
			flipped.delete(id);
		} else {
			flipped.add(id);
		}
	};
</script>

<div class="fc">
	<h1>Bộ Thẻ Ghi Nhớ</h1>
	
	<div class="cards">
		{#each flashcards as card (card.id)}
			<div class="card" on:click={() => flipCard(card.id)}>
				{#if flipped.has(card.id)}
					<div class="back">
						<video src={card.video} autoplay loop muted></video>
					</div>
				{:else}
					<div class="front">
						<img src={card.image} alt={card.word} />
						<p>{card.word}</p>
					</div>
				{/if}
			</div>
		{/each}
	</div>
</div>

<style>
	.cards {
		display: flex;
		flex-wrap: wrap;
		gap: 20px;
		justify-content: center;
		padding: 20px;
	}

	.card {
		width: 200px;
		height: 300px;
		perspective: 1000px;
		cursor: pointer;
	}

	.front,
	.back {
		width: 100%;
		height: 100%;
		position: absolute;
		backface-visibility: hidden;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		border: 1px solid #ccc;
		box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
		transition: transform 0.6s;
	}

	.front {
		background-color: #f9f9f9;
	}

	.back {
		transform: rotateY(180deg);
		background-color: #e0e0e0;
	}

	.card:hover .front {
		transform: rotateY(180deg);
	}

	.card:hover .back {
		transform: rotateY(0);
	}

	img {
		max-width: 100%;
		height: auto;
		margin-bottom: 10px;
	}

	video {
		max-width: 100%;
		height: auto;
	}
</style>
