<script>
    import { featuredPosts } from "../../stores/postStore.js";
    import { fade } from "svelte/transition";
    let homeImage =
        "https://images.unsplash.com/photo-1565527891433-117833507ed8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80";
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
            <h2 class="title has-text-centered">Featured Posts</h2>
            <div class="posts container ">
                {#each $featuredPosts as post}
                    <div class="card my-2 p-1">
                        <div class="columns  is-mobile">
                            {#if post.thumbnail}
                                <figure class="column is-one-fifth">
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
                                <h3 class="is-size-6 is-italic has-text-black">
                                    <a
                                        href="#/posts/{post.category.slug}">{post.category.name}</a>
                                </h3>
                                <h2 class="is-size-4">
                                    <a
                                        href="#/posts/{post.id}/{post.slug}"
                                        class="has-text-black">{post.title}</a>
                                </h2>

                                <p class="is-size-5 is-italic my-1">
                                    {post.summary.substring(0, 50)}
                                    ...
                                    <a
                                        href="#/posts/{post.id}/{post.slug}"
                                        class="is-link">Read full</a>
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
