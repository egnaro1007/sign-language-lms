<script>
	import { page } from '$app/stores';
	import Loading from '$lib/components/Loading.svelte';
	import FillInTheBlank from '$lib/components/question-types/FillInTheBlank.svelte';
	import SentenceRearrangement from '$lib/components/question-types/SentenceRearrangement.svelte';
	import Translation from '$lib/components/question-types/Translation.svelte';

	const learningID = $page.params.id;
	let questions = [];
	let currentIndex = 0;
	let loading = true;

	async function fetchQuestions() {
		loading = true;
		await new Promise((resolve) => setTimeout(resolve, 2000));
		questions = [
			{
				questionID: 1,
				type: 'rearrangement',
				question: 'Sắp xếp câu',
				answerList: ['câu', 'Sắp xếp', 'có nghĩa', 'từ', 'thành']
			},
			{
				questionID: 2,
				type: 'rearrangement',
				question: 'Sắp xếp câu',
				answerList: ['đậu', 'Sắp xếp', 'có nghĩa', 'từ', 'thành']
			},
			{
				questionID: 3,
				type: 'rearrangement',
				question: 'Sắp xếp câu',
				answerList: ['cây', 'Sắp xếp', 'có nghĩa', 'từ', 'thành']
			}
		];
		loading = false;
	}

	function nextQuestion() {
		currentIndex = Math.min(currentIndex + 1, questions.length - 1);
	}

	function previousQuestion() {
		currentIndex = Math.max(currentIndex - 1, 0);
	}
	fetchQuestions();
</script>

<div>
	{#if loading}
		<div
			style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 539.4px;"
		>
			<Loading />
		</div>
	{:else}
		<div class="arrange__count">
			<h3>Câu hỏi:</h3>
			<span>{currentIndex + 1}/{questions.length}</span>
		</div>

		{#if questions[currentIndex].type === 'rearrangement'}
			<SentenceRearrangement questionData={questions[currentIndex]} />
		{:else if questions[currentIndex].type === 'translation'}
			<Translation questionData={questions[currentIndex]} />
		{/if}

		<button on:click={previousQuestion} disabled={currentIndex === 0}>Previous</button>
		<button on:click={nextQuestion} disabled={currentIndex === questions.length - 1}>Next</button>
	{/if}
</div>
