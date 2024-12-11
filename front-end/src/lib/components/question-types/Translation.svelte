<script>
	import { onMount } from "svelte";

	export let questionData = {};
	export let finishQuestion = () => {};
	let isChecked = false;
	let userInput = '';
	let videoElement;
	let cameraAccessAllowed = false;

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

	async function captureFrameAndSend() {
		if (!cameraAccessAllowed) {
			return;
		}

		const canvas = document.createElement('canvas');
		canvas.width = videoElement.videoWidth;
		canvas.height = videoElement.videoHeight;
		const context = canvas.getContext('2d');
		context.drawImage(videoElement, 0, 0, canvas.width, canvas.height);
	
		  canvas.toBlob(async (blob) => {
			if (!blob) {
			console.error('Failed to create Blob');
			return;
			}
	
			try {
				const formData = new FormData();
				formData.append('file', blob, 'frame.jpg');
			
				const response = await fetch('http://127.0.0.1:8001/api/detect', {
					method: 'POST',
					body: formData
				});
			
				const result = await response.json();
				if (result) {
					userInput = result.sign_language;
				}
			} catch (err) {
				console.error('Error sending frame:', err);
			}
		  }, 'image/jpeg');
	}

	onMount(async () => {
			try {
				const stream = await navigator.mediaDevices.getUserMedia({ video: true });
				videoElement.srcObject = stream;
				cameraAccessAllowed = true;

				setInterval(() => {
					cameraAccessAllowed = (videoElement.srcObject && videoElement.srcObject.active);
					if (cameraAccessAllowed) {
						captureFrameAndSend();
					}
					console.log(userInput);
				}, 1000);
			
			} catch (err) {
				console.error('Error accessing camera: ', err);
			}
  		}
	);

</script>

<div>
	<div class="learning__header">
		<h1>{questionData.question || 'Dịch từ này sang ngôn ngữ ký hiệu'}</h1>
	</div>
	<div class="learning__divider">
			<div class="learning__info centered">
					<h2>{questionData.answerList[0]}</h2>
					<p>{questionData.description}</p>
			</div>
			<div class="learning__camera">
				<!-- <textarea bind:value={userInput} style="width: 100%; height: 100%;"></textarea> -->
				<video bind:this={videoElement} autoplay style="width: 100%; height: 100%; transform: scaleX(-1);">
					<track kind="captions" />
				</video>
				<p>{userInput}</p>
			</div>
	</div>
	<div class="learning__button">
		<button class="learning__submit" on:click={checkAnswer}>
			{isChecked ? 'Tiếp tục' : 'Kiểm tra'}
		</button>
	</div>
</div>
