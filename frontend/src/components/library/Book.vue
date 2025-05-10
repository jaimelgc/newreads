<script setup lang="ts">
    import { defineProps, computed } from 'vue';
    import { RouterLink } from 'vue-router';

    const props = defineProps<{
        book: {
            title: string;
            author_name?: string | string[];
            publish_date?: string;
            cover_url?: string;
            cover_edition_key?: string;
            cover_i?: number;
            edition_key?: string[];
            key?: string;
            first_publish_year?: number;
        };
    }>();

    const selectedEditionId = computed(() => {
        return props.book.cover_edition_key || props.book.edition_key?.[0] || null;
    });
    
    const coverUrl = computed(() => {
        if (props.book.cover_url) return props.book.cover_url; // From backend
        if (props.book.cover_i) return `https://covers.openlibrary.org/b/id/${props.book.cover_i}-M.jpg`;
        return 'https://via.placeholder.com/150';
    });

</script>

<template>
    <div class="border rounded shadow p-4 bg-white">
        <img :src="coverUrl" alt="Book Cover" class="mb-4" />
        <h3 class="text-xl font-semibold">{{ book.title }}</h3>
        <h3 class="text-xl font-semibold">{{ book.cover_i }}</h3>
        <h3 class="text-xl font-semibold">{{ book.cover_edition_key }}</h3>
        <p class="text-gray-600">{{ Array.isArray(book.author_name) ? book.author_name.join(', ') : book.author_name }}</p>
        <p class="text-sm text-gray-500">First published: {{ book.first_publish_year || book.publish_date || 'N/A' }}</p>
        <RouterLink
            v-if="selectedEditionId"
            :to="`/books/${selectedEditionId}`" 
            class="h-[36px] bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-lg text-center text-sm">
            
            Read More
        </RouterLink>
    </div>
</template>