<script setup lang="ts">
  import { RouterView } from 'vue-router'
  import NavBar from '@/components/misc/NavBar.vue';
  import { onMounted } from 'vue'
  import { useAuthStore } from '@/stores/auth'
import BottomVar from './components/misc/BottomVar.vue';


  onMounted(() => {
    const auth = useAuthStore()
    auth.loadAuthFromStorage()
    if (auth.token) {
      auth.user
    }
  })
</script>

<template class="h-full">
  <NavBar class=""/>
  <div class="bg-sideground">
    <div class="container-xl lg:container m-auto bg-background">
    <RouterView />
    </div>
  </div>
  <BottomVar />
</template>