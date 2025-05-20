<script setup lang="ts">
import { ref, computed } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import api from '@/api';

const title = ref('');
const content = ref('');
const error = ref('');
const isSubmitting = ref(false);
const router = useRouter();

const route = useRoute();
const bookData = computed(() => {
  try {
    return JSON.parse(route.query.book as string);
  } catch {
    return null;
  }
});

const submitPost = async () => {
  try {
    isSubmitting.value = true;
    error.value = '';

    await api.post('/forum/posts/', {
      title: title.value,
      content: content.value,
      ol_id: bookData.value?.ol_id || null
    });

    router.push({ name: 'ForumList' });
  } catch (err) {
    console.error(err);
    error.value = 'Failed to submit post.';
  } finally {
    isSubmitting.value = false;
  }
};
</script>

<template>
  <div class="max-w-2xl mx-auto mt-10 p-6 bg-background">
    <h1 class="text-2xl font-bold mb-4">Create New Post</h1>
    <p v-if="error" class="text-red-500 mb-2">{{ error }}</p>

    <!-- Display book information if provided -->
    <div v-if="bookData" class="mb-4 p-4 border rounded bg-gray-50">
      <h2 class="text-lg font-semibold">Book to Add:</h2>
      <p><strong>Title:</strong> {{ bookData.title }}</p>
      <p><strong>Open Library ID:</strong> {{ bookData.ol_id }}</p>
    </div>

    <form @submit.prevent="submitPost">
      <div class="mb-4">
        <label class="block mb-1 font-medium">Title</label>
        <input
          v-model="title"
          type="text"
          required
          class="border w-full p-2 rounded"
        />
      </div>

      <div class="mb-4">
        <label class="block mb-1 font-medium">Content</label>
        <textarea
          v-model="content"
          required
          rows="6"
          class="border w-full p-2 rounded"
        ></textarea>
      </div>

      <button
        type="submit"
        :disabled="isSubmitting"
        class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 disabled:opacity-50"
      >
        {{ isSubmitting ? 'Submitting...' : 'Submit' }}
      </button>
    </form>
  </div>
</template>