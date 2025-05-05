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

    const props = defineProps<{
        list: {
            id: number;
            title: string;
            author: UserType;
            created_at: string;
            books: EditionType[];
        };
    }>();

    const bookPreview = computed(() => {
        return props.list.books
            .slice(0, 5) 
            .map(book => book.cover_edition_key)
            .filter(Boolean); 
    });
    
    const coverUrls = computed(() => {
        return props.list.books
            .slice(0, 5) // limit to 5
            .map(book =>
            book.cover_i
                ? `https://covers.openlibrary.org/b/id/${book.cover_i}-M.jpg`
                : 'https://via.placeholder.com/150'
            );
    });

</script>

<template>
    <div class="border rounded shadow p-4 bg-white">
        <h3 class="text-xl font-semibold">{{ list.title }}</h3>
        <h3 class="text-xl font-semibold">{{ list.author.profile_picture }}</h3>
        <h3 class="text-xl font-semibold">{{ list.author.name }}</h3>
        <h3 class="text-xl font-semibold">{{ list.created_at }}</h3>
        <div v-for="(url, index) in coverUrls" :key="index">
            <img :src="url" alt="Book cover" />
        </div>
        <RouterLink
            :to="`/users/${list.author.name}/lists/${list.id}`" 
            class="h-[36px] bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-lg text-center text-sm">       
            Read More
        </RouterLink>
    </div>
</template>