<script>
	import { page } from '$app/stores';
	import Loading from '$lib/components/Loading.svelte';
    import FillInTheBlank from '$lib/components/question-types/FillInTheBlank.svelte';
    import SentenceRearrangement from '$lib/components/question-types/SentenceRearrangement.svelte';
    import Translation from '$lib/components/question-types/Translation.svelte';
    import MatchingQuestion from '$lib/components/question-types/MatchingQuestion.svelte';
	
	const learningID = $page.params.id;
	let questions = [];
	let currentIndex = 0;
	let loading = true;
	
	let score = 0;
	
	async function fetchQuestions() {
		loading = true;
		await new Promise((resolve) => setTimeout(resolve, 1000));
		questions = [
			{
				questionsID: 0,
                type: 'matching',
                answerList: [
					'sắp xếp',
                    'từ',
                    'tạo thành',
                    'câu đơn'
                ],
                key: [
					'video:https://qipedc.moet.gov.vn/videos/W02931T.mp4',
                    'video:https://qipedc.moet.gov.vn/videos/W03712.mp4',
                    'video:https://qipedc.moet.gov.vn/videos/W00559.mp4',
                    'video:https://qipedc.moet.gov.vn/videos/W00442.mp4'
                ]
            },
			{
				questionID: 1,
				type: 'rearrangement',
				question: 'Sắp xếp câu',
				description: 'Sắp xếp video thành câu',
				answerList: [
					'video:https://qipedc.moet.gov.vn/videos/W00442.mp4',
					'video:https://qipedc.moet.gov.vn/videos/W02931T.mp4',
					'video:https://qipedc.moet.gov.vn/videos/W03712.mp4',
					'video:https://qipedc.moet.gov.vn/videos/W00559.mp4'
				],
				key: [
					'video:https://qipedc.moet.gov.vn/videos/W02931T.mp4',
					'video:https://qipedc.moet.gov.vn/videos/W03712.mp4',
					'video:https://qipedc.moet.gov.vn/videos/W00559.mp4',
					'video:https://qipedc.moet.gov.vn/videos/W00442.mp4'
				]
			},
			{
				questionID: 2,
				description: 'Sắp xếp từ thành câu có nghĩa',
				type: 'rearrangement',
				question: 'Sắp xếp câu',
				answerList: ['câu', 'Sắp xếp', 'có nghĩa', 'từ', 'thành']
			},
			{
				questionID: 3,
				type: 'cloze',
				question: 'Điền từ vào chỗ trống',
				answerList: [
					'video:https://qipedc.moet.gov.vn/videos/W02931T.mp4',
					'video:https://qipedc.moet.gov.vn/videos/W03712.mp4',
					'input:',
					'video:https://qipedc.moet.gov.vn/videos/W00442.mp4'
				],
				key: ['tạo thành']
			},
			{
				questionID: 4,
				type: 'translation',
				question: 'Dịch từ này',
				description: 'Trái Đất là thành tinh chúng ta đang sống',
				answerList: ['Trái Đất'],
				key: ['trái đất']
			},
			{ questionID: 5, type: 'translation' }
		];
		loading = false;
	}

	function nextQuestion() {
		currentIndex = Math.min(currentIndex + 1, questions.length - 1);
	}

	function previousQuestion() {
		currentIndex = Math.max(currentIndex - 1, 0);
	}

	function finishQuestion(amount) {
		if (amount === undefined) {
			nextQuestion();
		} else {
			score += amount;
		}
	}

	fetchQuestions();
</script>

<div>
	<div class="learning__board">
		{#if loading}
			<div class="learning__loading centered">
				<Loading />
			</div>
		{:else}
			<div class="learning__count">
				<h3>Câu hỏi:</h3>
				<span>{currentIndex + 1}/{questions.length}</span>
			</div>

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
                <MatchingQuestion questionData={ questions[currentIndex] } finishQuestion={ (amount) => finishQuestion(amount) }/>        
			{/if}

			<button on:click={previousQuestion} disabled={currentIndex === 0}>Previous</button>
			<button on:click={nextQuestion} disabled={currentIndex === questions.length - 1}>Next</button>
		{/if}
	</div>
	<img src="/images/khunglong.png" alt="khunglong" class="learning__dinosaur" />
	<div class="learning__scoreboard centered">
		<p>Số điểm</p>
		<p>{score}</p>
	</div>
</div>
