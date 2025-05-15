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
    <div
      class="border rounded shadow p-4 bg-white cursor-pointer hover:bg-gray-50"
      @click="$emit('click')"
    >
      <h3 class="text-xl font-semibold">{{ post.title }}</h3>
      <p class="text-gray-600 text-sm">
        by {{ post.poster?.username || 'Unknown' }}
      </p>
      <p class="text-xs text-gray-400">
        {{ new Date(post.created_at).toLocaleString() }}
      </p>
    </div>
</template>
  

  