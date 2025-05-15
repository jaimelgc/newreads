<script setup lang="ts">
  import { ref, onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  import api from '@/api';
  import Posts from '@/components/forum/Posts.vue';

  interface Post {
    id: number;
    title: string;
    poster: { username: string } | null;
    created_at: string;
  }

  const posts = ref<Post[]>([]);
  const username = ref('');
  const router = useRouter();

  onMounted(async () => {
    const response = await api.get('/forum/posts/?ordering=-created_at&limit=20');
    posts.value = response.data;

    const user = await api.get('/user/profile/');
    username.value = user.data.username;
  });

  const goToPost = (id: number) => {
    router.push({ name: 'PostDetail', params: { id } });
  };
</script>

<template>
  <Posts :posts="posts" :username="username" @select="goToPost" />
</template>