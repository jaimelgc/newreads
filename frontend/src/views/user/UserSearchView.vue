<script setup lang="ts">
    import { ref, watch } from 'vue';
    import { useRoute, useRouter } from 'vue-router';
    import Users from '@/components/user/Users.vue';
    import { useApiSearch } from '@/search';
    import PulseLoader from 'vue-spinner/src/PulseLoader.vue';

    const route = useRoute();
    const router = useRouter();
    const searchTerm = ref(route.query.q as string || '');

    const { results, error, isLoading, fetchData } = useApiSearch();

    const search = () => {
        if (searchTerm.value.trim()) {
            router.replace({ query: { q: searchTerm.value } });
            fetchData('/user/', {
                search: searchTerm.value,
                field: "username",
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
    <div class="flex gap-2 mb-4 ml-6 mr-6">
      <input
        v-model="searchTerm"
        placeholder="browse users..."
        class="mt-4 border border-gray-300 rounded px-4 py-2 w-full"
      />
      <button
        @click="search"
        class="mt-4 px-6 py-2 border border-blue-500 text-blue-500 hover:bg-blue-500 hover:text-white rounded-lg text-sm transition"
      >
        Search
      </button>
    </div>

    <div v-if="!route.query.q && !isLoading">
      <div class="min-h-screen bg-background p-6 rounded-lg text-center ">
        <h2 class="text-2xl font-semibold mb-2 text-secondary-light">Search for users</h2>
        <p class="text-xl text-gray-200">Search for other users and see their lists and posts.</p>
      </div>
    </div>
    <div v-else>
      <div v-if="isLoading" class="min-h-screen flex flex-col justify-center items-center text-gray-500 py-6">
        <p class="text-3xl font-semibold text-secondary-light">Loading Users</p>
        <PulseLoader />
      </div>
      <div v-else-if="error" class="min-h-screen text-white">{{ error }}</div>
      <div v-else-if="results && results.length" class="min-h-screen">
        <Users :results="results" :isLoading="isLoading" :limit="12" method='Results'/>
      </div>
      <div v-else>
        <p>No users found. Try a different search.</p>
      </div>
    </div>
  </div>
</template>