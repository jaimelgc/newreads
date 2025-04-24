<script setup lang="ts">
        import { ref } from 'vue';
        import axios from 'axios'


    function useBookSearch() {
        const results = ref(null)
        const error = ref(null)
        const loading = ref(false)

        const searchBooks = async (key: string, url: string, page = 1) => {
            loading.value = true
            error.value = null

            try {
                const response = await axios.get('/api/library/search/', {
                    params: { key, url, page },
                })
                    results.value = response.data
                } catch (err: any) {
                    error.value = err.response?.data?.error || 'Something went wrong'
                } finally {
                    loading.value = false
            }
        }

        console.log("SALIDA", results)
        console.error("ERROR", error)
        return { results, error, loading, searchBooks }
    }   

    const searchTerm = ref('')
    const { results, error, loading, searchBooks } = useBookSearch()

    const search = () => {
        const key = `book-search-${searchTerm.value}`
        const url = `https://openlibrary.org/search.json?q=${encodeURIComponent(searchTerm.value)}`
        searchBooks(key, url)
    }

</script>

<template>
    <div>
      <input v-model="searchTerm" placeholder="Search books..." />
      <button @click="search">Search</button>
  
      <div v-if="loading">Loading...</div>
      <div v-else-if="error">{{ error }}</div>
      <div v-else-if="results">
        <pre>{{ results }}</pre>
      </div>
    </div>
  </template>