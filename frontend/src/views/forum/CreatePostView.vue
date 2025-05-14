<script setup lang="ts">
  import { ref, computed } from 'vue';
  import axios from 'axios';
  import { useRouter, useRoute } from 'vue-router';

  const title = ref('');
  const content = ref('');
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
      await axios.post('/api/posts/', {
        title: title.value,
        content: content.value,
        ol_id: null  // Optional: you can wire this to a selected book
      });
      router.push({ name: 'ForumList' });
    } catch (error) {
      console.error(error);
    }
  };
</script>

<template>
  <div>
    <h2>Create New Post</h2>
    <form @submit.prevent="submitPost">
      <div>
        <label>Title:</label>
        <input v-model="title" required />
      </div>
      <div>
        <label>Content:</label>
        <textarea v-model="content" required></textarea>
      </div>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>