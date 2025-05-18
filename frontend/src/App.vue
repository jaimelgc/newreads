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
    console.log('auth token', auth.token)
    console.log('auth user', auth.user)
  })
</script>

<template class="h-full">
  <div class="bg-sideground">
    <div class="container-xl lg:container m-auto bg-background">
    <NavBar />
    <RouterView />
    </div>
  </div>
</template>