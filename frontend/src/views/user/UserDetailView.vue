<script setup lang="ts">
  import { useRoute } from 'vue-router';
  import { reactive, onMounted } from 'vue';

  import api from '@/api';


  const route = useRoute();

  const userName = route.params.id;

  const state = reactive({
    user: {},
    isLoading: true
  });

  onMounted(async () => {
    try {
        const response = await api.get(`/user/${userName}`);
        state.user = response.data;
    } catch (error) {
        console.error('Error fetching user');
    } finally {
        state.isLoading = false;
    }
  });
</script>

<template>
  <section v-if="!state.isLoading" class="bg-green-50">
    <div class="container m-auto py-10 px-6">
      <div class="grid grid-cols-1 md:grid-cols-70/30 w-full gap-6">
        <main>
          <div class="bg-white p-6 rounded-lg shadow-md text-center md:text-left">
            <div class="text-gray-500 mb-4">{{ state.user }}</div>
          </div>
        </main>
      </div>
    </div>
  </section>
</template>
