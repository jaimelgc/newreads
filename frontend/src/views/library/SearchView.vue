<script setup lang="ts">
    import { ref, watch } from 'vue';
    import { useRoute, useRouter } from 'vue-router';
    import Books from '@/components/library/Books.vue';
    import { useApiSearch } from '@/search';

    const route = useRoute();
    const router = useRouter();
    const searchTerm = ref(route.query.q as string || '');

    const { results, error, isLoading, fetchData } = useApiSearch();

    const search = () => {
    if (searchTerm.value.trim()) {
        router.replace({ query: { q: searchTerm.value } });
        fetchData('/api/library/search/', {
        key: `book-search-${searchTerm.value}`,
        url: `https://openlibrary.org/search.json?q=${encodeURIComponent(searchTerm.value)}`,
        });
    }
    };

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
    <div class="flex gap-2 mb-4 mt-2 ml-6 mr-6">
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
      <div
        class="min-h-screen flex items-center justify-center bg-background p-6 rounded-lg text-center "
      >
        <div>
          <h2 class="text-2xl font-semibold mb-2 text-secondary-light">Welcome to the Library</h2>
          <p class="text-xl text-gray-200">Search books by title, author, characters...</p>
        </div>
      </div>
    </div>

    <div v-else>
      <div v-if="isLoading" class="min-h-screen flex items-center justify-center">
        <div class="text-xl text-gray-200">Loading...</div>
      </div>

      <div v-else-if="error">{{ error }}</div>

      <div v-else-if="results && results.length">
        <Books :results="results" :isLoading="isLoading" :limit="12" />
      </div>

      <div v-else class="min-h-screen flex items-center justify-center text-gray-600">
        <p>No results found. Try a different search.</p>
      </div>
    </div>
  </div>
</template>