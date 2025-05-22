<script setup lang="ts">
  import { ref, onMounted } from 'vue';
  import { useRoute } from 'vue-router';
  import api from '@/api';

  interface Comment {
    id: number;
    content: string;
    poster: { username: string } | null;
    created_at: string;
    quoted_post?: Comment | null;
    }

  interface Post {
    id: number;
    title: string;
    content: string;
    poster: { username: string } | null;
    created_at: string;
    comments: Comment[];
  }

  const route = useRoute();
  const post = ref<Post | null>(null);
  const newComment = ref('');
  const quotedCommentId = ref<number | null>(null);

  const fetchPost = async () => {
  const res = await api.get(`/forum/posts/${route.params.id}/`);
    post.value = res.data;
    console.log('post', post.value)
  };

  const submitComment = async () => {
  try {
    await api.post('/forum/comments/', {
      content: newComment.value,
      original_post: post.value?.id,
      quoted_post: quotedCommentId.value,
    });
    newComment.value = '';
    quotedCommentId.value = null;
    await fetchPost();
  } catch (error) {
    console.error(error);
  }
  };

onMounted(fetchPost);
</script>

<template>
  <div v-if="post" class="text-white flex flex-col min-h-screen">
    <div class="bg-gray-800 p-6">
      <h2 class="font-semibold text-2xl">{{ post.title }}</h2>
      <p class="font-semibold text-secondary-light">
        <strong>{{ post.poster?.username || 'Unknown' }}</strong> - {{ new Date(post.created_at).toLocaleString() }}
      </p>
      <p class="mt-4">{{ post.content }}</p>
    </div>

    <div class="flex-1 bg-gray-900 p-6">
      <h3 class="text-xl font-semibold mb-4">Comments</h3>
      <ul>
        <li v-for="comment in post.comments" :key="comment.id" class="mb-6">
          <div class="border border-gray-700 p-4 rounded-lg">
            <p class="font-semibold text-secondary-light">
              <strong>{{ comment.poster?.username || 'Unknown' }}</strong> said:
            </p>
            <p class="mt-2">{{ comment.content }}</p>
            <p class="text-sm text-gray-400 mt-2">
              {{ new Date(comment.created_at).toLocaleString() }}
            </p>
            <button
              @click="quotedCommentId = comment.id"
              class="mt-2 text-blue-400 hover:underline"
            >
              Reply
            </button>

            <div
              v-if="comment.quoted_post"
              class="mt-4 pl-4 border-l-2 border-gray-600 text-sm text-gray-400"
            >
              <small>
                Replying to {{ comment.quoted_post.poster?.username || 'Unknown' }}: "{{ comment.quoted_post.content }}"
              </small>
            </div>
          </div>
        </li>
      </ul>
    </div>
  
    <div class="bg-gray-800 p-6 sticky bottom-0 border border-secondary-light">
      <h4 class="text-lg font-semibold mb-4">Leave a Comment</h4>
      <div v-if="quotedCommentId" class="mb-4">
        <strong>Replying to comment #{{ quotedCommentId }}</strong>
        <button
          @click="quotedCommentId = null"
          class="ml-4 text-red-400 hover:underline"
        >
          Cancel
        </button>
      </div>
      <textarea
        v-model="newComment"
        placeholder="Write your comment..."
        rows="3"
        class="w-full p-2 rounded-lg bg-gray-700 text-white border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-400"
      ></textarea>
      <button
        @click="submitComment"
        class="mt-4 px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600"
      >
        Post Comment
      </button>
    </div>
  </div>
</template>