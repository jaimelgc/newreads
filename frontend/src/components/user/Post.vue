<script setup lang="ts">
    import { defineProps, computed } from 'vue';

    interface UserType {
        id: number;
        name: string;
        profile_picture: string;
    }

    interface EditionType {
        key: string;
        title: string;
        author_name?: string[];
        first_publish_year?: number;
        cover_i?: number;
        publishers?: string[];
        number_of_pages?: number;
        by_statement?: string;
        cover_edition_key?: string, 
    }

    interface PostType {
        id: number;
        title: string;
        author: UserType;
        created_at: string;
        book: EditionType;
        comments: PostType[];
    }

    const props = defineProps<{
        post: {
            id: number;
            title: string;
            author: UserType;
            created_at: string;
            book: EditionType;
            comments: PostType[];
        };
    }>();

    // return props.post.comments.length

</script>

<template>
    <div class="border rounded shadow p-4 bg-white">
        <h3 class="text-xl font-semibold">{{ post.title }}</h3>
        <h3 class="text-xl font-semibold">{{ post.author.profile_picture }}</h3>
        <h3 class="text-xl font-semibold">{{ post.author.name }}</h3>
        <h3 class="text-xl font-semibold">{{ post.created_at }}</h3>
        <h3 class="text-xl font-semibold">{{ post.comments.length }}</h3>
        <h3 class="text-xl font-semibold">{{ post.created_at }}</h3>
        <RouterLink
            :to="`/posts/${post.id}`" 
            class="h-[36px] bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-lg text-center text-sm">       
            Read More
        </RouterLink>
    </div>
</template>