<script>
    import { latestPosts, tagPosts } from "../../stores/postStore.js";
    import { fade } from "svelte/transition";

    export let params = {};
    latestPosts.subscribe((data) => {
        $tagPosts = data.filter((post) =>
            post.tags.find((item) => item.slug == params.slug)
        );
    });
    function getTagPosts(id) {
        latestPosts.subscribe((data) => {
            $tagPosts = data.filter((post) =>
                post.tags.find((item) => item.id == id)
            );
        });
    }
</script>

<svelte:head>
    <title>{params.slug} | Dr Anil B</title>
</svelte:head>

<main class="section p-2">
    <h2 class="title">{params.slug}</h2>
    <article class="container">
        {#if $tagPosts.length > 0}
            <div class="posts">
                {#each $tagPosts as post}
                    <div class=" columns post card m-2 p-2">
                        {#if post.thumbnail}
                            <figure class="column is-one-fifth">
                                <img
                                    src={post.thumbnail}
                                    alt=""
                                    class="card-image"
                                    transition:fade />
                            </figure>
                        {/if}
                        <div class="column">
                            <h3 class="subtitle">
                                <a
                                    href="#/posts/{post.category.slug}">{post.category.name}</a>
                            </h3>
                            <h2 class="title">
                                <a
                                    href="#/posts/{post.id}/{post.slug}">{post.title}</a>
                            </h2>
                            <p>{post.summary}</p>
                            <p>
                                <a
                                    href="#/posts/{post.id}/{post.slug}"
                                    class="button is-outlined">Read full</a>
                            </p>
                            <p>
                                <em>Topics: </em>
                                {#each post.tags as tag}
                                    <span class="button is-small">
                                        <a
                                            href="#/tagposts/{tag.slug}"
                                            on:click={() => getTagPosts(tag.id)}>{tag.name}</a></span>
                                {/each}
                            </p>
                        </div>
                    </div>
                {/each}
            </div>
        {:else}
            <p>No Posts yet</p>
        {/if}
    </article>
</main>
