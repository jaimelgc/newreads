<script setup lang="ts">

    // import logo from '@/assets/img/logo.png'
    import { RouterLink, useRoute } from 'vue-router';
    import { useAuthStore } from '@/stores/auth'
    import { computed } from 'vue'

    const isActiveLink = (routePath:string) => {
      const route = useRoute();
      return route.path === routePath;
    }

    const auth = useAuthStore()

    const buttonDestination = computed(() => {
      return auth.isLoggedIn ? { name: 'UserDetail' } : { name: 'Login' }
    })

    const buttonText = computed(() => {
      return auth.isLoggedIn ? 'View Profile' : 'Login'
    })

</script>

<template>
    <nav class="bg-green-700 border-b border-green-500">
      <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
        <div class="flex h-20 items-center justify-between">
          <div class="flex flex-1 items-center justify-center md:items-stretch md:justify-start">
            <!-- Logo -->
            <RouterLink class="flex flex-shrink-0 items-center mr-4" to="/">
              <img class="h-10 w-auto"  alt="NewReads" /> <!-- :src="logo" -->
              <span class="hidden md:block text-white text-2xl font-bold ml-2">
                NewReads
              </span>
            </RouterLink>
            <div class="md:ml-auto">
              <div class="flex space-x-2">
                <RouterLink to="/" :class="[isActiveLink('/') ? 'bg-green-900' : 'hover:bg-green-900 hover:text-white', 'text-white', 'rounded-md', 'px-3', 'py-2']">
                  Home
                </RouterLink>
                <RouterLink to="/library" :class="[isActiveLink('/library') ? 'bg-green-900' : 'hover:bg-green-900 hover:text-white', 'text-white', 'rounded-md', 'px-3', 'py-2']">
                  Library
                </RouterLink>
                <RouterLink to="/forum" :class="[isActiveLink('/forum') ? 'bg-green-900' : 'hover:bg-green-900 hover:text-white', 'text-white', 'rounded-md', 'px-3', 'py-2']">
                  Forum
                </RouterLink>
                <RouterLink :to="buttonDestination" :class="[isActiveLink('/user') ? 'bg-green-900' : 'hover:bg-green-900 hover:text-white', 'text-white', 'rounded-md', 'px-3', 'py-2']">
                  {{ buttonText }}
                </RouterLink>
              </div>
            </div>
          </div>
        </div>
      </div>
    </nav>
</template>