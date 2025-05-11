<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import api from '@/api';

const route = useRoute();
const listId = route.params.listId;
const username = route.params.username;

const list = ref<{
  id: number;
  name: string;
  description: string;
  author: {
    id: number;
    username: string;
    profile_picture: string;
  };
  created_at: string;
  books: {
    key: string;
    title: string;
    author_name?: string[];
    first_publish_year?: number;
    cover_i?: number;
    publishers?: string[];
    number_of_pages?: number;
    by_statement?: string;
    cover_edition_key?: string;
  }[];
} | null>(null);

const isLoading = ref(true);

onMounted(async () => {
  try {
    const response = await api.get(`/user/booklists/${listId}/`);
    list.value = response.data;
  } catch (error) {
    console.error('Error fetching list:', error);
  } finally {
    isLoading.value = false;
  }
});
</script>

<template>
  <section v-if="!isLoading" class="py-10 px-6 bg-white">
    <div class="max-w-4xl mx-auto">
      <h1 class="text-3xl font-bold mb-4">{{ list?.name }}</h1>
      <p class="text-gray-600 mb-2">By 
        {{ list?.author.username }}
        <img
          :src="list?.author.profile_picture"
          alt="Author profile picture"
          class="inline-block w-6 h-6 rounded-full object-cover mr-2"
        />
      </p>
      <p class="text-sm text-gray-400 mb-4">Created: {{ list?.created_at }}</p>
      <p class="text-gray-700 mb-6">{{ list?.description }}</p>

      <div v-if="list?.books && list.books.length" class="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div v-for="book in list.books" :key="book.key" class="text-center">
          <img
            :src="book.cover_i
              ? `https://covers.openlibrary.org/b/id/${book.cover_i}-M.jpg`
              : 'https://via.placeholder.com/150'"
            class="w-full h-auto rounded"
            alt="Book cover"
          />
          <div class="mt-2 text-sm font-medium">{{ book.title }}</div>
        </div>
      </div>
      <p v-else>No books in this list yet.</p>
    </div>
  </section>
</template>