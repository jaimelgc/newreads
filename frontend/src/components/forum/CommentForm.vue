<script setup lang="ts">
import { ref } from 'vue';
import api from '@/api';
import { useAuthStore } from '@/stores/auth';

const props = defineProps<{
  postId: number;
  onSubmitted: () => void;
}>();

const content = ref('');
const isSubmitting = ref(false);
const error = ref('');

const auth = useAuthStore();

const submitComment = async () => {
  if (!content.value.trim()) {
    error.value = 'Comment cannot be empty.';
    return;
  }

  isSubmitting.value = true;
  error.value = '';

  try {
    await api.post(`/posts/${props.postId}/comments/`, {
      content: content.value,
    });
    content.value = '';
    props.onSubmitted();
  } catch (err: any) {
    error.value = 'Failed to submit comment.';
    console.error(err);
  } finally {
    isSubmitting.value = false;
  }
};
</script>

<template>
  <form @submit.prevent="submitComment" class="bg-white p-4 rounded shadow">
    <textarea
      v-model="content"
      rows="4"
      class="w-full p-2 border border-gray-300 rounded mb-2 resize-none"
      placeholder="Write your comment..."
    ></textarea>
    <div v-if="error" class="text-red-500 text-sm mb-2">{{ error }}</div>
    <button
      type="submit"
      class="bg-green-500 hover:bg-green-600 text-white font-semibold py-2 px-4 rounded"
      :disabled="isSubmitting"
    >
      {{ isSubmitting ? 'Posting...' : 'Post Comment' }}
    </button>
  </form>
</template>