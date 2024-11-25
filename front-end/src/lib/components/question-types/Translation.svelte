<script>
    export let questionData = {};
</script>

<div>
    <h1>{questionData.question || 'Dịch từ này'}</h1>
    <ul>
        <li>{questionData.answerList && questionData.answerList.length > 0 ? questionData.answerList[0] : ''}</li>
    </ul>
</div>
