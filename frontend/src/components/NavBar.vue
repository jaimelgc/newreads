<script setup lang="ts">
  import { RouterLink, useRoute } from 'vue-router';
  import { storeToRefs } from 'pinia';
  import { useAuthStore } from '@/stores/auth';
  import { computed } from 'vue';

  const route = useRoute();
  const auth = useAuthStore();
  
  const { isLoggedIn, user } = storeToRefs(auth);

  const isActiveLink = (routePath: string) => route.path.startsWith(routePath);

  const buttonDestination = computed(() => {
    return isLoggedIn.value && user.value
      ? { name: 'UserDetailView', params: { username: user.value.username } }
      : { name: 'Login' };
  });

  const buttonText = computed(() => {
    return isLoggedIn.value && user.value ? user.value.username : 'Login';
  });
</script>

<template>
  <nav class="bg-green-700 border-b border-green-500">
    <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
      <div class="flex h-20 items-center justify-between">
        <div class="flex flex-1 items-center justify-center md:items-stretch md:justify-start">
          <!-- Logo -->
          <RouterLink to="/" class="flex flex-shrink-0 items-center mr-4">
            <img class="h-10 w-auto" alt="NewReads" />
            <span class="hidden md:block text-white text-2xl font-bold ml-2">NewReads</span>
          </RouterLink>

          <div class="md:ml-auto">
            <div class="flex space-x-2">
              <RouterLink to="/" :class="[isActiveLink('/') ? 'bg-green-900' : 'hover:bg-green-900 hover:text-white', 'text-white', 'rounded-md', 'px-3', 'py-2']">
                Library
              </RouterLink>
              <RouterLink to="/forum" :class="[isActiveLink('/forum') ? 'bg-green-900' : 'hover:bg-green-900 hover:text-white', 'text-white', 'rounded-md', 'px-3', 'py-2']">
                Forum
              </RouterLink>

              <!-- Login or Username Link -->
              <RouterLink :to="buttonDestination" :class="[isActiveLink('/user') ? 'bg-green-900' : 'hover:bg-green-900 hover:text-white', 'text-white', 'rounded-md', 'px-3', 'py-2']">
                {{ buttonText }}
              </RouterLink>

              <!-- Sign up or Logout -->
              <RouterLink
                v-if="!isLoggedIn"
                to="/register"
                :class="[isActiveLink('/register') ? 'bg-green-900' : 'hover:bg-green-900 hover:text-white', 'text-white', 'rounded-md', 'px-3', 'py-2']">
                Sign up
              </RouterLink>
              <RouterLink
                v-else
                to="/logout"
                class="hover:bg-green-900 hover:text-white text-white rounded-md px-3 py-2">
                Logout
              </RouterLink>
            </div>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>