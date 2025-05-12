<script setup lang="ts">
import ListForm from '@/components/user/ListForm.vue';
import { useRoute, useRouter } from 'vue-router';
import { onMounted, ref } from 'vue';
import api from '@/api';

const route = useRoute();
const router = useRouter();
const username = route.params.username as string;

const userId = ref<number | null>(null);
const isLoading = ref(true);
const error = ref<string | null>(null);

onMounted(async () => {
  try {
    const res = await api.get(`/user/${username}/`);
    userId.value = res.data.id;
  } catch (err) {
    error.value = 'Failed to fetch user.';
  } finally {
    isLoading.value = false;
  }
});

async function handleSubmit(data: { name: string; description: string; items: any[]; is_public: boolean }) {
  if (!userId.value) return;
  const payload = {
    ...data,
    items: data.items.map(item => ({
      book: item.book.ol_id,
      title: item.title,
    })),
    user: userId.value,
  };
  await api.post(`/user/booklists/`, payload);
  router.push(`/users/${username}/lists`);
}
</script>

<template>
  <div class="max-w-2xl mx-auto mt-10 p-6 bg-white shadow rounded">
    <h1 class="text-2xl font-bold mb-4">Create List</h1>
    <p v-if="error" class="text-red-500 mb-2">{{ error }}</p>
    <ListForm v-if="!isLoading" :onSubmit="handleSubmit" />
  </div>
</template>