<script setup lang="ts">
    import router from '@/router';
    import { RouterLink } from 'vue-router';
    import { useAuthStore } from '@/stores/auth';
    import { onMounted } from 'vue';

    const auth = useAuthStore();

    onMounted(() => {
      auth.clearAuth();
      localStorage.clear();
      router.push('/')
    });
 </script>
 
 <template>
     <section class="text-center flex flex-col justify-center items-center h-96">
       <i class="pi pi-exclamation-triangle text-yellow-500 text-7xl mb-5"></i>
       <h1 class="text-6xl font-bold mb-4">Successfully logged out </h1>
       <p class="text-xl mb-5">This page does not exist</p>
       <RouterLink to="/" class="text-white bg-green-700 hover:bg-green-900 rounded-md px-3 py-2 mt-4">
         Home
       </RouterLink>
       <RouterLink to="/login" class="text-white bg-green-700 hover:bg-green-900 rounded-md px-3 py-2 mt-4">
         Login
       </RouterLink>
     </section>
 </template>