<script setup lang="ts">
  import { defineProps, computed, ref, onMounted } from 'vue';
  import { RouterLink, useRouter } from 'vue-router';
  import Modal from '@/components/Modal.vue';
  import AuthModal from '@/components/AuthModal.vue';
  import { storeToRefs } from 'pinia';
  import { useAuthStore } from '@/stores/auth';
  import api from '@/api';
  import { useToast } from 'vue-toastification';

  const auth = useAuthStore();
  const { isLoggedIn, user } = storeToRefs(auth);
  const router = useRouter();
  const toast = useToast();

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
    if (props.book.cover_url) return props.book.cover_url;
    if (props.book.cover_i) return `https://covers.openlibrary.org/b/id/${props.book.cover_i}-M.jpg`;
    return 'https://via.placeholder.com/150';
  });

  const showModal = ref(false);
  const showLoginPrompt = ref(false);
  const userLists = ref<{ id: number; name: string }[]>([]);
  const selectedListId = ref<number | null>(null);
  const username = isLoggedIn.value && user.value ? user.value.username : null;

  async function fetchUserLists() {
    if (!isLoggedIn.value) return;
    const response = await api.get(`/user/booklists/`, {
      params: { username: username },
    });
    userLists.value = response.data;
  }

  async function addBookToList() {
    if (!selectedListId.value || !selectedEditionId.value) {
      return
    };

    try {
      const bookResponse = await api.get(`/library/getbook/${selectedEditionId.value}/`);
      const bookId = bookResponse.data.id;

      await api.post('/user/blitems/', {
        book_list: selectedListId.value,
        book: bookId,
      });
      toast.success('List Bookmarked');
      showModal.value = false;
      selectedListId.value = null;
    } catch (error) {
      console.error('Failed to add book to list:', error);
    }
  }

  function handleAddToListClick() {
    if (!isLoggedIn.value) {
      showLoginPrompt.value = true;
      return;
    }
    showModal.value = true;
  }

  async function goToCreateList() {
    if (!selectedEditionId.value) return;

    const bookResponse = await api.get(`/library/getbook/${selectedEditionId.value}/`);
    const bookId = bookResponse.data.id;
    router.push({
      name: 'ListCreate',
      params: { username: user.value?.username },
      query: {
        book: JSON.stringify({
          ol_id: bookId,
          title: props.book.title,
        }),
      },
    });
  }

  async function goToCreatePost() {
    if (!isLoggedIn.value) {
      showLoginPrompt.value = true;
      return;
    }

    if (!selectedEditionId.value) return;

    // const bookResponse = await api.get(`/library/getbook/${selectedEditionId.value}/`);
    // const bookId = bookResponse.data.id;
    router.push({
      name: 'CreatePostView',
      params: { username: user.value?.username },
      query: {
        book: JSON.stringify({
          ol_id: selectedEditionId.value,
          title: props.book.title,
        }),
      },
    });
  }

  onMounted(fetchUserLists);
</script>

<template>
  <div class="border-background rounded shadow p-6 bg-background hover:border-blue-300 border-4 flex flex-col items-center text-center">
    <RouterLink
      v-if="selectedEditionId"
      :to="`/books/${selectedEditionId}`"
      class="rounded shadow p-6 bg-background flex flex-col items-center text-center"
    >
      <img
        :src="coverUrl"
        alt="Book Cover"
        class="mb-4 h-60 w-40 object-cover"
      />
      <h3 class="text-xl font-semibold mb-1 text-white">{{ book.title }}</h3>
      <p class="text-gray-300 mb-1">
        {{ Array.isArray(book.author_name) ? book.author_name.join(', ') : book.author_name }}
      </p>
      <p class="text-sm text-gray-300 mb-4">
        First published: {{ book.first_publish_year || book.publish_date || 'N/A' }}
      </p>
    </RouterLink>
    <div class="flex flex-wrap justify-center gap-2">
      <button
        @click.stop="handleAddToListClick"
        class="h-[36px] border border-blue-500 text-blue-500 hover:bg-blue-500 hover:text-white px-4 py-1.5 rounded-lg text-sm transition"
      >
        Add to List
      </button>

      <button
        @click.stop="goToCreatePost"
        class="h-[36px] border border-purple-500 text-purple-500 hover:bg-purple-500 hover:text-white px-4 py-1.5 rounded-lg text-sm transition"
      >
        New Post
      </button>
    </div>
  </div>

  <Modal :show="showModal" @close="showModal = false" @confirm="addBookToList">
    <template #default>
      <h2 class="text-lg font-semibold mb-4">Choose a list to add this book to:</h2>
      <select v-model="selectedListId" class="text-black w-full border rounded p-2 mb-4">
        <option disabled value="">Select a list</option>
        <option v-for="list in userLists" :key="list.id" :value="list.id">
          {{ list.name }}
        </option>
      </select>
      <button
        @click="goToCreateList"
        class="w-full bg-secondary-light hover:bg-secondary-default text-gray-100 font-bold px-4 py-2 rounded-lg text-sm"
      >
        Create New List
      </button>
    </template>
  </Modal>

  <AuthModal
    :show="showLoginPrompt"
    @close="showLoginPrompt = false"
    @login="router.push({ name: 'Login' });"
    @register="router.push({ name: 'Register' })"
  />
</template>