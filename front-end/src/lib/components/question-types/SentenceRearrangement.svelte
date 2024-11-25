<script>
    export let questionData = {};
</script>

<div>
    <h1>{questionData.question || 'Sắp xếp lại từ thành câu có nghĩa'}</h1>
    <ul>
        {#if questionData.answerList && questionData.answerList.length > 0}
            {#each questionData.answerList as answer}
                <li>{answer}</li>
            {/each}
        {/if}
    </ul>
</div>

