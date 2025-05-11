<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import ListForm from '@/components/user/ListForm.vue';
import api from '@/api';

const route = useRoute();
const router = useRouter();

const initialData = ref<{ title: string; books: any[] } | undefined>(undefined);
const loading = ref(true);
const error = ref<string | null>(null);

onMounted(async () => {
  try {
    const res = await api.get(`/user/${route.params.username}/lists/${route.params.listId}/`);
    initialData.value = {
      title: res.data.title,
      books: res.data.books
    };
  } catch (err) {
    error.value = 'Failed to load list.';
  } finally {
    loading.value = false;
  }
});

async function handleSubmit(data: { title: string; books: any[] }) {
  await api.put(`/user/${route.params.username}/lists/${route.params.listId}/`, data);
  router.push(`/users/${route.params.username}/lists`);
}
</script>

<template>
  <div class="max-w-2xl mx-auto mt-10 p-6 bg-white shadow rounded">
    <h1 class="text-2xl font-bold mb-4">Edit List</h1>
    <div v-if="loading">Loading...</div>
    <div v-else-if="error">{{ error }}</div>
    <ListForm v-else :initialData="initialData" :onSubmit="handleSubmit" />
  </div>
</template>