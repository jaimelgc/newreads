<script setup lang="ts">
  import { RouterView } from 'vue-router'
  import NavBar from '@/components/NavBar.vue';
  import { onMounted } from 'vue'
  import { useAuthStore } from '@/stores/auth'

  onMounted(() => {
    const auth = useAuthStore()
    if (auth.token) {
      auth.fetchUser()
    }
  })
</script>

<template>
  <NavBar />
  <RouterView />
</template>