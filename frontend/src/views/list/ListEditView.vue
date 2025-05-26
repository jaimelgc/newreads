<script setup lang="ts">
import { computed, ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import ListForm from '@/components/lists/ListForm.vue';
import api from '@/api';

const route = useRoute();
const router = useRouter();
const listId = route.params.listId as string;
const username = route.params.username as string;

const list = ref<{
  name: string;
  description: string;
  items: {
    id: number;
    book: {
      ol_id: string;
      title: string;
      author_name?: string;
      cover_url?: string;
    };
    title?: string;
    added_at: string;
  }[];
  is_public: boolean;
} | null>(null);

const isLoading = ref(true);
const error = ref<string | null>(null);

onMounted(async () => {
  try {
    const response = await api.get(`/user/booklists/${listId}/`);
    list.value = response.data;
  } catch (err) {
    error.value = 'Failed to load list.';
  } finally {
    isLoading.value = false;
  }
});

const initialData = computed(() => {
  if (!list.value) return undefined;

  return {
    name: list.value.name,
    description: list.value.description,
    is_public: list.value.is_public,
    items: list.value.items.map(item => ({
      book: {
        ol_id: item.book.ol_id,
        title: item.book.title,
      },
      title: item.title,
    })),
  };
});

async function handleSubmit(data: { name: string; description: string; items: any[]; is_public: boolean }) {
  try {
    const payload = {
      name: data.name,
      description: data.description,
      items: data.items.map(item => ({
        book: item.book.ol_id,
        title: item.title,
      })),
      is_public: data.is_public,
    };
    await api.put(`/user/booklists/${listId}/`, payload);
    router.push(`/users/${username}/lists/${listId}`);
  } catch (err) {
    error.value = 'Failed to update list.';
  }
}
</script>

<template>
  <div class="min-h-screen max-w-2xl mx-auto p-6 bg-background shadow rounded">
    <h1 class="text-secondary-light mt-10 text-2xl font-bold mb-4">Edit List</h1>
    <div v-if="isLoading" class="font-bold text-white">Loading...</div>
    <div v-else-if="error" class="font-bold text-red-500">{{ error }}</div>
    <ListForm v-else :initialData="initialData" :onSubmit="handleSubmit" />
  </div>
</template>