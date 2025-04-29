<script setup lang="ts">
    import { defineProps, ref, computed } from 'vue';
    import axios from 'axios'

    const props = defineProps<{
        book: {
            title: string;
            author_name?: string[];
            first_publish_year?: number;
            cover_i?: number;
        };
    }>();

    
    const coverUrl = props.book.cover_i
    ? `https://covers.openlibrary.org/b/id/${props.book.cover_i}-M.jpg`
    : 'https://via.placeholder.com/150';

    // og JS
    
    // const props = defineProps({
    //     book: Object
    // })


    // full description
   
    // const showFullDescription = ref(false)

    // const toggleFullDescription = () => {
    //     showFullDescription.value = !showFullDescription.value
    // }

    // const truncateDescription = computed(() => {
    //     let description = props.book.description;
    //     if (!showFullDescription.value) {
    //         description = description.substring(0,90) + '...';
    //     }
    //     return description;
    // });

</script>

<template>
    <div class="border rounded shadow p-4 bg-white">
        <img :src="coverUrl" alt="Book Cover" class="mb-4" />
        <h3 class="text-xl font-semibold">{{ book.title }}</h3>
        <p class="text-gray-600">by {{ book.author_name?.join(', ') || 'Unknown' }}</p>
        <p class="text-sm text-gray-500">First published: {{ book.first_publish_year || 'N/A' }}</p>
    </div>
    
    <!-- <div class="bg-white rounded-xl shadow-md relative">
        <div class="p-4">
            <div class="mb-6">
                <div class="text-gray-600 my-2">{{ book.title }}</div>
            </div>
            <div class="mb-5">
                {{ truncateDescription }}
                <button @click="toggleFullDescription" class="text-green-500 hover:text-green-600">
                    {{ showFullDescription ? 'See Less' : 'See More' }}
                </button>
            </div>
            <RouterLink :to="'library/books/' + book.id" class="h-[36px] bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-lg text-center text-sm">
                Read More
            </RouterLink>
        </div>
    </div> -->
</template>