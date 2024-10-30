<script>
	// import {countdowntimer} from './arrange.js';
	// let count = 10;

	// function countdown() {
	// const interval = setInterval(() => {
	// 	if (count > 0) {
	// 	count -= 1;
	// 	} else {
	// 	clearInterval(interval);
	// 	}
	// }, 1000);
	// }
	// // Call countdown when the component is mounted
	// countdown();

	import { formatTime } from './arrange.js';
	let timeLeft = 600;

	
</script>
<div class="arrange">
	<div class="container">
		<div class="arrange__board">
			<div class="arrange__time">
				<h3>Thời gian còn lại:</h3>
				<span>{formatTime(timeLeft)}</span>

				 
			</div>
			<div class="arrange__count">
				<h3>Câu hỏi:</h3>
				<span>1/10</span>
			</div>
			<div class="arrange__answer">
				<ul class="arrange__items">
					<li class="arrange__holder"></li>
					<li class="arrange__holder"></li>
					<li class="arrange__holder"></li>
					<li class="arrange__holder"></li>
					<li class="arrange__holder"></li>
					<li class="arrange__holder"></li>
				</ul>
			</div>
			<div class="arrange__button">
				<button class="arrange__submit">Xác nhận</button>
			</div>
			<div class="arrange__choices">
				<ul class="arrange__items">
					<li class="arrange__item">thời gian buổi sáng</li>
					<li class="arrange__item">để</li>
					<li class="arrange__item">Tôi thường dành</li>
					<li class="arrange__item">đọc sách.</li>
					<li class="arrange__item">học tiếng việt</li>
					<li class="arrange__item">và</li>
				</ul>
			</div>
		</div>
		<img src="/khunglong.png" alt="khunglong" class="arrange__dinosaur" />
		<div class="arrange__scoreboard"></div>
	</div>
</div>
