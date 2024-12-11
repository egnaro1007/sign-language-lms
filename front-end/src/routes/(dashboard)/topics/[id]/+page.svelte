<script>
	export let data;

	// Now access the topic from data
	$: topic = data.topic;

	console.log(topic);
</script>

<div class="topic">
	<div class="topic__left">
		<div class="topic__img">
			<img src={topic.img} alt={topic.title} />
		</div>
		<h1>{topic.title}</h1>
		<p>{topic.description}</p>
	</div>
    <div class="topic__right">
        <h2>Vocabulary</h2>
        <ul>
            {#each topic.vocabulary as word}
                <li>{word}</li>
            {/each}
        </ul>
    </div>
</div>
