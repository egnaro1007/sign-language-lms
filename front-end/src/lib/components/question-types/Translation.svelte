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
    <h1>{questionData.question || 'Dịch từ này sang ngôn ngữ ký hiệu'}</h1>
    <div class="arrange__choices">
        <ul class="arrange__items">
            <li class="arrange__item">
                <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%;">
                    <h2>{questionData.answerList[0]}</h2>
                    <p>{questionData.description}</p>
                </div>
            </li>
            <li class="arrange__holder">
                <textarea bind:value={userInput} style="width: 100%; height: 100%;"></textarea>
            </li>
        </ul>
    </div>
    <div class="arrange__button">
        <button class="arrange__submit" on:click={ checkAnswer }>
            {isChecked ? 'Tiếp tục' : 'Kiểm tra'}
        </button>
    </div>
</div>
