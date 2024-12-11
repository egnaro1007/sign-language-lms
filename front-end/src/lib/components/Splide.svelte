<script>
	import { onMount } from 'svelte';
	import Splide from '@splidejs/splide';
	import { fade } from 'svelte/transition';

	let splide;

	onMount(() => {
		splide = new Splide('.splide', {
			type: 'loop', // Slider type: 'loop', 'fade', or 'slide'
			perPage: 1, // Number of slides per view
			autoplay: true, // Enable autoplay
			interval: 3000, // Autoplay interval in ms
			pagination: true // Show pagination
		});

		splide.mount(); // Initialize the slider
	});
</script>

<!-- Splide HTML Structure -->
<div class="splide" out:fade={{ duration: 200 }}>
	<div class="splide__track">
		<ul class="splide__list">
			<li class="splide__slide"><img src="/images/banner1.png" alt="Slide 1" /></li>
			<li class="splide__slide"><img src="/images/banner2.png" alt="Slide 2" /></li>
			<!-- Add more slides as needed -->
		</ul>
	</div>
</div>

<style>
	@import '@splidejs/splide/dist/css/splide.min.css';
	.splide {
		border-radius: 7px;
		overflow: hidden;
	}
</style>
