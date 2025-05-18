<script setup lang="ts">
    import { defineProps, computed, watchEffect } from 'vue';
    import api from '@/api';

    interface UserType {
        id: number;
        username: string;
        profile_picture: string;
    }

    interface BookDetails {
        id: number;
        ol_id: string;
        title: string;
        author_name?: string;
        cover_url?: string;
    }

    const props = defineProps<{
        list: {
            id: number;
            name: string;
            description: string;
            author: UserType;
            created_at: string;
            items: {
            id: number;
            book: number;
            added_at: string;
            bookDetails?: BookDetails;
            }[];
        };
    }>();

    async function fetchBookDetails(item: { book: number; bookDetails?: BookDetails }) {
        try {
            const response = await api.get(`/library/books/${item.book}/`);
            item.bookDetails = response.data;
        } catch (error) {
            console.error('Error fetching book details:', error);
        }
    }

    watchEffect(() => {
        if (props.list.items?.length) {
            props.list.items.forEach(item => {
                if (!item.bookDetails) {
                    fetchBookDetails(item);
                }
            });
        }
    });

    const coverUrls = computed(() =>
        props.list.items
            .map(item => item.bookDetails?.cover_url)
            .slice(0, 6)
    );
</script>


<template>
    <div
      class="border-background rounded shadow p-6 bg-background hover:border-blue-300 border-4 flex flex-col items-center text-center"
    >
      <h3 class="text-xl font-semibold mb-1 text-white">{{ list.name }}</h3>
  
      <div class="flex items-center gap-2 mb-2">
        <img
          :src="list.author.profile_picture"
          alt="Profile picture"
          class="w-6 h-6 rounded-full object-cover"
        />
        <p class="text-gray-300 text-sm">{{ list.author.username }}</p>
      </div>
  
      <!-- <p class="text-gray-400 text-sm mb-4">{{ list.description }}</p> -->
  
      <div v-if="coverUrls.length" class="grid grid-cols-3 gap-2 mb-4">
        <img
          v-for="(url, index) in coverUrls"
          :key="index"
          :src="url"
          alt="Book cover"
          class="w-full h-40 object-cover rounded"
        />
      </div>
      <p v-else class="text-gray-400 text-sm mb-4">No books in this list yet.</p>
  
      <RouterLink
        :to="`/users/${list.author.username}/lists/${list.id}`"
        class="h-[36px] border border-green-500 text-green-500 hover:bg-green-500 hover:text-white px-4 py-1.5 rounded-lg text-sm transition"
      >
        Read More
      </RouterLink>
    </div>
</template>
  