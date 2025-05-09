import { ref } from 'vue'
import axios from 'axios'

export function useApiSearch<T = any>() {
  const results = ref<T | null>(null)
  const error = ref<string | null>(null)
  const isLoading = ref(false)

  const fetchData = async (
    endpoint: string,
    params: Record<string, any> = {}
  ) => {
    isLoading.value = true
    error.value = null

    try {
      const response = await axios.get(endpoint, { params })
      results.value = response.data.docs ?? response.data
    } catch (err: any) {
      error.value = err.response?.data?.error || 'Something went wrong'
    } finally {
      isLoading.value = false
    }
  }

  return { results, error, isLoading, fetchData }
}

export function useSingleFetch<T = any>() {
  const res = ref<T | null>(null)
  const error = ref<string | null>(null)
  const isLoading = ref(false)

  const fetchSingle = async (route: string) => {
    isLoading.value = true
    error.value = null

    try {
      const response = await axios.get(`/api/${route}`)
      res.value = response.data
    } catch (err: any) {
      error.value = err.response?.data?.detail || 'Failed to load book'
    } finally {
      isLoading.value = false
    }
  }

  return { res, error, isLoading, fetchSingle }
}