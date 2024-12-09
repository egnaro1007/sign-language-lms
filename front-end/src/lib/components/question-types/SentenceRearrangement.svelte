<script>
    export let questionData = {};
    let userInputList = [];
    let originalAnswerList = [];
    let draggedItem = null;
    let dragoverItem = null;


    $: if (questionData.answerList) {
        userInputList = new Array(questionData.answerList.length).fill('');
    }

    $: if (questionData.answerList) {
        originalAnswerList = [...questionData.answerList];
    }

    function handleDragStart(event, listType, index) {
        if (listType[index] === '') return;
        draggedItem = { listType, index };
        // console.log('Drag start:', draggedItem.listType, draggedItem.index); 
        event.dataTransfer.effectAllowed = 'move';
    }

    function handleDragOver(event, listType, index) {
        event.preventDefault();
        dragoverItem = { listType, index };
        // console.log('Drag over:', dragoverItem.listType, dragoverItem.index); 
    }

    function handleDrop(event) {
        event.preventDefault();
        const temp = draggedItem.listType[draggedItem.index];
        draggedItem.listType[draggedItem.index] = dragoverItem.listType[dragoverItem.index];
        dragoverItem.listType[dragoverItem.index] = temp;

        if (draggedItem.listType === userInputList) {
            userInputList = [...userInputList];
        } else if (draggedItem.listType === originalAnswerList) {
            originalAnswerList = [...originalAnswerList];
        }

        if (dragoverItem.listType === userInputList) {
            userInputList = [...userInputList];
        } else if (dragoverItem.listType === originalAnswerList) {
            originalAnswerList = [...originalAnswerList];
        }

        draggedItem = null;
        dragoverItem = null;

        // console.log('Drag drop:', draggedItem.listType, draggedItem.index, dragoverItem.listType, dragoverItem.index);
    }

    function handleDragEnd() {
        draggedItem = null;
    }
</script>

<div>
    <h1>{questionData.question || 'Sắp xếp lại từ thành câu có nghĩa'}</h1>
    <h2>{questionData.description}</h2>
    <ul>
        <div class="arrange__answer">
            <ul class="arrange__items">
                {#if userInputList && userInputList.length > 0}
                    {#each userInputList as item, index}
                        <li 
                            class={item === '' ? 'arrange__holder' : 'arrange__item'} 
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
        <div class="arrange__button">
            <button class="arrange__submit">Xác nhận</button>
        </div>
        <div class="arrange__choices">
            <ul class="arrange__items">
                {#if originalAnswerList && originalAnswerList.length > 0}
                    {#each originalAnswerList as item, index}
                        <li 
                            class={item === '' ? 'arrange__holder' : 'arrange__item'} 
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