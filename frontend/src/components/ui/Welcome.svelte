<script>
    import { categorystore, postTitles } from "../../stores/postStore.js";
</script>

<div>
    <h2 class="title is-2">Welcome</h2>
    {#each $categorystore as category}
        <h3 class="title is-3">{category.name}</h3>
        {#each $postTitles as item}
            {#if item.category.slug === category.slug}
                <p><a href="#/posts/{item.id}/{item.slug}">{item.title}</a></p>
            {/if}
        {/each}
    {/each}
</div>
