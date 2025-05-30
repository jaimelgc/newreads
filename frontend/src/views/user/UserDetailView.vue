<script setup lang="ts">
  import { useRoute, useRouter } from 'vue-router';
  import { ref, reactive, computed, onMounted } from 'vue';
  import api from '@/api';
  import Lists from '@/components/lists/Lists.vue';
  import { useAuthStore } from '@/stores/auth';
  import Posts from '@/components/forum/Posts.vue';

  const route = useRoute();
  const router = useRouter();
  const userName = route.params.username;
  const isLoading = ref(true);


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

  const currentUser = useAuthStore().user; 
  const canCreate = computed(() => currentUser?.username === state.user.username);

  const activeTab = ref<'lists' | 'posts'>('lists');
  const userLists = ref([]);
  const userPosts = ref([]);

  function goToPost(postId: number) {
    router.push({ name: 'PostDetail', params: { id: postId } });
  }

  onMounted(async () => {
    try {
      const  response = await api.get(`/user/${userName}/`);
      state.user = response.data;
      // USER LISTS
      const listsResponse = await api.get(`/user/booklists/`, {
        params: { username: userName },
      });
      userLists.value = listsResponse.data;
      
      // USER POSTS
      const postsResponse = await api.get(`/forum/posts/`, {
        params: { username: userName },
      });
      userPosts.value = postsResponse.data;
    } catch (error) {
      console.error('Error fetching user');
    } finally {
      state.isLoading = false;
    }
  });
</script>

<template>
  <div v-if="state.isLoading" class="bg-background min-h-screen">Loading</div>
  <section v-if="!state.isLoading" class="bg-background">
    <div class="container m-auto py-10 px-6">
      <div class="grid grid-cols-1 md:grid-cols-70/30 w-full gap-6">
        <main>
          <div class="bg-background p-6 rounded-lg shadow-md flex flex-col md:flex-row items-center gap-6">
            <img
              src="/def.jpg"
              alt="Profile picture"
              class="w-32 h-32 rounded-full object-cover"
            />
            <div class="text-center md:text-left">
              <h2 class="text-2xl font-bold text-white">{{ state.user.username }}</h2>
              <p class="text-sm text-gray-200 mt-1">Joined: {{ state.user.created }}</p>
              <p class="mt-4 text-white">{{ state.user.bio || 'No bio provided.' }}</p>
              <div class="mt-4">
                <span v-if="state.user.is_moderator" class="badge bg-purple-200 text-purple-800 mr-2">Moderator</span>
                <span v-if="state.user.is_writer" class="badge bg-blue-200 text-blue-800">Writer</span>
              </div>
            </div>
          </div>
          <div class="mt-10">
            <div class="flex border-b mb-4">
              <button
                class="py-2 px-4 font-semibold"
                :class="activeTab === 'lists' ? 'border-b-2 border-green-600 text-green-700' : 'text-gray-500'"
                @click="activeTab = 'lists'"
              >
                Lists
              </button>
              <button
                class="py-2 px-4 font-semibold"
                :class="activeTab === 'posts' ? 'border-b-2 border-green-600 text-green-700' : 'text-gray-500'"
                @click="activeTab = 'posts'"
              >
                Posts
              </button>
            </div>

            <div v-if="activeTab === 'lists'">
              <Lists
                :results="userLists"
                :isLoading="state.isLoading"
                :limit="10"
                context="user"
                :canCreate="canCreate" 
                :username="state.user.username"
              />
            </div>
            <div v-if="activeTab === 'posts'" >
              <Posts :results="userPosts" :isLoading="false" method="" @select="goToPost" />
            </div>
          </div>
        </main>
      </div>
    </div>
  </section>
</template>
