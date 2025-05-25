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
  <nav class="bg-secondary-default border-b border-green-300">
    <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
      <div class="flex h-20 items-center justify-between">
        <div class="flex flex-1 items-center justify-center md:items-stretch md:justify-start">
          <RouterLink to="/" class="flex flex-shrink-0 items-center mr-4">
            <img class="h-10 w-auto max-w-[8rem]" src="/logo-2-crop.png" alt="NewReads" />
            <span class="hidden md:block text-white text-2xl font-bold ml-2">NewReads</span>
          </RouterLink>

          <div class="md:ml-auto">
            <div class="flex space-x-2">
              <RouterLink to="/" class="font-bold bg-secondary-default hover:bg-secondary-light hover:text-white text-white rounded-md px-3 py-2">
                Library
              </RouterLink>
              <div class="relative group">
                <button class="font-bold bg-secondary-default hover:bg-secondary-light hover:text-white text-white rounded-md px-3 py-2">
                  Search
                </button>
                <div
                  class="absolute left-0 z-10 hidden group-hover:flex flex-col bg-gray-800 text-white rounded-md shadow-lg mt-0 w-48"
                >
                  <RouterLink
                    to="/search"
                    class="block px-4 py-2 hover:bg-secondary-light"
                  >
                    Books
                  </RouterLink>
                  <RouterLink
                    to="/booklists/search"
                    class="block px-4 py-2 hover:bg-secondary-light"
                  >
                    Lists
                  </RouterLink>
                  <RouterLink
                    to="/forum"
                    class="block px-4 py-2 hover:bg-secondary-light"
                  >
                    Posts
                  </RouterLink>
                  <RouterLink
                    to="/users/search"
                    class="block px-4 py-2 hover:bg-secondary-light"
                  >
                    Users
                  </RouterLink>
                </div>
              </div>

              <RouterLink to="/forum" class="font-bold bg-secondary-default hover:bg-secondary-light hover:text-white text-white rounded-md px-3 py-2">
                Forum
              </RouterLink>

              <RouterLink :to="buttonDestination" class="font-bold bg-secondary-default hover:bg-secondary-light hover:text-white text-white rounded-md px-3 py-2">
                {{ buttonText }}
              </RouterLink>

              <RouterLink
                v-if="!isLoggedIn"
                to="/register"
                class="font-bold bg-secondary-default hover:bg-secondary-light hover:text-white text-white rounded-md px-3 py-2">
                Sign up
              </RouterLink>
              <RouterLink
                v-else
                to="/logout"
                class="font-bold hover:bg-secondary-light hover:text-white text-white rounded-md px-3 py-2">
                Logout
              </RouterLink>
            </div>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>