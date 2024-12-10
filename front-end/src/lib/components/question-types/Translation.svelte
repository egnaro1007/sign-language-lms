<script>
	export let questionData = {};
	export let finishQuestion = () => {};
	let isChecked = false;
	let userInput = '';

	$: userInput, checkAnswer();

	function checkAnswer() {
		if (!isChecked) {
			if (userInput === questionData.key[0]) {
				isChecked = true;
				finishQuestion(10);
			}
		} else {
			isChecked = false;
			finishQuestion();
		}
	}
</script>

<div>
	<div class="learning__header">
		<h1>{questionData.question || 'Dịch từ này sang ngôn ngữ ký hiệu'}</h1>
	</div>
	<div class="learning__divider">
			<div class="learning__info centered">
					<h2>{questionData.answerList[0]}</h2>
					<p>{questionData.description}</p>
			</div>
			<div class="learning__camera">
				<textarea bind:value={userInput} style="width: 100%; height: 100%;"></textarea>
			</div>
	</div>
	<div class="learning__button">
		<button class="learning__submit" on:click={checkAnswer}>
			{isChecked ? 'Tiếp tục' : 'Kiểm tra'}
		</button>
	</div>
</div>
