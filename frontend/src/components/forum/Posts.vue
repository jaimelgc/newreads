<script setup lang="ts">
    import Post from './Post.vue';
    import { defineProps, defineEmits } from 'vue';

    interface Post {
        id: number;
        title: string;
        poster: { username: string } | null;
        created_at: string;
    }

    const props = defineProps<{
        posts: Post[];
        username: string;
    }>();

    const emit = defineEmits<{
        (e: 'select', id: number): void;
    }>();
</script>

<template>
    <section class="bg-blue-50 px-4 py-10">
      <div class="container-xl lg:container m-auto">
        <h2 class="text-3xl font-bold text-green-500 mb-6 text-center">Recent Posts</h2>
        
        <RouterLink
          :to="`/${username}/forum/new`"
          class="h-[36px] bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-lg text-center text-sm mb-6 block w-fit mx-auto"
        >
          New Post
        </RouterLink>
  
        <div v-if="posts.length === 0" class="text-center text-gray-500">
          No posts found.
        </div>
  
        <div class="grid grid-cols-1 gap-4">
          <Post
            v-for="post in posts"
            :key="post.id"
            :post="post"
            @click="emit('select', post.id)"
          />
        </div>
      </div>
    </section>
</template>
  
