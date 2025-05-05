<script setup lang="ts">
    import { defineProps, computed } from 'vue';

    const props = defineProps<{
        edition: {
            key: string; // /works/OL27482W
            title: string;
            author_name?: string[];
            first_publish_year?: number;
            cover_edition_key?: string, 
            cover_i?: number;
            edition_count?: number;
            edition_key?: string[];
        };
    }>();

    const selectedEditionId = computed(() => {
        return props.edition.cover_edition_key || props.edition.edition_key?.[0] || null;
    });
    
    const coverUrl = props.edition.cover_i
    ? `https://covers.openlibrary.org/b/id/${props.edition.cover_i}-M.jpg`
    : 'https://via.placeholder.com/150';

</script>

<template>
    <div class="border rounded shadow p-4 bg-white">
        <img :src="coverUrl" alt="Edition Cover" class="mb-4" />
        <h3 class="text-xl font-semibold">{{ edition.title }}</h3>
        <h3 class="text-xl font-semibold">{{ edition.cover_i }}</h3>
        <h3 class="text-xl font-semibold">{{ edition.cover_edition_key }}</h3>
        <!-- <h3 class="text-xl font-semibold">{{ edition.key }}</h3> -->
        <p class="text-gray-600">by {{ edition.author_name?.join(', ') || 'Unknown' }}</p>
        <p class="text-sm text-gray-500">First published: {{ edition.first_publish_year || 'N/A' }}</p>
        <RouterLink
            v-if="selectedEditionId"
            :to="`/books/${selectedEditionId}`" 
            class="h-[36px] bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-lg text-center text-sm">
            
            Read More
        </RouterLink>
    </div>
</template>