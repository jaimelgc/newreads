<script setup lang="ts">
    import { defineProps, ref, computed } from 'vue';
    import axios from 'axios'

    const props = defineProps<{
        book: {
            key: string; // /works/OL27482W
            title: string;
            author_name?: string[];
            first_publish_year?: number;
            cover_edition_key?: string, 
            cover_i?: number;
            edition_count?: number; // how is this working if books doesn't specify it, does it not matter
            edition_key?: string[];
        };
    }>();

    const selectedEditionId = computed(() => {
        return props.book.cover_edition_key || props.book.edition_key?.[0] || null;
    });
    
    const coverUrl = props.book.cover_i
    ? `https://covers.openlibrary.org/b/id/${props.book.cover_i}-M.jpg`
    : 'https://via.placeholder.com/150';

</script>

<template>
    <div class="border rounded shadow p-4 bg-white">
        <img :src="coverUrl" alt="Book Cover" class="mb-4" />
        <h3 class="text-xl font-semibold">{{ book.title }}</h3>
        <h3 class="text-xl font-semibold">{{ book.cover_i }}</h3>
        <h3 class="text-xl font-semibold">{{ book.cover_edition_key }}</h3>
        <!-- <h3 class="text-xl font-semibold">{{ book.key }}</h3> -->
        <p class="text-gray-600">by {{ book.author_name?.join(', ') || 'Unknown' }}</p>
        <p class="text-sm text-gray-500">First published: {{ book.first_publish_year || 'N/A' }}</p>
        <RouterLink
            v-if="selectedEditionId"
            :to="`/library/books/${selectedEditionId}`" 
            class="h-[36px] bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-lg text-center text-sm">
            
            Read More
        </RouterLink>
    </div>
</template>