<script setup lang="ts">
    import { ref, onMounted } from 'vue';
    import { useRouter } from 'vue-router';
    import publicApi from '@/f-api';
    import api from '@/api';

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
        console.log('response', response.data)

        const user = await api.get('/user/profile/');
        username.value = user.data.username
        console.log('user', user)
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
        <strong>{{ post.title }}</strong> by {{ username || 'Unknown' }} - {{ new Date(post.created_at).toLocaleString() }}
      </li>
    </ul>
  </div>
</template>