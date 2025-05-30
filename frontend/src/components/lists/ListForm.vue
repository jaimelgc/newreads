<script setup lang="ts">
import { ref, watch } from 'vue';

const props = defineProps<{
  initialData?: {
    name: string;
    description: string;
    items: { book: { ol_id: string; title: string }; title?: string }[];
    is_public: boolean;
  };
  onSubmit: (data: {
    name: string;
    description: string;
    items: { book: { ol_id: string }; title?: string }[];
    is_public: boolean;
  }) => Promise<void>;
}>();

const form = ref({
  name: props.initialData?.name || '',
  description: props.initialData?.description || '',
  items: props.initialData?.items || [],
  is_public: props.initialData?.is_public ?? true,
});

watch(
  () => props.initialData,
  (newData) => {
    if (newData) {
      form.value.name = newData.name;
      form.value.description = newData.description;
      form.value.items = newData.items;
      form.value.is_public = newData.is_public;
    }
  },
  { immediate: true }
);

const isSaving = ref(false);
const error = ref<string | null>(null);

function addItem() {
  form.value.items.push({ book: { ol_id: '', title: '' }, title: '' });
}

function removeItem(index: number) {
  form.value.items.splice(index, 1);
}

const cancelEdit = () => window.history.back();

async function submit() {
  isSaving.value = true;
  error.value = null;
  try {
    const payload = {
      ...form.value,
      items: form.value.items.map((item) => ({
        book: { ol_id: item.book.ol_id },
        title: item.title,
      })),
    };
    await props.onSubmit(payload);
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
      class="text-white bg-modal border border-secondary-light w-full p-2 rounded mb-4"
      type="text"
      required
    />

    <label class="block mb-1 font-medium">Description</label>
    <textarea
      v-model="form.description"
      class="text-white bg-modal border border-secondary-light w-full p-2 rounded mb-4"
      rows="4"
    ></textarea>

    <button
      type="submit"
      :disabled="isSaving"
      class="m-2 px-4 py-2 font-semibold border border-secondary-light text-secondary-light hover:bg-secondary-light hover:text-white rounded disabled:opacity-50"
    >
      {{ isSaving ? 'Saving...' : 'Submit' }}
    </button>
    <button
      type="submit"
      @click="cancelEdit"
      class="m-2 px-4 py-2 font-semibold border border-red-500 text-red-500 hover:bg-red-500 hover:text-white rounded disabled:opacity-50"
    >
      Cancel
    </button>

    <p v-if="error" class="text-red-500 mt-2">{{ error }}</p>
  </form>
</template>