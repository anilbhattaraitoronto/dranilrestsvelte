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
                        <div class="column card-content">
                            <h3 class="subtitle">
                                <a
                                    href="#/posts/{post.category.slug}">{post.category.name}</a>
                            </h3>
                            <h2 class="title">
                                <a
                                    href="#/posts/{post.id}/{post.slug}">{post.title}</a>
                            </h2>
                            <p class="is-size-7 is-italic my-6">
                                {post.summary}
                            </p>
                            <p class="has-text-right my-3">
                                <a
                                    href="#/posts/{post.id}/{post.slug}"
                                    class="button is-outlined is-link">Read full</a>
                            </p>
                            <p class="has-text-right my-6">
                                <em>Topics: </em>
                                {#each post.tags as tag}
                                    <span class="button is-small">
                                        <a
                                            href="#/tagposts/{tag.slug}"
                                            on:click={() => getTagPosts(tag.id)}>{tag.name}</a></span>
                                {/each}
                            </p>
                            <p class="is-italic is-size-7 has-text-weight-bold">
                                {new Date(post.posted_date).toDateString()}
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
