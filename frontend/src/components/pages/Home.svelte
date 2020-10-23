<script>
    import { featuredPosts } from "../../stores/postStore.js";
    import { fade } from "svelte/transition";
    let homeImage =
        "https://images.unsplash.com/photo-1565527891433-117833507ed8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80";
</script>

<svelte:head>
    <title>Welcome to Dr Anil Bhattarai's Page</title>
</svelte:head>

<article class="container m-0">
    <div class="hero is-black mx-0">
        <div class="hero-body">
            <div class="container has-text-centered">
                <h2 class="title is-2">Welcome</h2>
                <p class="has-text-warning-dark">A new world awaits, always!</p>
                {#if $featuredPosts.length > 0}
                    <div class="posts container ">
                        <h2 class="title has-text-centered my-4">
                            Featured Posts
                        </h2>
                        {#each $featuredPosts as post}
                            <div class="card my-2 has-text-left">
                                <div class=" is-mobile">
                                    {#if post.imageurl}
                                        <div class="card-image">
                                            <figure
                                                class="image"
                                                transition:fade>
                                                <img
                                                    src={post.imageurl}
                                                    alt="" />
                                            </figure>
                                        </div>
                                    {:else if post.image}
                                        <div class="card-image ">
                                            <figure
                                                class="image"
                                                transition:fade>
                                                <img src={post.image} alt="" />
                                            </figure>
                                        </div>
                                    {/if}
                                    <div class=" card-content">
                                        <p>
                                            <span
                                                class="is-size-7 is-italic">{new Date(post.posted_date).toDateString()}</span>
                                        </p>
                                        <h3 class="is-size-6 is-italic">
                                            <a
                                                href="#/posts/{post.category.slug}">{post.category.name}</a>
                                        </h3>
                                        <h2 class="is-size-4 title">
                                            <a
                                                href="#/posts/{post.id}/{post.slug}"
                                                class="has-text-black">{post.title}</a>
                                        </h2>

                                        <p
                                            class="is-size-5 is-italic my-6 has-background-light p-2">
                                            {post.summary}
                                            ...
                                            <!-- <a
                                        href="#/posts/{post.id}/{post.slug}"
                                        class="is-link">Read full</a> -->
                                        </p>
                                        <div class="content">
                                            {@html post.content}
                                        </div>
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
            </div>
        </div>
    </div>
</article>
