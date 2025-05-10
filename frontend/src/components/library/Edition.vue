<script setup lang="ts">
    import { defineProps, computed } from 'vue';

    const props = defineProps<{
        edition: {
            key: string; // /works/OL27482W
            title: string;
            author_name?: string[];
            first_publish_year?: number;
            publish_date?: string;
            cover_edition_key?: string; 
            cover_i?: number;
            edition_key?: string[];
            authors?: { key: string }[];
            full_title?: string;
            isbn_13?: string[];
            isbn_10?: string[];
            publishers?: string[];
            authors_details?: { [key: string]: string };
        };
    }>();

    const selectedEditionId = computed(() => {
        return props.edition.cover_edition_key || props.edition.edition_key?.[0] || null;
    });

    const authors = computed(() => {
        if (props.edition.authors) {
            return props.edition.authors.map((author) => 
                props.edition.authors_details?.[author.key] || 'Unknown Author'
            ).join(', ');
        }
        return 'Unknown';
    });

    const publishYear = computed(() => {
        return props.edition.first_publish_year || props.edition.publish_date || 'N/A';
    });
    
    const coverUrl = props.edition.cover_i
    ? `https://covers.openlibrary.org/b/id/${props.edition.cover_i}-M.jpg`
    : 'https://via.placeholder.com/150';

</script>

<template>
    <div class="border rounded shadow p-4 bg-white">
        <img :src="coverUrl" alt="Edition Cover" class="mb-4" />
        <h3 class="text-xl font-semibold">{{ edition.title || edition.full_title || 'Untitled' }}</h3>
        <h3 class="text-xl font-semibold">{{ edition.cover_i }}</h3>
        <h3 class="text-xl font-semibold">{{ edition.cover_edition_key }}</h3>
        <!-- <h3 class="text-xl font-semibold">{{ edition.key }}</h3> -->
        <p class="text-gray-600">by {{ authors }}</p>
        <p class="text-sm text-gray-500">Published: {{ publishYear }}</p>
        <RouterLink
            v-if="selectedEditionId"
            :to="`/books/${selectedEditionId}`" 
            class="h-[36px] bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-lg text-center text-sm">
            
            Read More
        </RouterLink>
    </div>
</template>