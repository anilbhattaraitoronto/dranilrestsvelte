<script>
    import { latestPosts, postDetail } from "../../stores/postStore.js";
    import { fade } from "svelte/transition";
    export let params = {};

    latestPosts.subscribe((data) => {
        $postDetail = data.find((item) => item.id == params.id);
    });
</script>

<svelte:head>
    <title>{params.slug} | Dr Anil B</title>
</svelte:head>
{#if $postDetail}
    <div class="post card">
        <!-- {#if $postDetail.image}
            <div class="card-image">
                <figure class="image is-4by3">
                    <img src={$postDetail.image} alt="" />
                </figure>
            </div>
        {/if} -->
        {#if $postDetail.imageurl}
            <div class="card-image">
                <figure class="image is-4by3" transition:fade>
                    <img src={$postDetail.imageurl} alt="" />
                </figure>
            </div>
        {:else if $postDetail.image}
            <div class="card-image">
                <figure class="image is-4by3" transition:fade>
                    <img src={$postDetail.imageurl} alt="" />
                </figure>
            </div>
        {/if}
        <div class="card-content">
            <h3 class="subtitle">
                <a
                    href="#/posts/{$postDetail.category.slug}">{$postDetail.category.name}</a>
            </h3>
            <h2 class="title">{$postDetail.title}</h2>
            <p class="is-size-7 is-italic my-6">
                <em>Summary:</em>
                {$postDetail.summary}
            </p>
            <p />
            <div class="content container">
                {@html $postDetail.content}
            </div>
        </div>
        <footer class="card-footer">
            <span card-footer-item>Topics</span>:
            {#each $postDetail.tags as tag}
                <span class="card-footer-item">
                    <a href="#/tagposts/{tag.slug}">{tag.name}</a>
                </span>
            {/each}
        </footer>
    </div>
{:else}
    <p>No post yet</p>
{/if}
