<script setup lang="ts">
        import { ref } from 'vue';
        import axios from 'axios'
        import api from '@/api';
        import Books from './Books.vue';


    function useBookSearch() {
        const results = ref(null)
        const error = ref(null)
        const isLoading = ref(false)

        const searchBooks = async (key: string, url: string, page = 1) => {
            isLoading.value = true
            error.value = null

            try {
                const response = await api.get('/library/search/', {
                    params: { key, url, page },
                })
                    results.value = response.data.docs
                    console.log(results.value)
                } catch (err: any) {
                    error.value = err.response?.data?.error || 'Something went wrong'
                } finally {
                    isLoading.value = false
            }
        }

        console.log("SALIDA", results)
        // console.error("ERROR", error)
        return { results, error, isLoading, searchBooks }
    }   

    const searchTerm = ref('')
    const { results, error, isLoading, searchBooks } = useBookSearch()

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
      <div v-if="isLoading">Loading...</div>
      <div v-else-if="error">{{ error }}</div>
      <div v-else-if="results">
        <Books :results="results" :isLoading="isLoading" :limit="10"/>
      </div>
    </div>
  </template>