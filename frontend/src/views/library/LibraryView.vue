<script setup lang="ts">
  import { ref, onMounted, onActivated } from 'vue';
  import { useRouter } from 'vue-router';
  import Books from '@/components/library/Books.vue';
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
  <div>
    <input v-model="searchTerm" placeholder="Search books..." />
    <button @click="search">Search</button>
    
    <div id="featuredBook">
      <div v-if="!bookError && !bookIsLoading && featuredBook">
        <Book :key="featuredBook.key" :book="featuredBook" />
      </div>
      <div v-else><h1>hello</h1></div>
    </div>

    <div id="featuredList">
      <div v-if="!listError && !listIsLoading && featuredList">
        <List :key="featuredList.key" :book="featuredList" />
      </div>
    </div>

    <div id="featuredPost">
      <div v-if="!postError && !postIsLoading && featuredPost">
        <Post :key="featuredPost.key" :book="featuredPost" />
      </div>
    </div>
  </div>
</template>