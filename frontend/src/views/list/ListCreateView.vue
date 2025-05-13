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

    // Extract book data from query parameters
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
    // Create the new list
    const listResponse = await api.post(`/user/booklists/`, {
      ...data,
      user: userId.value,
    });

    // If a book is provided, add it to the newly created list
    if (bookToAdd.value) {
      await api.post('/user/blitems/', {
        book_list: listResponse.data.id,
        book: bookToAdd.value.ol_id,
      });
    }

    // Redirect to the user's lists page
    router.push(`/users/${username}/lists`);
  } catch (err) {
    error.value = 'Failed to create the list.';
  }
}
</script>

<template>
  <div class="max-w-2xl mx-auto mt-10 p-6 bg-white shadow rounded">
    <h1 class="text-2xl font-bold mb-4">Create List</h1>
    <p v-if="error" class="text-red-500 mb-2">{{ error }}</p>

    <!-- Display book information if provided -->
    <div v-if="bookToAdd" class="mb-4 p-4 border rounded bg-gray-50">
      <h2 class="text-lg font-semibold">Book to Add:</h2>
      <p><strong>Title:</strong> {{ bookToAdd.title }}</p>
      <p><strong>Open Library ID:</strong> {{ bookToAdd.ol_id }}</p>
    </div>

    <ListForm v-if="!isLoading" :onSubmit="handleSubmit" />
  </div>
</template>