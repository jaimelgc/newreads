<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import api from '@/api';
import { useAuthStore } from '@/stores/auth';

const route = useRoute();
const router = useRouter();
const isEdit = computed(() => !!route.params.listId);
const authUser = useAuthStore().user;

const form = ref({
  title: '',
  books: []  // list of edition keys or objects
});

const isLoading = ref(false);
const error = ref<string | null>(null);

onMounted(async () => {
  if (isEdit.value) {
    isLoading.value = true;
    try {
      const res = await api.get(`/user/${route.params.username}/lists/${route.params.listId}/`);
      form.value = {
        title: res.data.title,
        books: res.data.books  // adapt as needed
      };
    } catch (err) {
      error.value = 'Failed to load list.';
    } finally {
      isLoading.value = false;
    }
  }
});

async function save() {
  try {
    if (isEdit.value) {
      await api.put(`/user/${route.params.username}/lists/${route.params.listId}/`, form.value);
    } else {
      await api.post(`/user/${route.params.username}/lists/`, form.value);
    }
    router.push(`/users/${route.params.username}/lists`);
  } catch (err) {
    error.value = 'Failed to save list.';
  }
}
</script>

<template>
  <div class="max-w-2xl mx-auto p-6 bg-white shadow rounded mt-10">
    <h1 class="text-2xl font-bold mb-4">{{ isEdit ? 'Edit List' : 'Create List' }}</h1>

    <form @submit.prevent="save">
      <label class="block mb-2 font-medium">Title</label>
      <input v-model="form.title" class="border w-full p-2 rounded mb-4" />

      <!-- Book selector UI can go here -->

      <button type="submit" class="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600">
        {{ isEdit ? 'Update' : 'Create' }}
      </button>

      <p v-if="error" class="text-red-500 mt-2">{{ error }}</p>
    </form>
  </div>
</template>