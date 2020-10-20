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
    <h2 class="title is-capitalized has-text-centered">{params.slug}</h2>
    <article class="container">
        {#if $categoryPosts.length > 0}
            <div class="posts">
                {#each $categoryPosts as post}
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
