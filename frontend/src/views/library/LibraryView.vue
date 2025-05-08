<script setup lang="ts">
    import { ref, computed } from 'vue';
    import Books from '@/components/library/Books.vue';
    import Book from '@/components/library/Book.vue';
    import { useApiSearch } from '@/search';
    import { storeToRefs } from 'pinia'
    import { useAuthStore } from '@/stores/auth'

    const auth = useAuthStore()
    const { isLoggedIn, user } = storeToRefs(auth)

    console.log(isLoggedIn.value)
    console.log(user.value)

    const searchTerm = ref('')
    const { results, error, isLoading, fetchData } = useApiSearch()

    const featuredBook = () => {
      const endpoint = '/api/library/search/'
      const params = {
          key: `book-featured`,
          url: `https://openlibrary.org/isbn/9780261103344.json`
      }
      fetchData(endpoint, params)
    }

    const search = () => {
      const endpoint = '/api/library/search/'
      const params = {
          key: `book-search-${searchTerm.value}`,
          url: `https://openlibrary.org/search.json?q=${encodeURIComponent(searchTerm.value)}`
      }
      fetchData(endpoint, params)
    }
</script>

<template>
        <div>
      <input v-model="searchTerm" placeholder="Search books..." />
      <button @click="search">Search</button>
      <div v-if="isLoading">Loading...</div>
      <div v-else-if="error">{{ error }}</div>
      <div v-else-if="results">
        <Books :results="results" :isLoading="isLoading" :limit="10"/>
      </div>
      <div id="featuredBook">
        <Book :key="book.key" :book="featuredBook" />
      </div>
      <div id="featuredList">


      </div>
      <div id="featuredPost">


      </div>
    </div>
</template>
