<script>
    import { page } from '$app/stores';
    import Loading from '$lib/components/Loading.svelte';

    const learningID = $page.params.id;
    let questions = [];
    let currentIndex = 0;
    let loading = true;
    let selectedAnswers = [];

    async function fetchQuestions() {
        loading = true;
        await new Promise((resolve) => setTimeout(resolve, 500));
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
                answerList: ['đậu', 'Sắp xếp', 'có nghĩa', 'từ', 'thành', 'sẵn sàng']
            },
            {
                questionID: 3,
                type: 'rearrangement',
                question: 'Sắp xếp câu',
                answerList: ['cây', 'Sắp xếp', 'có nghĩa', 'từ', 'thành']
            }
        ];
        selectedAnswers = new Array(questions[currentIndex].answerList.length).fill(null);
        loading = false;
    }

    function nextQuestion() {
        currentIndex = Math.min(currentIndex + 1, questions.length - 1);
        selectedAnswers = new Array(questions[currentIndex].answerList.length).fill(null);
    }

    function previousQuestion() {
        currentIndex = Math.max(currentIndex - 1, 0);
        selectedAnswers = new Array(questions[currentIndex].answerList.length).fill(null);
    }

    function selectAnswer(index) {
		console.log(index);
        const answer = questions[currentIndex].answerList[index];
        const emptyIndex = selectedAnswers.indexOf(null);
        if (emptyIndex !== -1) {
            selectedAnswers[emptyIndex] = answer;
            questions[currentIndex].answerList[index] = null;
        }
    }

    function returnAnswer(index) {
        const answer = selectedAnswers[index];
        if (answer !== null) {
            const emptyIndex = questions[currentIndex].answerList.indexOf(null);
            if (emptyIndex !== -1) {
                questions[currentIndex].answerList[emptyIndex] = answer;
                selectedAnswers[index] = null;
            }
        }
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
        <div class="arrange__time">
            <h3>Thời gian còn lại:</h3>
            <span>10</span>
        </div>
        <div class="arrange__count">
            <h3>Câu hỏi:</h3>
            <span>{currentIndex + 1}/{questions.length}</span>
        </div>

        <!-- Selected Answers (Holders) -->
        <div class="arrange__answer">
            <ul class="arrange__items">
                {#each selectedAnswers as answer, index}
                    <li
                        class="{answer === null ? 'arrange__holder' : 'arrange__item'}"
                        on:click={() => returnAnswer(index)}
                    >
                        {answer}
                    </li>
                {/each}
            </ul>
        </div>

        <!-- Submit Button -->
        <div class="arrange__button">
            <button class="arrange__submit">Xác nhận</button>
        </div>

        <!-- Choices -->
        <div class="arrange__choices">
            <ul class="arrange__items">
                {#each questions[currentIndex].answerList as answer, index}
                    <li
                        class="{answer === null ? 'arrange__holder' : 'arrange__item'}"
                        on:click={() => selectAnswer(index)}
                    >
                        {answer}
                    </li>
                {/each}
            </ul>
        </div>

        <!-- Navigation Buttons -->
        <button on:click={previousQuestion} disabled={currentIndex === 0}>Previous</button>
        <button on:click={nextQuestion} disabled={currentIndex === questions.length - 1}>Next</button>
    {/if}
</div>

