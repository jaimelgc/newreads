<script setup lang="ts">
  import { defineProps, defineEmits, onMounted, ref } from 'vue';
  import api from '@/api';

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
    content: string
    poster: { username: string } | null;
    created_at: string;
    comments: [];
    book: number | null;
  }

  const props = defineProps<{ post: Post }>();
  defineEmits(['click']);

  const postBook = ref<Book | null>(null);

  onMounted(async () => {
    if (props.post.book) {
      try {
        const response = await api.get(`/library/books/${props.post.book}/`);
        postBook.value = response.data;
      } catch (err) {
        console.error('Failed to fetch book:', err);
      }
    }
  });
</script>

<template>
  <RouterLink
    class="block px-4 py-6 border-b border-gray-700 hover:bg-sideground transition-colors"
    :to="`/post/${post.id}`"
  >
    <div class="flex flex-col gap-1 sm:flex-row sm:items-start sm:justify-between sm:gap-6">
      <div class="flex-1">
        <h3 class="text-lg font-semibold text-white hover:underline">{{ post.title }}</h3>
        <p class="text-sm text-gray-400">by {{ post.poster?.username || 'unknown' }}</p>
        <p class="text-xs text-gray-500">{{ new Date(post.created_at).toLocaleString() }}</p>
        <!-- <p class=" text-white">{{ post.content }}</p> -->
        <p class=" text-gray-400">{{ post.comments.length }} comments </p>
      </div>

      <div v-if="postBook" class="flex items-start gap-4 mt-4 sm:mt-0">
        <div>
          <p class="text-white text-sm"><strong>Title:</strong> {{ postBook.title }}</p>
          <p class="text-white text-sm"><strong>Author:</strong> {{ postBook.author_name || 'Unknown' }}</p>
          <p class="text-white text-sm"><strong>Published:</strong> {{ postBook.publish_date || 'N/A' }}</p>
        </div>
        <img
          v-if="postBook.cover_url"
          :src="postBook.cover_url"
          alt="Book Cover"
          class="w-24 h-auto rounded shadow-lg"
        />
      </div>
    </div>
  </RouterLink>
</template>


  