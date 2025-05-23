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

interface Book {
  id: number;
  ol_id: string;
  title: string;
  author_name: string | null;
  publish_date: string | null;
  cover_url: string | null;
}

interface Post {
  id: number;
  title: string;
  content: string;
  poster: { username: string } | null;
  created_at: string;
  comments: Comment[];
  book: number | null;
}

const route = useRoute();
const post = ref<Post | null>(null);
const postBook = ref<Book | null>(null);
const newComment = ref('');
const quotedCommentId = ref<number | null>(null);

const fetchPost = async () => {
  const res = await api.get(`/forum/posts/${route.params.id}/`);
  post.value = res.data;

  if (post.value?.book) {
    try {
      const bookRes = await api.get(`/library/books/${post.value.book}/`);
      postBook.value = bookRes.data;
    } catch (err) {
      console.error('Failed to fetch book:', err);
    }
  }
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
  <div v-if="post" class="text-white flex flex-col min-h-screen bg-gray-900">
    <div class="bg-gray-800 p-6 border-b border-gray-700">
      <h2 class="font-semibold text-2xl mb-1">{{ post.title }}</h2>
      <p class="text-secondary-light">
        <strong>{{ post.poster?.username || 'Unknown' }}</strong> - {{ new Date(post.created_at).toLocaleString() }}
      </p>
      <p class="mt-4 text-white whitespace-pre-line">{{ post.content }}</p>
    </div>

    <div v-if="postBook" class="flex gap-6 p-6 bg-gray-850 border-b border-gray-700">
      <RouterLink :to="`/books/${postBook.cover_url}`">
        <img
          v-if="postBook.cover_url"
          :src="postBook.cover_url"
          alt="Book Cover"
          class="w-28 h-auto rounded-lg shadow-md"
        />
      </RouterLink>
      <div>
        <p class="text-white text-md font-semibold">{{ postBook.title }}</p>
        <p class="text-white text-md font-semibold">{{ postBook.author_name || 'Unknown' }}</p>
        <p class="text-white text-md font-semibold">{{ postBook.publish_date || 'N/A' }}</p>
      </div>
    </div>

    <div class="flex-1 p-6 overflow-y-auto">
      <h3 class="text-xl font-semibold mb-4">Comments</h3>
      <ul>
        <li v-for="comment in post.comments" :key="comment.id" class="mb-6">
          <div class="border border-gray-700 p-4 rounded-lg bg-gray-800">
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
                Replying to {{ comment.quoted_post.poster?.username || 'Unknown' }}:
                "{{ comment.quoted_post.content }}"
              </small>
            </div>
          </div>
        </li>
      </ul>
    </div>

    <div class="bg-gray-850 p-4 border-t border-gray-700 sticky bottom-0 z-10">
      <h4 class="text-lg font-semibold mb-2">Leave a Comment</h4>
      <div v-if="quotedCommentId" class="mb-2 text-sm text-gray-400">
        Replying to
        {{
          post?.comments.find(c => c.id === quotedCommentId)?.poster?.username || 'Unknown'
        }}
        <button
          @click="quotedCommentId = null"
          class="ml-2 text-red-400 hover:underline"
        >
          Cancel
        </button>
      </div>
      <textarea
        v-model="newComment"
        placeholder="Write your comment..."
        rows="2"
        class="w-full p-2 rounded bg-gray-700 text-white border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-400"
      ></textarea>
      <div class="flex justify-end mt-2">
        <button
          @click="submitComment"
          class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
        >
          Post Comment
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.bg-gray-850 {
  background-color: #1e1e1e;
}
</style>
