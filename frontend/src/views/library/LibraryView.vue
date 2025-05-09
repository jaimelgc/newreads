<script setup lang="ts">
  import { ref, computed, onMounted } from 'vue';
  import Books from '@/components/library/Books.vue';
  import Book from '@/components/library/Book.vue';
  import { useApiSearch, useSingleFetch } from '@/search';
  import { storeToRefs } from 'pinia'
  import { useAuthStore } from '@/stores/auth'

  // CHECK AUTH
  const auth = useAuthStore()
  const { isLoggedIn, user } = storeToRefs(auth)

  console.log(isLoggedIn.value)
  console.log(user.value)

  // SEARCH
  const searchTerm = ref('')
  const { results, error, isLoading, fetchData } = useApiSearch()

  const search = () => {
    const endpoint = '/api/library/search/'
    const params = {
        key: `book-search-${searchTerm.value}`,
        url: `https://openlibrary.org/search.json?q=${encodeURIComponent(searchTerm.value)}`
    }
    fetchData(endpoint, params)
  }

  // FEATURES
  const { res: featuredBook, error: bookError, isLoading: bookIsLoading, fetchSingle: fetchFeaturedBook } = useSingleFetch()
  const { res: featuredList, error: listError, isLoading: listIsLoading, fetchSingle: fetchFeaturedList } = useSingleFetch()
  const { res: featuredPost, error: postError, isLoading: postIsLoading, fetchSingle: fetchFeaturedPost } = useSingleFetch()
  onMounted(() => { 
    fetchFeaturedBook('books/OL21419612M')
    fetchFeaturedBook('books/OL21419612M')
    fetchFeaturedBook('books/OL21419612M')
  })
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
        <div v-if="!bookError && !bookIsLoading" && featuredBook>
          <Book :key="featuredBook.key" :book="featuredBook" />
        </div>
      </div>
      <div id="featuredList">


      </div>
      <div id="featuredPost">


      </div>
    </div>
</template>
