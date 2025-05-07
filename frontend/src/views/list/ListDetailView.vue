<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import api from '@/api';

const route = useRoute();
const listId = route.params.listId;
const username = route.params.username;

const list = ref(null);
const isLoading = ref(true);

onMounted(async () => {
  try {
    const response = await api.get(`/user/${username}/lists/${listId}/`);
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
      <h1 class="text-3xl font-bold mb-4">{{ list.title }}</h1>
      <p class="text-gray-600 mb-2">By {{ list.author.name }}</p>
      <p class="text-sm text-gray-400 mb-4">Created: {{ list.created_at }}</p>

      <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
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
    </div>
  </section>
</template>