<script setup lang="ts">
  import { onMounted, ref, computed } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  import api from '@/api';
  import Modal from '@/components/Modal.vue';
  import AuthModal from '@/components/AuthModal.vue';
  import { useModal } from '@/composables/useModal';
  import { useAuthStore } from '@/stores/auth';
  import { useToast } from 'vue-toastification';
  import PulseLoader from 'vue-spinner/src/PulseLoader.vue';

  const toast = useToast();

  const route = useRoute();
  const router = useRouter();
  const listId = route.params.listId;
  const username = route.params.username;

  const auth = useAuthStore();
  const { user, isLoggedIn } = auth;

  const list = ref<{
    id: number;
    name: string;
    description: string;
    author: {
      id: number;
      username: string;
      profile_picture: string;
    };
    created_at: string;
    items: {
      id: number;
      book: number;
      added_at: string;
      bookDetails?: {
        id: number;
        ol_id: string;
        title: string;
        author_name?: string;
        cover_url?: string;
      };
    }[];
  } | null>(null);

  const isLoading = ref(true);
  const showLoginPrompt = ref(false);
  const error = ref<string | null>(null);

  const deleteListModal = useModal();
  const deleteItemModal = useModal<number>();

  const canDelete = computed(() => {
    return user?.username === list.value?.author.username || user?.isModerator;
  });

  const canBookmark = computed(() => {
    return user?.username !== list.value?.author.username;
  });

  const visibleCount = ref(10);

  const visibleItems = computed(() => {
    return list.value?.items.slice(0, visibleCount.value) ?? [];
  });

  const showMore = () => {
    visibleCount.value += 10;
  };

  const fetchBookDetails = async () => {
    if (!list.value) return;
    const items = list.value.items;

    await Promise.all(
      items.map(async (item) => {
        try {
          const response = await api.get(`/library/books/${item.book}/`);
          item.bookDetails = response.data;
        } catch (error) {
          console.error(`Failed to fetch book with id ${item.book}:`, error);
        }
      })
    );
  };

  const deleteList = async () => {
    try {
      await api.delete(`/user/booklists/${listId}/`);
      router.push(`/users/${username}`);
    } catch (error) {
      console.error('Error deleting list:', error);
    } finally {
      deleteListModal.close();
    }
  };

  const deleteItem = async () => {
    const itemId = deleteItemModal.payload.value;
    if (!itemId) return;

    try {
      await api.delete(`/user/blitems/${itemId}/`);
      list.value!.items = list.value!.items.filter(item => item.id !== itemId);
    } catch (error) {
      console.error('Error deleting item:', error);
    } finally {
      deleteItemModal.close();
    }
  };

  async function bookmark() {
      if (!auth.user?.id) {
        showLoginPrompt.value = true;
        return;
      }

      try {
        await api.post(`/user/booklists/${list.value!.id}/bookmark/`);
        toast.success('List Bookmarked');
        router.push(`/users/${auth.user.username}`);
      } catch (err) {
        toast.error('Failed to bookmark the list.');
      }
    }

  onMounted(async () => {
    try {
      const response = await api.get(`/user/booklists/${listId}/`);
      list.value = response.data;
      await fetchBookDetails();
    } catch (error) {
      console.error('Error fetching list:', error);
    } finally {
      isLoading.value = false;
    }
  });
</script>

<template>
  <div v-if="isLoading" class="min-h-screen flex flex-col justify-center items-center text-gray-500 py-6">
    <p class="text-3xl font-semibold text-secondary-light">Loading List</p>
    <PulseLoader />
  </div>
  <section v-if="!isLoading" class="py-10 px-6 bg-background min-h-screen">
    <div class="max-w-4xl mx-auto">
      <h1 class="text-3xl font-bold mb-4 text-white">{{ list?.name }}</h1>
      <p class="text-gray-200 mb-2">
        By 
        <RouterLink
          :to="`/users/${list?.author.username}/`"
          class="text-secondary-light font-semibold hover:text-secondary-default">
          {{ list?.author.username }}
        </RouterLink>
        <img
          src="/def.jpg"
          alt="Author profile picture"
          class="inline-block w-6 h-6 rounded-full object-cover ml-2"
        />
      </p>
      <p class="text-sm text-gray-200 mb-4">Created: {{ list?.created_at }}</p>
      <p class="text-gray-200 mb-6">{{ list?.description }}</p>

      <div v-if="canDelete" class="flex gap-4 mb-6">
        <RouterLink
          :to="`/users/${username}/lists/${listId}/edit`"
          class="px-4 py-2 border rounded border-secondary-light text-secondary-light hover:bg-secondary-light hover:text-white"
        >
          Edit List
        </RouterLink>
        <button
          @click="deleteListModal.open()"
          class="px-4 py-2 border rounded border-red-500 text-red-500 hover:bg-red-500 hover:text-white"
        >
          Delete List
        </button>
      </div>
      <div v-if="canBookmark" class="flex gap-4 mb-6">
        <button
        @click="bookmark"
          class="h-[36px] border border-blue-400 text-blue-400 hover:bg-blue-400 hover:text-white px-4 py-1.5 rounded-lg text-sm transition"
        >
          Bookmark
        </button>
      </div>

      <div class="bg-background border border-blue-200 rounded-lg p-6 w-[]">
        <div v-if="list?.items?.length" class="divide-y divide-secondary-light">
          <div
            v-for="item in visibleItems"
            :key="item.id"
            class="flex items-start gap-4 py-4 relative"
          >
            <img
              :src="item.bookDetails?.cover_url || 'https://via.placeholder.com/100x150'"
              class="w-36 h-auto rounded"
              alt="Book cover"
            />
            <div>
              <RouterLink :to="`/books/${item.bookDetails?.ol_id}`">
                <div class="text-lg font-medium text-white hover:text-secondary-light">{{ item.bookDetails?.title }}</div>
              </RouterLink>
              <div class="text-sm text-gray-300">{{ item.bookDetails?.author_name }}</div>
              <div class="text-xs text-gray-400">Added: {{ item.added_at }}</div>
            </div>
            <button
              v-if="canDelete"
              @click="deleteItemModal.open(item.id)"
              class="absolute top-2 right-2 text-xs border bg-white hover:bg-red-700 border-red-700 text-red-700 hover:text-white rounded-full px-2 py-1"
            >
              ✕
            </button>
          </div>
        </div>
        <p v-else class="text-bold text-2xl text-secondary-light">No books in this list yet.</p>
        <div v-if="list && list.items.length > visibleCount" class="mt-6 text-center">
          <button
            @click="showMore"
            class="px-4 py-2 text-sm border border-blue-400 text-blue-400 hover:bg-blue-400 hover:text-white rounded-lg transition"
          >
            Show More
          </button>
        </div>
        
      </div>

      <AuthModal
        :show="showLoginPrompt"
        @close="showLoginPrompt = false"
        @login="router.push({ name: 'Login' });"
        @register="router.push({ name: 'Register' })"
      />

      <Modal
        :show="deleteListModal.isOpen.value"
        @close="deleteListModal.close"
        @confirm="deleteList"
      >
        <p class="text-white">Are you sure you want to delete this list?</p>
      </Modal>

      <Modal
        :show="deleteItemModal.isOpen.value"
        @close="deleteItemModal.close"
        @confirm="deleteItem"
      >
        <p class="text-white">Are you sure you want to remove this book from the list?</p>
      </Modal>
    </div>
  </section>
</template>