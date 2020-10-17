import { writable, derived } from 'svelte/store'


export const tagstore = writable([])
export const categorystore = writable ([])
export const latestPosts = writable([])
export const categoryPosts = writable([])
export const tagPosts = writable([])
export const postDetail = writable({})
export const postTitles = derived(latestPosts, ($latestPosts) => $latestPosts.map((item) => {
    return {
        category:item.category,
        title: item.title,
        slug: item.slug,
        id: item.id,
        posted_date: item.posted_date
    }
}))
export const featuredPosts = derived(latestPosts, ($latestPosts)=> $latestPosts.filter((item)=> item.featured==true))