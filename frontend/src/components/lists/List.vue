<script setup lang="ts">
  import { defineProps, ref, computed, watchEffect } from 'vue';
  import api from '@/api';
  import { RouterLink, useRouter } from 'vue-router';
  import { useAuthStore } from '@/stores/auth';
  import { useModal } from '@/composables/useModal';
  import ConfirmModal from '../ConfirmModal.vue';
  import AuthModal from '@/components/AuthModal.vue';

  const router = useRouter();

  interface UserType {
      id: number;
      username: string;
      profile_picture: string;
  }

  interface BookDetails {
      id: number;
      ol_id: string;
      title: string;
      author_name?: string;
      cover_url?: string;
  }

  const props = defineProps<{
      list: {
          id: number;
          name: string;
          description: string;
          author: UserType;
          created_at: string;
          items: {
            id: number;
            book: number;
            added_at: string;
            bookDetails?: BookDetails;
          }[];
      };
  }>();

  const auth = useAuthStore();
  const showLoginPrompt = ref(false);
  const error = ref<string | null>(null);
  const emit = defineEmits<{
    (e: 'deleted', id: number): void;
  }>();

  const canDelete = computed(() => {
    return auth.user?.username === props.list.author.username || auth.user?.isModerator;
  });

  const { isOpen, open, close } = useModal();

  async function deleteList() {
    try {
      await api.delete(`/user/booklists/${props.list.id}/`);
      emit('deleted', props.list.id);
      close();
      window.location.reload();
    } catch (error) {
      console.error('Failed to delete list:', error);
    }
  }

  async function fetchBookDetails(item: { book: number; bookDetails?: BookDetails }) {
      try {
          const response = await api.get(`/library/books/${item.book}/`);
          item.bookDetails = response.data;
      } catch (error) {
          console.error('Error fetching book details:', error);
      }
  }

  watchEffect(() => {
      if (props.list.items?.length) {
          props.list.items.forEach(item => {
              if (!item.bookDetails) {
                  fetchBookDetails(item);
              }
          });
      }
  });

  const coverUrls = computed(() =>
      props.list.items
          .map(item => item.bookDetails?.cover_url)
          .slice(0, 6)
  );

  async function bookmark() {
    if (!auth.user?.id) {
      showLoginPrompt.value = true;
      return;
    }

    try {
      await api.post(`/user/booklists/${props.list.id}/bookmark/`);
      router.push(`/users/${auth.user.username}`);
    } catch (err) {
      error.value = 'Failed to bookmark the list.';
    }
  }
</script>

<template>
  <div class="relative border-background rounded shadow p-6 bg-background hover:border-blue-300 border-4 flex flex-col items-center text-center">
    <button
      v-if="canDelete"
      @click="() => open()"
      class="absolute top-2 right-2 border hover:bg-red-700 border-red-700 text-red-700 hover:text-white rounded-full w-8 h-8 flex justify-center text-lg font-bold"
      title="Delete list"
      aria-label="Delete list"
    >
      x
    </button>

    <h3 class="text-xl font-semibold mb-1 text-white">{{ list.name }}</h3>

    <div class="flex items-center gap-2 mb-2">
      <img
        src="/def.jpg"
        alt="Profile picture"
        class="w-6 h-6 rounded-full object-cover"
      />
      <p class="text-gray-300 text-sm">{{ list.author.username }}</p>
    </div>

    <div class="h-[22rem] w-[26rem] relative border border-secondary-light bg-sideground rounded-lg m-2 p-4">
      <div v-if="coverUrls.length" class="grid grid-cols-3 gap-2 mb-4 h-full">
        <img
          v-for="(url, index) in coverUrls"
          :key="index"
          :src="url"
          alt="Book cover"
          class="w-full h-40 object-cover rounded text-secondary-default"
        />
      </div>
      <div v-else class="flex items-center justify-center h-full">
        <p class="text-gray-400 text-sm">No books in this list yet.</p>
      </div>
    </div>

    <div class="flex flex-wrap justify-center gap-2">
      <RouterLink
        :to="`/users/${list.author.username}/lists/${list.id}`"
        class="h-[36px] border border-green-500 text-green-500 hover:bg-green-500 hover:text-white px-4 py-1.5 rounded-lg text-sm transition"
      >
        Read More
      </RouterLink>
      <button
      @click="bookmark"
        class="h-[36px] border border-blue-400 text-blue-400 hover:bg-blue-400 hover:text-white px-4 py-1.5 rounded-lg text-sm transition"
      >
        Bookmark
      </button>
    </div>

    <AuthModal
      :show="showLoginPrompt"
      @close="showLoginPrompt = false"
      @login="router.push({ name: 'Login' });"
      @register="router.push({ name: 'Register' })"
    />
    <ConfirmModal
      :show="isOpen"
      title="Confirm Deletion"
      :message="`Are you sure you want to delete the list '${list.name}'? This action cannot be undone.`"
      @close="close"
      @confirm="deleteList"
    />
  </div>
</template>