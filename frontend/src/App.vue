<script setup lang="ts">
  import { RouterView } from 'vue-router'
  import NavBar from '@/components/NavBar.vue';
  import { onMounted } from 'vue'
  import { useAuthStore } from '@/stores/auth'


  onMounted(() => {
    const auth = useAuthStore()
    auth.loadAuthFromStorage()
    if (auth.token) {
      auth.user
    }
  })
</script>

<template>
  <NavBar />

  <RouterView />
</template>