<script setup lang="ts">
    import { defineProps, computed, ref, onMounted } from 'vue';
    import { RouterLink } from 'vue-router';
    import Modal from '@/components/Modal.vue';
    import { storeToRefs } from 'pinia';
    import { useAuthStore } from '@/stores/auth';
    import api from '@/api';

    const auth = useAuthStore();
    const { isLoggedIn, user } = storeToRefs(auth);

    // BOOK CARD
    const props = defineProps<{
        book: {
            title: string;
            ol_id: string;
            author_name?: string | string[];
            publish_date?: string;
            cover_url?: string;
            cover_edition_key?: string;
            cover_i?: number;
            edition_key?: string[];
            key?: string;
            first_publish_year?: number;
        };
    }>();

    const selectedEditionId = computed(() => {
        return props.book.cover_edition_key || props.book.edition_key?.[0] || props.book.ol_id || null;
    });
    
    const coverUrl = computed(() => {
        if (props.book.cover_url) return props.book.cover_url; // From backend
        if (props.book.cover_i) return `https://covers.openlibrary.org/b/id/${props.book.cover_i}-M.jpg`;
        return 'https://via.placeholder.com/150';
    });

    // POP UP
    const showModal = ref(false);
    const userLists = ref<{ id: number; name: string }[]>([]);
    const selectedListId = ref<number | null>(null);
    const username = isLoggedIn.value && user.value ? user.value.username : null;

    async function fetchUserLists() {
        const response = await api.get(`/user/booklists/`, {
            params: { username: username },
        });
        userLists.value = response.data;
    }

    async function addBookToList() {
        if (!selectedListId.value || !selectedEditionId.value) return;

        try {
            const bookResponse = await api.get(`/library/getbook/${selectedEditionId.value}/`);
            const bookId = bookResponse.data.id;
            console.log(selectedListId.value, bookId)

            await api.post('/user/blitems/', {
                book_list: selectedListId.value,
                book: bookId,
            });
            showModal.value = false;
            selectedListId.value = null;
        } catch (error) {
            console.error('Failed to add book to list:', error);
        }
    }

    onMounted(fetchUserLists);
</script>

<template>
    <div class="border rounded shadow p-4 bg-white">
    <img :src="coverUrl" alt="Book Cover" class="mb-4" />
    <h3 class="text-xl font-semibold">{{ book.title }}</h3>
    <p class="text-gray-600">
      {{ Array.isArray(book.author_name) ? book.author_name.join(', ') : book.author_name }}
    </p>
    <p class="text-sm text-gray-500">
      First published: {{ book.first_publish_year || book.publish_date || 'N/A' }}
    </p>

    <div class="flex gap-2 mt-4">
      <RouterLink
        v-if="selectedEditionId"
        :to="`/books/${selectedEditionId}`"
        class="h-[36px] bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-lg text-center text-sm"
      >
        Read More
      </RouterLink>

      <button
        @click="showModal = true"
        class="h-[36px] bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-lg text-sm"
      >
        Add to List
      </button>
    </div>
    <Modal :show="showModal" @close="showModal = false" @confirm="addBookToList">
      <template #default>
        <h2 class="text-lg font-semibold mb-4">Choose a list to add this book to:</h2>
        <select v-model="selectedListId" class="w-full border rounded p-2">
          <option disabled value="">Select a list</option>
          <option v-for="list in userLists" :key="list.id" :value="list.id">
            {{ list.name }}
          </option>
        </select>
      </template>
    </Modal>
  </div>
</template>