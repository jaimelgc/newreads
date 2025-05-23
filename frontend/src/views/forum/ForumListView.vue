<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import Posts from '@/components/forum/Posts.vue';
import api from '@/api';
import { useAuthStore } from '@/stores/auth';
import { storeToRefs } from 'pinia';

interface Post {
  id: number;
  title: string;
  content: string;
  poster: { username: string } | null;
  created_at: string;
  comments: []
  book: number
}

const route = useRoute();
const router = useRouter();

const auth = useAuthStore()
const { isLoggedIn, user } = storeToRefs(auth);


const searchTerm = ref(route.query.q as string || '');
const posts = ref<Post[]>([]);
const isLoading = ref(false);
const error = ref<string | null>(null);

const fetchPosts = async () => {
  try {
    isLoading.value = true;
    error.value = null;

    const endpoint = searchTerm.value.trim()
      ? `/forum/posts/?search=${searchTerm.value}&field=title`
      : `/forum/posts/?ordering=-created_at`;

    console.log('Fetching posts from:', endpoint);

    const response = await api.get(endpoint);
    console.log('API Response:', response.data); 

    posts.value = response.data;

    // const bookPost = response.data.find((post: any) => post.book !== null);
    // if (bookPost) {
    //   const bookResponse = await api.get(`/library/books/${bookPost.value}/`);
    // }
    // console.log('bookResponse', bookResponse.value.id)

  } catch (err: any) {
    console.error('Error fetching posts:', err);
    error.value = err.message || 'Error loading posts';
  } finally {
    isLoading.value = false;
  }
};

const goToNewPost = () => {
  router.push(`/${user.value?.username}/forum/new`);
};

onMounted(() => {
  fetchPosts();
});

const search = () => {
  router.replace({ query: { q: searchTerm.value } });
  fetchPosts();
};

const onEnter = (e: KeyboardEvent) => {
  if (e.key === 'Enter') {
    search();
  }
};
</script>

<template>
  <div>
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-4 ml-6 mr-6">

      <div class="flex flex-grow gap-2">
        <input
          v-model="searchTerm"
          @keydown="onEnter"
          placeholder="browse posts..."
          class="mt-4 border border-gray-300 rounded px-4 py-2 w-full"
        />
        <button
          @click="search"
          class="mt-4 px-6 py-2 border border-blue-500 text-blue-500 hover:bg-blue-500 hover:text-white rounded-lg text-sm transition"
        >
          Search
        </button>
      </div>
      <button
        @click="goToNewPost"
        class="mt-4 px-4 py-2 bg-secondary-default text-white rounded hover:bg-green-700 transition"
      >
        + New Post
      </button>
      <!-- <div class="min-h-screen bg-background p-6 rounded-lg text-center ">
        <h2 class="text-2xl font-semibold mb-2 text-secondary-light">Search for posts by title</h2>
        <p class="text-xl text-gray-200">Join the conversation about your favorite reads</p>
      </div> -->
    </div>
    <Posts
      :results="posts"
      :isLoading="isLoading"
      :limit="12"
      :method="searchTerm ? 'Search Results' : 'Latest Posts'"
    />

    <div v-if="!isLoading && !posts.length" class="text-center text-gray-500 p-4">
      No posts found. Try a different search.
    </div>
  </div>
</template>
