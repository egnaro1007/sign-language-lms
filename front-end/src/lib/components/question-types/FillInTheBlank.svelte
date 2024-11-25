<script>
    export let questionData = {};
</script>

<div>
    <h1>{questionData.question || 'Điền vào chỗ trống'}</h1>
    <ul>
        {#if questionData.answerList && questionData.answerList.length > 0}
            {#each questionData.answerList as answer}
                <li>{answer}</li>
            {/each}
        {/if}
    </ul>
</div>
