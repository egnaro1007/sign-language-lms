<script>
	import { onMount } from 'svelte';

	export let questionData = {};
	export let finishQuestion = () => {};
	let isChecked = false;

	let shuffledAnswer = {};
	let shuffledKey = {};

	let leftRefs = [];
	let rightRefs = [];

	let matches = [];
	let selectedItem = null;
	let cursorPosition = { x: 0, y: 0 };

	function listToDict(list) {
		let originalDict = {};
		list.forEach((item, index) => {
			originalDict[item] = index;
		});

		const shuffledDict = Object.fromEntries(
			Object.entries(originalDict).sort(() => Math.random() - 0.5)
		);

		return shuffledDict;
	}

	function updatePositions() {
		leftRefs = leftRefs.map((ref) => ref.getBoundingClientRect());
		rightRefs = rightRefs.map((ref) => ref.getBoundingClientRect());
	}

	function updateCursorPosition(event) {
		cursorPosition = {
			x: event.clientX - 75,
			y: event.clientY - 70
		};
	}

	function handleItemClick(item, column) {
		// If the item is already matched, deselect it
		if (matches.some((match) => match[column] === item)) {
			selectedItem = null;
			return;
		}

		// If no item is selected, select the current item
		if (!selectedItem) {
			selectedItem = { item, column };
			return;
		}

		// Have selected item
		// If the new item is in the same column as the selected item, deselect the selected item
		if (selectedItem.column === column) {
			selectedItem = null;
			return;
		}
		// Push to matches list
		matches.push({
			[column]: item,
			[column === 'left' ? 'right' : 'left']: selectedItem.item
		});

		// console.log(matches);

		matches = [...matches];

		selectedItem = null;
	}

	function checkAnswer() {
		if (!isChecked) {
			isChecked = true;
			for (let match of matches) {
				if (match.left !== match.right) {
					finishQuestion(-1);
					return;
				}
			}
			finishQuestion(10);
		} else {
			isChecked = false;
			finishQuestion();
		}
	}

	onMount(() => {
		shuffledAnswer = listToDict(questionData.answerList);
		shuffledKey = listToDict(questionData.key);
		updatePositions();
		window.addEventListener('mousemove', updateCursorPosition);
		window.addEventListener('keydown', (event) => {
			if (event.key === 'Escape') {
				selectedItem = null;
			}
		});
	});
</script>

<div>
	<div class="learning__header">
		<h1>{questionData.question || 'Nối các từ với thể hiện của chúng'}</h1>
	</div>
	<div class="learning__matching">
		<div>
			{#each Object.entries(shuffledAnswer) as [key, value]}
				<div>
					<button bind:this={leftRefs[value]} on:click={() => handleItemClick(value, 'left')}>
						{key}
					</button>
				</div>
			{/each}
		</div>
		<div style="max-height: 100%;">
			{#each Object.entries(shuffledKey) as [key, value]}
				<div style="height: 100px;">
					<button
						bind:this={rightRefs[value]}
						on:click={() => handleItemClick(value, 'right')}
						style="width: 100%; height: 100%;"
					>
						{#if key.startsWith('video:')}
							<video
								style="width: auto; height: auto; max-width: 100%; max-height: 100%;"
								loop
								autoplay
							>
								<source src={key.slice(6)} type="video/mp4" />
								<track kind="captions" srclang="vi" label="Vietnamese" style="display: none;" />
							</video>
						{:else}
							{key}
						{/if}
					</button>
				</div>
			{/each}
		</div>
	</div>
	<div class="learning__button">
		<button class="learning__submit" on:click={checkAnswer}>
			{isChecked ? 'Tiếp tục' : 'Kiểm tra'}
		</button>
	</div>
	<div>
		<svg
			style="pointer-events: none; position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
		>
			{#each matches as match}
				<line
					x1={leftRefs[match.left].offsetLeft + leftRefs[match.left].offsetWidth}
					y1={leftRefs[match.left].offsetTop + leftRefs[match.left].offsetHeight / 2}
					x2={rightRefs[match.right].offsetLeft}
					y2={rightRefs[match.right].offsetTop + rightRefs[match.right].offsetHeight / 2}
					stroke="red"
					stroke-width="2"
				/>
			{/each}
			{#if selectedItem && selectedItem.column === 'left'}
				<line
					x1={leftRefs[selectedItem.item].offsetLeft + leftRefs[selectedItem.item].offsetWidth}
					y1={leftRefs[selectedItem.item].offsetTop + leftRefs[selectedItem.item].offsetHeight / 2}
					x2={cursorPosition.x}
					y2={cursorPosition.y}
					stroke="blue"
					stroke-width="2"
				/>
			{:else if selectedItem && selectedItem.column === 'right'}
				<line
					x1={cursorPosition.x}
					y1={cursorPosition.y}
					x2={rightRefs[selectedItem.item].offsetLeft}
					y2={rightRefs[selectedItem.item].offsetTop +
						rightRefs[selectedItem.item].offsetHeight / 2}
					stroke="blue"
					stroke-width="2"
				/>
			{/if}
		</svg>
	</div>
</div>
