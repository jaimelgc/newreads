<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import api from '@/api';
import CommentForm from '@/components/forum/CommentForm.vue';
import { useAuthStore } from '@/stores/auth';

const route = useRoute();
const postId = route.params.id as string;
const authStore = useAuthStore();

const post = ref<any>(null);
const comments = ref<any[]>([]);
const isLoading = ref(true);

onMounted(async () => {
  try {
    const postRes = await api.get(`/posts/${postId}/`);
    post.value = postRes.data;
    const commentRes = await api.get(`/posts/${postId}/comments/`);
    comments.value = commentRes.data;
  } catch (e) {
    console.error('Error loading post:', e);
  } finally {
    isLoading.value = false;
  }
});

function handleCommentPosted(newComment: any) {
  comments.value.push(newComment);
}
</script>

<template>
  <section v-if="!isLoading">
    <div class="container mx-auto p-4 bg-white rounded shadow">
      <h1 class="text-2xl font-bold mb-2">{{ post.title }}</h1>
      <div class="text-gray-700 mb-4">{{ post.content }}</div>
      <div class="text-sm text-gray-400 mb-6">Posted by {{ post.poster?.username }} on {{ post.created_at }}</div>

      <h2 class="text-xl font-semibold mt-6">Comments</h2>
      <div v-if="comments.length === 0" class="text-gray-500">No comments yet.</div>
      <div v-else class="space-y-4 mt-4">
        <div
          v-for="comment in comments"
          :key="comment.id"
          class="border border-gray-200 p-4 rounded"
        >
          <p class="text-gray-800">{{ comment.content }}</p>
          <p class="text-sm text-gray-400 mt-1">By {{ comment.poster?.username }} at {{ comment.created_at }}</p>
          <blockquote
            v-if="comment.quote"
            class="text-sm text-gray-600 italic border-l-4 pl-2 border-gray-300 mt-2"
          >
            "{{ comment.quote }}"
          </blockquote>
        </div>
      </div>

      <div v-if="authStore.user" class="mt-6">
        <h3 class="text-lg font-medium">Leave a Comment</h3>
        <CommentForm :postId="postId" @comment-posted="handleCommentPosted" />
      </div>
    </div>
  </section>
</template>

<style scoped>
.container {
  max-width: 800px;
}
</style>
