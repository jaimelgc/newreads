<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import api from '@/api';

const route = useRoute();
const router = useRouter();
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
  items: {
    id: number;
    book: {
      ol_id: string;
      title: string;
      author_name?: string;
      cover_url?: string;
    };
    added_at: string;
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

const deleteList = async () => {
  try {
    await api.delete(`/user/booklists/${listId}/`);
    router.push(`/users/${username}`);
  } catch (error) {
    console.error('Error deleting list:', error);
  }
};
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

      <div class="flex gap-4 mb-6">
        <RouterLink
          :to="`/users/${username}/lists/${listId}/edit`"
          class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 inline-block"
        >
          Edit List
        </RouterLink>
        <button
          @click="deleteList"
          class="px-4 py-2 bg-red-500 text-white rounded hover:bg-red-600"
        >
          Delete List
        </button>
      </div>

      <div v-if="list?.items && list.items.length" class="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div v-for="item in list.items" :key="item.id" class="text-center">
          <img
            :src="item.book.cover_url || 'https://via.placeholder.com/150'"
            class="w-full h-auto rounded"
            alt="Book cover"
          />
          <div class="mt-2 text-sm font-medium">{{ item.book.title }}</div>
          <div class="text-xs text-gray-500">{{ item.book.author_name }}</div>
        </div>
      </div>
      <p v-else>No books in this list yet.</p>
    </div>
  </section>
</template>