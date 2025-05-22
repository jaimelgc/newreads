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
const bookToAdd = ref<{ ol_id: string; title: string } | null>(null);

onMounted(async () => {
  try {
    const res = await api.get(`/user/${username}/`);
    userId.value = res.data.id;

    if (route.query.book) {
      bookToAdd.value = JSON.parse(route.query.book as string);
    }
  } catch (err) {
    error.value = 'Failed to fetch user.';
  } finally {
    isLoading.value = false;
  }
});

async function handleSubmit(data: { name: string; description: string; is_public: boolean }) {
  if (!userId.value) return;

  try {
    const listResponse = await api.post(`/user/booklists/`, {
      ...data,
      user: userId.value,
    });

    if (bookToAdd.value) {
      await api.post('/user/blitems/', {
        book_list: listResponse.data.id,
        book: bookToAdd.value.ol_id,
      });
    }
    
    router.push(`/users/${username}`);
  } catch (err) {
    error.value = 'Failed to create the list.';
  }
}
</script>

<template>
  <div class="min-h-screen max-w-2xl mx-auto p-6 text-white bg-background shadow rounded">
    <h1 class="text-secondary-light text-2xl font-bold mb-4">Create List</h1>
    <p v-if="error" class="text-red-500 mb-2">{{ error }}</p>

    <div v-if="bookToAdd" class="mx-5 mb-4 p-4 border rounded bg-modal">
      <h2 class="text-lg font-semibold">First Book: {{ bookToAdd.title }}</h2>
    </div>

    <ListForm v-if="!isLoading" :onSubmit="handleSubmit" />
  </div>
</template>