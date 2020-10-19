<script>
    import { latestPosts, categoryPosts } from "../../stores/postStore.js";
    export let params = {};
    // let categoryPosts = [];

    latestPosts.subscribe((data) => {
        $categoryPosts = data.filter(
            (item) => item.category.slug == params.slug
        );
    });
</script>

<svelte:head>
    <title>{params.slug} | Dr Anil B</title>
</svelte:head>

<main class="section p-2">
    <h2 class="title">{params.slug}</h2>
    <article class="container">
        {#if $categoryPosts.length > 0}
            <div class="posts">
                {#each $categoryPosts as post}
                    <div class=" columns post card m-2 p-2">
                        {#if post.thumbnail}
                            <figure class="column is-one-fifth">
                                <img
                                    src={post.thumbnail}
                                    alt=""
                                    class="card-image" />
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
                                            href="#/tagposts/{tag.slug}">{tag.name}</a></span>
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
