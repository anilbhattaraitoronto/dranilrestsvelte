<script>
    import { featuredPosts } from "../../stores/postStore.js";
    import { fade } from "svelte/transition";
    let homeImage =
        "https://images.unsplash.com/photo-1603035743818-e4e8bb0a0683?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80";
</script>

<svelte:head>
    <title>Welcome to Dr Anil Bhattarai's Page</title>
</svelte:head>

<main>
    <div class="container card">
        <div class="card-image is-3by4">
            <figure class="image" transition:fade>
                <img src={homeImage} alt="" />
            </figure>
        </div>
    </div>
    <article class="container">
        {#if $featuredPosts.length > 0}
            <h2 class="title has-text-centered">Latest Posts</h2>
            <div class="posts container ">
                {#each $featuredPosts as post}
                    <div class="columns m-2 p-2 card">
                        {#if post.thumbnail}
                            <figure transition:fade class="column is-one-fifth">
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
                                <em>Topics: </em>
                                {#each post.tags as tag}
                                    <span class="button is-small">
                                        <a
                                            href="#/tagposts/{tag.slug}">{tag.name}</a></span>
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
