<script setup lang="ts">
  import { RouterView } from 'vue-router'
  import NavBar from '@/components/NavBar.vue';
  import { onMounted } from 'vue'
  import { useAuthStore } from '@/stores/auth'
  import Breadcrumbs from './components/Breadcrumbs.vue';

  onMounted(() => {
    const auth = useAuthStore()
    if (auth.token) {
      auth.user
    }
  })
</script>

<template>
  <NavBar />
  <Breadcrumbs />
  <RouterView />
</template>