<script>
    import { categorystore } from "../../stores/postStore.js";
</script>

<nav class="navbar container has-shadow">
    <a href="#/" class="navbar-item">Home</a>
    {#if $categorystore.length > 0}
        {#each $categorystore as category}
            <a href="#/posts/{category.slug}" on:click>{category.name}</a>
        {/each}
    {/if}
</nav>
