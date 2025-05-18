<script setup lang="ts">
    import { ref, watch } from 'vue';
    import { useRoute, useRouter } from 'vue-router';
    import Posts from '@/components/forum/Posts.vue';
    import { useApiSearch } from '@/search';
    import api from '@/api';

    const route = useRoute();
    const router = useRouter();
    const searchTerm = ref(route.query.q as string || '');

    const { results, error, isLoading, fetchData } = useApiSearch();

    const search = (async () => {
    if (searchTerm.value.trim()) {
        router.replace({ query: { q: searchTerm.value } });
        const postsResponse = await api.get(`/forum/posts/?title=${searchTerm.value}`); 
    }});

    watch(
    () => route.query.q,
    (newQuery) => {
        if (newQuery) {
        searchTerm.value = newQuery as string;
        search();
        }
    },
    { immediate: true }
    );
</script>

<template>
  <div>
    <div class="flex gap-2 mb-4 mt-2">
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

    <div v-if="!route.query.q && !isLoading">
      <div class="bg-gray-100 p-6 rounded-lg text-center text-gray-600">
        <h2 class="text-xl font-semibold mb-2">Welcome to the Library</h2>
        <p>Use the search bar above to find books from the Open Library.</p>
      </div>
    </div>
    <div v-else>
      <div v-if="isLoading">Loading...</div>
      <div v-else-if="error">{{ error }}</div>
      <div v-else-if="results && results.length">
        <Books :results="results" :isLoading="isLoading" :limit="12" />
      </div>
      <div v-else>
        <p>No results found. Try a different search.</p>
      </div>
    </div>
  </div>
</template>
