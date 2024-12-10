<script>
	export let questionData = {};
</script>

<div>
	<div class="learning__header">
		<h1>{questionData.question || 'Điền vào chỗ trống'}</h1>
	</div>
	<ul>
		{#if questionData.answerList && questionData.answerList.length > 0}
			{#each questionData.answerList as answer}
				<li>{answer}</li>
			{/each}
		{/if}
	</ul>
</div>
