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
    <div class=" columns post mt-6 p-2">
        {#if $postDetail.imageurl}
            <div class=" column card-image is-one-third">
                <figure class="image is-4by3" transition:fade>
                    <img src={$postDetail.imageurl} alt="" />
                </figure>
            </div>
        {:else if $postDetail.image}
            <div class=" column card-image is-one-third">
                <figure class="image is-4by3" transition:fade>
                    <img src={$postDetail.imageurl} alt="" />
                </figure>
            </div>
        {/if}
        <div class=" column card-content">
            <h3 class="subtitle">
                <a
                    href="#/posts/{$postDetail.category.slug}">{$postDetail.category.name}</a>
            </h3>
            <h2 class="title">{$postDetail.title}</h2>
            <p class="is-size-5 is-italic my-6 has-background-light p-2">
                <em> <strong>Summary:</strong> </em>
                {@html $postDetail.summary}
            </p>
            <p />
            <div class="content container">
                {@html $postDetail.content}
            </div>

            <footer class="card-footer">
                <em class="card-footer-item">Topics:</em>
                {#each $postDetail.tags as tag}
                    <span class="card-footer-item">
                        <a href="#/tagposts/{tag.slug}">{tag.name}</a>
                    </span>
                {/each}
            </footer>
        </div>
    </div>
{:else}
    <p>No post yet</p>
{/if}
