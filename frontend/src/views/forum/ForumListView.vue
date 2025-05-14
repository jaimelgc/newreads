<script setup lang="ts">
    import { ref, onMounted } from 'vue';
    import { useRouter } from 'vue-router';
    import axios from 'axios';

    interface Post {
        id: number;
        title: string;
        poster: { username: string } | null;
        created_at: string;
    }

    const posts = ref<Post[]>([]);
    const router = useRouter();

    onMounted(async () => {
        const response = await axios.get('/api/posts/?ordering=-created_at&limit=20');
        posts.value = response.data;
    });

    const goToPost = (id: number) => {
        router.push({ name: 'ForumDetail', params: { id } });
    };
</script>

<template>
  <div>
    <h2>Recent Posts</h2>
    <ul>
      <li v-for="post in posts" :key="post.id" @click="goToPost(post.id)" style="cursor:pointer;">
        <strong>{{ post.title }}</strong> by {{ post.poster?.username || 'Unknown' }} - {{ new Date(post.created_at).toLocaleString() }}
      </li>
    </ul>
  </div>
</template>