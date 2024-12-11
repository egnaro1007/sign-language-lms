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
		<h1>{questionData.question || 'Điền vào chỗ trống'}</h1>
	</div>
	<ul>
		<div class="learning__answer">
            <ul class="learning__items">
                {#if questionData.answerList && questionData.answerList.length > 0}
                    {#each questionData.answerList as item, index}
                        <li class={item === '' ? 'learning__holder' : 'learning__item'}>
                            {#if item.startsWith('video:')}
                                <video 
                                    style="width: 100%; height: auto; max-width: 100%; max-height: 100%;" 
                                    loop 
                                    autoplay
                                >
                                    <source src={item.slice(6)} type="video/mp4">
                                    <track kind="captions" srclang="vi" label="Vietnamese" style="display: none;">
                                </video>
							{:else if item.startsWith('input:')}
								<div class="learning__item">
									<textarea bind:value={userInput} style="width: 100%; height: 100%;"></textarea>
								</div>
                            {:else}
                                {item}
                            {/if}
                        </li>
                    {/each}
                {/if}
            </ul>
        </div>
        <div class="learning__button">
            <button class="learning__submit" on:click={ checkAnswer }>
                {isChecked ? 'Tiếp tục' : 'Kiểm tra'}
            </button>
        </div>
	</ul>
</div>
