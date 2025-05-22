<script setup lang="ts">
  import { defineProps, defineEmits } from 'vue';
  
  interface Post {
    id: number;
    title: string;
    poster: { username: string } | null;
    created_at: string;
  }
  
  defineProps<{ post: Post }>();
  defineEmits(['click']);
</script>

<template>
  <RouterLink
    class="border-white border-t-4 rounded shadow p-6 bg-modal hover:border-blue-300 border-4 flex flex-col text-left cursor-pointer transition-all"
    :to="`/post/${post.id}`"
  >
    <h3 class="text-xl font-semibold mb-1 text-white">{{ post.title }}</h3>
    <p class="text-gray-300 text-sm mb-1">
      by {{ post.poster?.username || 'Unknown' }}
    </p>
    <p class="text-xs text-gray-400">
      {{ new Date(post.created_at).toLocaleString() }}
    </p>
  </RouterLink>
</template>
  

  