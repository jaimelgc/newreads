<script setup lang="ts">
import { ref, watch } from 'vue';

const props = defineProps<{
  initialData?: { name: string; books: any[]; description: string; is_public: boolean; };
  onSubmit: (data: { name: string; books: any[]; description: string; is_public: boolean; }) => Promise<void>;
}>();

const form = ref({
  name: props.initialData?.name || '',
  books: props.initialData?.books || [],
  description: props.initialData?.description || '',
  is_public: props.initialData?.is_public ?? true,
});

watch(
  () => props.initialData,
  (newData) => {
    if (newData) {
      form.value.name = newData.name;
      form.value.books = newData.books;
      form.value.description = newData.description;
      form.value.is_public = newData.is_public;
    }
  },
  { immediate: true }
);

const isSaving = ref(false);
const error = ref<string | null>(null);

async function submit() {
  isSaving.value = true;
  error.value = null;
  try {
    await props.onSubmit({ ...form.value });
  } catch (err) {
    error.value = 'Failed to save.';
  } finally {
    isSaving.value = false;
  }
}
</script>

<template>
  <form @submit.prevent="submit" class="max-w-xl mx-auto">
    <label class="block mb-1 font-medium">Title</label>
    <input
      v-model="form.name"
      class="border w-full p-2 rounded mb-4"
      type="text"
      required
    />

    <label class="block mb-1 font-medium">Description</label>
    <textarea
      v-model="form.description"
      class="border w-full p-2 rounded mb-4"
      rows="4"
    ></textarea>

    <label class="block mb-1 font-medium">Public</label>
    <input
      type="checkbox"
      v-model="form.is_public"
      class="mb-4"
    />
    <span class="ml-2">{{ form.is_public ? 'Yes' : 'No' }}</span>
    <button
      type="submit"
      :disabled="isSaving"
      class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 disabled:opacity-50"
    >
      {{ isSaving ? 'Saving...' : 'Submit' }}
    </button>

    <p v-if="error" class="text-red-500 mt-2">{{ error }}</p>
  </form>
</template>