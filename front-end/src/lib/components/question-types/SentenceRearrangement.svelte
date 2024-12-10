<script>
    export let questionData = {};
    export let finishQuestion = () => {};
    let userInputList = [];
    let originalAnswerList = [];
    let draggedItem = null;
    let dragoverItem = null;

    let isChecked = false;

    $: if (questionData.answerList) {
        userInputList = new Array(questionData.answerList.length).fill('');
    }

    $: if (questionData.answerList) {
        originalAnswerList = [...questionData.answerList];
    }

    function handleDragStart(event, listType, index) {
        if (listType[index] === '') return;
        draggedItem = { listType, index };
        event.dataTransfer.effectAllowed = 'move';
    }

    function handleDragOver(event, listType, index) {
        event.preventDefault();
        dragoverItem = { listType, index };
    }

    function handleDrop(event) {
        event.preventDefault();
        const temp = draggedItem.listType[draggedItem.index];
        draggedItem.listType[draggedItem.index] = dragoverItem.listType[dragoverItem.index];
        dragoverItem.listType[dragoverItem.index] = temp;

        // Make the assignments reactive
        userInputList = [...userInputList];
        originalAnswerList = [...originalAnswerList];

        // console.log('Drag drop:', draggedItem.listType, draggedItem.index, dragoverItem.listType, dragoverItem.index);

        draggedItem = null;
        dragoverItem = null;
    }

    function handleDragEnd() {
        draggedItem = null;
    }

    function checkAnswer() {
        if (!isChecked) {
            isChecked = true;
            if (userInputList.join(' ') === questionData.key.join(' ')) {
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
        <h1>{questionData.question || 'Sắp xếp lại từ thành câu có nghĩa'}</h1>
        <h3>{questionData.description}</h3>
    </div>
    <ul>
        <div class="learning__answer">
            <ul class="learning__items">
                {#if userInputList && userInputList.length > 0}
                    {#each userInputList as item, index}
                        <li 
                            class={item === '' ? 'learning__holder' : 'learning__item'} 
                            draggable={userInputList[index] !== ''}
                            on:dragstart={(event) => handleDragStart(event, userInputList, index)}
                            on:dragend={handleDragEnd}
                            on:dragover={(event) => handleDragOver(event, userInputList, index)}
                            on:drop={(event) => handleDrop(event)}
                        >
                            {#if item.startsWith('video:')}
                                <video 
                                    style="width: 100%; height: auto; max-width: 100%; max-height: 100%;" 
                                    loop 
                                    autoplay
                                >
                                    <source src={item.slice(6)} type="video/mp4">
                                    <track kind="captions" srclang="vi" label="Vietnamese" style="display: none;">
                                </video>
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
        <div class="learning__choices">
            <ul class="learning__items">
                {#if originalAnswerList && originalAnswerList.length > 0}
                    {#each originalAnswerList as item, index}
                        <li 
                            class={item === '' ? 'learning__holder' : 'learning__item'} 
                            draggable={originalAnswerList[index] !== ''}
                            on:dragstart={(event) => handleDragStart(event, originalAnswerList, index)} 
                            on:dragend={handleDragEnd}
                            on:dragover={(event) => handleDragOver(event, originalAnswerList, index)}
                            on:drop={(event) => handleDrop(event)}
                        >
                            {#if item.startsWith('video:')}
                                <video 
                                    style="width: 100%; height: auto; max-width: 100%; max-height: 100%;" 
                                    loop 
                                    autoplay
                                >
                                    <source src={item.slice(6)} type="video/mp4">
                                    <track kind="captions" srclang="vi" label="Vietnamese" style="display: none;">
                                </video>
                            {:else}
                                {item}
                            {/if}
                        </li>
                    {/each}
                {/if}
            </ul>
        </div>
    </ul>
</div>