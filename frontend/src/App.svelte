<script>
    import { onMount } from "svelte";
    import Router from "svelte-spa-router";
    import {
        tagstore,
        categorystore,
        latestPosts,
        categoryPosts,
        tagPosts,
        postDetail,
        postTitles,
    } from "./stores/postStore";
    import { user } from "./stores/authStore.js";
    import Navbar from "./components/ui/Navbar.svelte";
    import Home from "./components/pages/Home.svelte";
    import PostDetail from "./components/pages/PostDetail.svelte";
    import CategoryPosts from "./components/pages/CategoryPosts.svelte";
    import TagPosts from "./components/pages/TagPosts.svelte";
    import Footer from "./components/ui/Footer.svelte";
    onMount(() => {
        fetch("postapi/posts/")
            .then((response) => response.json())
            .then((data) => {
                $tagstore = data[0];
                $categorystore = data[1];
                $latestPosts = data[2];
            })
            .catch((err) => console.log("Error is, ", err));
    });
    //

    const routes = {
        "/": Home,
        "/posts/:slug": CategoryPosts,
        "/posts/:id/:slug": PostDetail,
        "/tagposts/:slug": TagPosts,
    };

    let is_active = false;

    function getTagPosts(id) {
        latestPosts.subscribe((data) => {
            $tagPosts = data.filter((post) =>
                post.tags.find((item) => item.id == id)
            );
        });
        is_active == false ? (is_active = true) : (is_active = false);
    }

    function getCategoryPosts(id) {
        latestPosts.subscribe((data) => {
            $categoryPosts = data.filter((post) => post.category.id == id);
        });
        is_active == false ? (is_active = true) : (is_active = false);
    }
    function getPostDetail(id) {
        latestPosts.subscribe((data) => {
            $postDetail = data.find((post) => post.id == id);
        });
    }
    //toggle menu

    function toggleMenu() {
        is_active == false ? (is_active = true) : (is_active = false);
    }
</script>

<style>
    li {
        list-style-type: none;
    }
</style>

<svelte:head>
    <title>Welcome to Dr Anil</title>
</svelte:head>
<main class="section container px-0">
    <nav
        class="navbar container has-shadow  is-link  is-fixed-top has-background-black px-3 ">
        <div class="navbar-brand p-0">
            <a href="#/" class="navbar-item is-size-4 is-white">
                <img
                    src="/static/ab_logo_bw.png"
                    alt=""
                    style="background:white; padding:4px; height:100px;" />
                Home
            </a>
            <span
                class=" navbar-burger burger {is_active ? 'is-active' : ''}"
                on:click={toggleMenu}>
                <span />
                <span />
                <span />
            </span>
        </div>
        <div class="navbar-menu {is_active ? 'is-active' : ''} ">
            <div class="navbar-start" />
            <div class="navbar-end">
                <div class="navbar-item has-dropdown is-hoverable">
                    <span
                        class="navbar-link  is-size-5 is-black has-text-right">Categories</span>
                    <div class="navbar-dropdown p-0">
                        {#if $categorystore.length > 0}
                            {#each $categorystore as category}
                                <a
                                    class=" navbar-item button is-black is-small px-1 py-0  has-text-right mt-1"
                                    href="#/posts/{category.slug}"
                                    on:click={() => getCategoryPosts(category.id)}>{category.name}</a>
                            {/each}
                        {/if}
                    </div>
                </div>
                <div class="navbar-item has-dropdown is-hoverable">
                    <span
                        class="navbar-link is-size-5 is-black has-text-right my-0">Topics</span>
                    <div class="navbar-dropdown p-0 m-0 ">
                        {#if $tagstore.length > 0}
                            {#each $tagstore as item}
                                <a
                                    class="  navbar-item button is-black is-small  is-capitalized px-1 py-0 mt-1 has-text-right"
                                    href="#/tagposts/{item.slug}"
                                    on:click={() => getTagPosts(item.id)}>{item.name}</a>
                            {/each}
                        {/if}
                    </div>
                </div>
            </div>
        </div>
    </nav>
    <div class="container columns m-0 ">
        <div class="container column is-three-quarters px-0 ">
            <Router {routes} />
        </div>
        <div class=" container column p-0" id="cart">
            <div class="hero-body">
                <h2 class="title has-text-centered">Recent</h2>
                {#if $postTitles.length > 0}
                    {#each $postTitles as item}
                        <div>
                            <p class="is-size-7 is-italic">
                                {new Date(item.posted_date).toDateString()}
                                / #{item.category.name}
                            </p>

                            <p>
                                <a
                                    href="#/posts/{item.id}/{item.slug}"
                                    class="has-text-link"
                                    on:click={() => getPostDetail(item.id)}>{item.title}</a>
                            </p>
                            <hr class="my-2" />
                        </div>
                    {/each}
                {/if}
            </div>
        </div>
    </div>
</main>
<Footer />
