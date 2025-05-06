<script setup lang="ts">
  import { useRoute } from 'vue-router';
  import { reactive, onMounted } from 'vue';
  import api from '@/api';

  const route = useRoute();
  const userName = route.params.username;


  const state = reactive({
    user: {
      username: '',
      email: '',
      created: '',
      bio: '',
      profile_picture: '',
      is_moderator: false,
      is_writer: false
    },
    isLoading: true
  });

  onMounted(async () => {
    try {
      const response = await api.get(`/user/${userName}/`);
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
          <div class="bg-white p-6 rounded-lg shadow-md flex flex-col md:flex-row items-center gap-6">
            <img
              :src="state.user.profile_picture"
              alt="Profile picture"
              class="w-32 h-32 rounded-full object-cover"
            />
            <div class="text-center md:text-left">
              <h2 class="text-2xl font-bold">{{ state.user.username }}</h2>
              <p class="text-gray-600">{{ state.user.email }}</p>
              <p class="text-sm text-gray-400 mt-1">Joined: {{ state.user.created }}</p>
              <p class="mt-4">{{ state.user.bio || 'No bio provided.' }}</p>
              <div class="mt-4">
                <span v-if="state.user.is_moderator" class="badge bg-purple-200 text-purple-800 mr-2">Moderator</span>
                <span v-if="state.user.is_writer" class="badge bg-blue-200 text-blue-800">Writer</span>
              </div>
            </div>
          </div>
        </main>
      </div>
    </div>
  </section>
</template>

<style scoped>
.badge {
  @apply px-2 py-1 rounded-full text-sm;
}
</style>
