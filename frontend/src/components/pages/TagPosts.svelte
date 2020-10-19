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
    <title>{params.slug.toUpperCase()} | Dr Anil B</title>
</svelte:head>

<main class="section p-2">
    <h2 class="title">{params.slug.toUpperCase()}</h2>
    <article class="container">
        {#if $tagPosts.length > 0}
            <div class="posts">
                {#each $tagPosts as post}
                    <!-- <div class=" columns post card m-2 p-2">
                        {#if post.thumbnail}
                            <figure class="column is-one-fifth">
                                <img
                                    src={post.thumbnail}
                                    alt=""
                                    class="card-image" />
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
                            <p class="is-size-5 is-italic my-6">
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
                    </div> -->
                    <div class="card my-2 p-1">
                        <div class="columns  is-mobile">
                            {#if post.thumbnail}
                                <figure class="column is-one-fourth">
                                    <img
                                        src={post.thumbnail}
                                        alt=""
                                        class="card-image" />
                                </figure>
                            {/if}
                            <div class="column card-content">
                                <p>
                                    <span
                                        class="is-size-7 is-italic">{new Date(post.posted_date).toDateString()}</span>
                                </p>
                                <h3 class="is-size-6 is-italic">
                                    <a
                                        href="#/posts/{post.category.slug}"
                                        class="">{post.category.name}</a>
                                </h3>
                                <h2 class="is-size-4">
                                    <a
                                        href="#/posts/{post.id}/{post.slug}">{post.title}</a>
                                </h2>

                                <p class="is-size-5 is-italic my-1">
                                    {post.summary.substring(0, 50)}
                                    ...
                                </p>
                                <p class="has-text-right my-1">
                                    <a
                                        href="#/posts/{post.id}/{post.slug}"
                                        class="button is-outlined is-link">Read
                                        full</a>
                                </p>
                            </div>
                        </div>
                        <footer class="card-footer">
                            <em class="card-footer-item">Topics: </em>
                            {#each post.tags as tag}
                                <span class="card-footer-item">
                                    <a
                                        href="#/tagposts/{tag.slug}">{tag.name}</a></span>
                            {/each}
                        </footer>
                    </div>
                {/each}
            </div>
        {:else}
            <p>No Posts yet</p>
        {/if}
    </article>
</main>
