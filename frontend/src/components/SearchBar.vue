<script setup lang="ts">
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';

  const searchTerm = ref('');
  const router = useRouter();

  const search = () => {
    if (searchTerm.value.trim()) {
      router.push({ name: 'Search', query: { q: searchTerm.value } });
    }
  };
</script>

<template>
  <div class="search-bar">
    <input
      v-model="searchTerm"
      placeholder="Search books..."
      class="border rounded px-4 py-2"
    />
    <button
      @click="search"
      class="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded ml-2"
    >
      Search
    </button>
  </div>
</template>