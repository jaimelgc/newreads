<script setup lang="ts">
import { ref } from 'vue';
import api from '@/api';

const emit = defineEmits(['submitted']);

const title = ref('');
const content = ref('');
const bookOlId = ref('');
const isSubmitting = ref(false);
const error = ref('');

const submitPost = async () => {
  if (!title.value.trim() || !content.value.trim()) {
    error.value = 'Title and content are required.';
    return;
  }

  isSubmitting.value = true;
  error.value = '';

  try {
    await api.post('/posts/', {
      title: title.value,
      content: content.value,
      book: bookOlId.value || null,
    });

    // Reset form
    title.value = '';
    content.value = '';
    bookOlId.value = '';

    emit('submitted'); // Let parent refresh or navigate
  } catch (err) {
    console.error(err);
    error.value = 'Failed to create post.';
  } finally {
    isSubmitting.value = false;
  }
};
</script>

<template>
  <form @submit.prevent="submitPost" class="bg-white p-6 rounded shadow space-y-4">
    <div>
      <label class="block mb-1 font-semibold">Title</label>
      <input
        v-model="title"
        type="text"
        class="w-full p-2 border border-gray-300 rounded"
        placeholder="Post title"
      />
    </div>

    <div>
      <label class="block mb-1 font-semibold">Content</label>
      <textarea
        v-model="content"
        rows="6"
        class="w-full p-2 border border-gray-300 rounded resize-none"
        placeholder="Write your post..."
      ></textarea>
    </div>

    <div>
      <label class="block mb-1 font-semibold">Book OpenLibrary ID (optional)</label>
      <input
        v-model="bookOlId"
        type="text"
        class="w-full p-2 border border-gray-300 rounded"
        placeholder="e.g. OL123M"
      />
    </div>

    <div v-if="error" class="text-red-500 text-sm">{{ error }}</div>

    <button
      type="submit"
      class="bg-green-600 hover:bg-green-700 text-white font-semibold py-2 px-4 rounded"
      :disabled="isSubmitting"
    >
      {{ isSubmitting ? 'Posting...' : 'Post' }}
    </button>
  </form>
</template>