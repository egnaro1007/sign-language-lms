<script>
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import axios from 'axios';
	import Loading from '$lib/components/Loading.svelte';
	import FillInTheBlank from '$lib/components/question-types/FillInTheBlank.svelte';
	import SentenceRearrangement from '$lib/components/question-types/SentenceRearrangement.svelte';
	import Translation from '$lib/components/question-types/Translation.svelte';
	import MatchingQuestion from '$lib/components/question-types/MatchingQuestion.svelte';

	const learningID = $page.params.id;
	let questions = [];
	let currentIndex = 0;
	let loading = true;
	let bubbleContent = '';

	let score = 0;

	async function fetchQuestions() {
		loading = true;
		console.log('fetching questions');
		try {
			const response = await axios.get('http://127.0.0.1:8000/api/learning/topic/' + learningID);
			questions = response.data.questions;
		} catch (error) {
			console.error(error);
		} finally {
			loading = false;
		}
	}

	function nextQuestion() {
		currentIndex = Math.min(currentIndex + 1, questions.length - 1);
		bubbleContent = '';
	}

	function previousQuestion() {
		currentIndex = Math.max(currentIndex - 1, 0);
		bubbleContent = '';
	}

	function finishQuestion(amount) {
		if (amount === undefined) {
			nextQuestion();

		} else if (amount === -1) {
			bubbleContent = 'Sai rồi!';
			setTimeout(() => {
				bubbleContent = '';
			}, 2000);

		} else {
			bubbleContent = 'Đúng rồi!';
			score += amount;
			setTimeout(() => {
				bubbleContent = '';
			}, 2000);
		}
	}

	onMount(() => {
		fetchQuestions();
	});
</script>

<div>
	<div class="learning__board">
		{#if loading}
			<div class="learning__loading centered">
				<Loading />
			</div>
		{:else}
			<div class="learning__count">
				<h2>Câu:</h2>
				<span>{currentIndex + 1}/{questions.length}</span>
			</div>
			{#key currentIndex}
				{#if questions[currentIndex].type === 'cloze'}
					<FillInTheBlank
						questionData={questions[currentIndex]}
						finishQuestion={(amount) => finishQuestion(amount)}
					/>
				{:else if questions[currentIndex].type === 'rearrangement'}
					<SentenceRearrangement
						questionData={questions[currentIndex]}
						finishQuestion={(amount) => finishQuestion(amount)}
					/>
				{:else if questions[currentIndex].type === 'translation'}
					<Translation
						questionData={questions[currentIndex]}
						finishQuestion={(amount) => finishQuestion(amount)}
					/>
				{:else if questions[currentIndex].type === 'matching'}
					<MatchingQuestion
						questionData={questions[currentIndex]}
						finishQuestion={(amount) => finishQuestion(amount)}
					/>
				{/if}
			{/key}
			
			<!-- <button on:click={previousQuestion} disabled={currentIndex === 0}>Previous</button>
			<button on:click={nextQuestion} disabled={currentIndex === questions.length - 1}>Next</button> -->
		{/if}
	</div>
	{#if bubbleContent}
		<div class="learning__noti">
			<img src="/images/bubble.png" alt="bubble">
			{#if bubbleContent === 'Sai rồi!'}
				<h3 class="text--false">{bubbleContent}</h3>
			{:else}
			<h3 class="text">{bubbleContent}</h3>
			{/if}
		</div>
	{/if}
	<img src="/images/khunglong.png" alt="khunglong" class="learning__dinosaur" />
	<div class="learning__scoreboard centered">
		<p>Điểm</p>
		<p>{score}</p>
	</div>
</div>
