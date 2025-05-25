<script setup lang="ts">
import { reactive, ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import api from '@/api';

const route = useRoute();
const router = useRouter();
const userName = route.params.name;

const state = reactive({
  user: {
    username: '',
    email: '',
    created: '',
    bio: '',
    is_moderator: false,
    is_writer: false,
    profile_picture: '',
  },
  isLoading: true,
  preview: '',
  file: null as File | null,
  error: '',
  success: '',
});

onMounted(async () => {
  try {
    const response = await api.get(`/profile/`);
    Object.assign(state.user, response.data);
    state.preview = state.user.profile_picture;
  } catch (e) {
    state.error = 'Failed to load user data.';
  } finally {
    state.isLoading = false;
  }
});

const handleFileChange = (event: Event) => {
  const target = event.target as HTMLInputElement;
  const file = target.files?.[0];
  if (file) {
    state.file = file;
    state.preview = URL.createObjectURL(file);
  }
};

const updateUser = async () => {
  const formData = new FormData();
  formData.append('bio', state.user.bio);
  formData.append('is_moderator', String(state.user.is_moderator));
  formData.append('is_writer', String(state.user.is_writer));
  if (state.file) {
    formData.append('profile_picture', state.file);
  }

  try {
    await api.patch('/profile/', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    });
    state.success = 'Profile updated successfully!';
    setTimeout(() => {
      router.push(`/users/${userName}`);
    }, 1000);
  } catch (e) {
    state.error = 'Failed to update user.';
  }
};
</script>

<template>
    <section v-if="!state.isLoading" class="bg-green-50 min-h-screen">
        <div class="container m-auto py-10 px-6 max-w-2xl">
        <h2 class="text-2xl font-bold mb-6">Edit Profile</h2>

        <div v-if="state.success" class="bg-green-100 text-green-800 p-3 rounded mb-4">
            {{ state.success }}
        </div>
        <div v-if="state.error" class="bg-red-100 text-red-800 p-3 rounded mb-4">
            {{ state.error }}
        </div>

        <form @submit.prevent="updateUser" class="space-y-6">
            <div>
            <label class="block font-semibold mb-1">Username</label>
            <input disabled v-model="state.user.username" class="form-control" />
            </div>

            <div>
            <label class="block font-semibold mb-1">Email</label>
            <input disabled v-model="state.user.email" class="form-control" />
            </div>

            <div>
            <label class="block font-semibold mb-1">Bio</label>
            <textarea v-model="state.user.bio" class="form-control" rows="4" />
            </div>

            <div>
            <label class="block font-semibold mb-1">Profile Picture</label>
            <input type="file" accept="image/*" @change="handleFileChange" class="form-control" />
            <div v-if="state.preview" class="mt-2">
                <img :src="state.preview" class="w-24 h-24 rounded-full object-cover" />
            </div>
            </div>

            <div class="flex gap-4">
            <label class="flex items-center gap-2">
                <input type="checkbox" v-model="state.user.is_moderator" />
                Moderator
            </label>
            <label class="flex items-center gap-2">
                <input type="checkbox" v-model="state.user.is_writer" />
                Writer
            </label>
            </div>

            <div class="flex gap-4">
            <button type="submit" class="btn btn-success">Save</button>
            <router-link :to="`/users/${userName}`" class="btn btn-secondary">Cancel</router-link>
            </div>
        </form>
        </div>
    </section>
</template>

<style lang="postcss" scoped>
    .form-control {
        @apply w-full border border-gray-300 rounded p-2;
    }
    .btn {
        @apply px-4 py-2 rounded text-white;
    }
    .btn-success {
        @apply bg-green-600 hover:bg-green-700;
    }
    .btn-secondary {
        @apply bg-gray-500 hover:bg-gray-600;
    }
</style>