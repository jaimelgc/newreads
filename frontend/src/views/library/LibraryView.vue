<script setup lang="ts">
  import { ref, onMounted, onActivated } from 'vue';
  import { useRouter } from 'vue-router';
  import Book from '@/components/library/Book.vue';
  import List from '@/components/user/List.vue';
  import Post from '@/components/user/Post.vue';
  import { useSingleFetch } from '@/search';

  const router = useRouter();
  const searchTerm = ref('');

  const search = () => {
    if (searchTerm.value.trim()) {
      router.push({ name: 'SearchView', query: { q: searchTerm.value } });
    }
  };

  const {
    res: featuredBook,
    error: bookError,
    isLoading: bookIsLoading,
    fetchSingle: fetchFeaturedBook,
  } = useSingleFetch();

  const {
    res: featuredList,
    error: listError,
    isLoading: listIsLoading,
    fetchSingle: fetchFeaturedList,
  } = useSingleFetch();

  const {
    res: featuredPost,
    error: postError,
    isLoading: postIsLoading,
    fetchSingle: fetchFeaturedPost,
  } = useSingleFetch();

  onMounted(() => {
    fetchFeaturedBook('library/getbook/OL21419612M/');
  });

  onActivated(() => {
    if (!featuredBook.value) {
      fetchFeaturedBook('library/getbook/OL21419612M/');
    }
  });
</script>

<template>
  <div class="p-4 max-w-6xl mx-auto space-y-4">
    <div class="text-white text-xl font-bold pb-0 mb-0">Search for books, lists and posts</div>
    <div class="flex gap-2 mb-4">
      <input
        v-model="searchTerm"
        placeholder="Search books..."
        class="border border-gray-300 rounded px-4 py-2 w-full"
      />
      <button
        @click="search"
        class="px-6 py-2 border border-blue-500 text-blue-500 hover:bg-blue-500 hover:text-white rounded-lg text-sm transition"
      >
        Search
      </button>
    </div>
    <div class="text-white pt-0">By title, genre or characters</div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 p-4">
      <div
        id="featuredBook"
        class="rounded-lg p-4 hover:shadow-lg transition aspect-square"
      >
        <div class=" font-bold text-2xl text-white">Featured Book</div>
        <div class="border rounded-lg" v-if="!bookError && !bookIsLoading && featuredBook">
          <Book :key="featuredBook.key" :book="featuredBook" />
        </div>
        <div v-else>
          <h1 class="text-center text-gray-500">No book found</h1>
        </div>
      </div>

      <!-- List box -->
      <div
        id="featuredList"
        class="border rounded-lg p-4 hover:shadow-lg transition aspect-square"
      >
        <div v-if="!listError && !listIsLoading && featuredList">
          <List :key="featuredList.key" :book="featuredList" />
        </div>
        <div v-else>
          <h1 class="text-center text-gray-500">No list found</h1>
        </div>
      </div>
    </div>

    <!-- Post full-width box -->
    <div
      id="featuredPost"
      class="border rounded-lg p-4 hover:shadow-lg transition"
    >
      <div v-if="!postError && !postIsLoading && featuredPost">
        <Post
          :key="post.id"
          :post="post"
          @click="emit('select', post.id)"
        />
      </div>
      <div v-else>
        <h1 class="text-center text-gray-500">No post found</h1>
      </div>
    </div>
  </div>
</template>
