<script setup lang="ts">
    import { ref, computed, defineProps, withDefaults } from 'vue';
    import List from '@/components/lists/List.vue'

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

    interface ListType {
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
    }

    const props = withDefaults(
        defineProps<{
          results: ListType[];
          isLoading: boolean;
          limit?: number;
          context?: 'user' | 'search';
          canCreate?: boolean;
          username?: string;
        }>(),
        {
          limit: 12,
          context: 'search',
          canCreate: false,
        }
    );

    const visibleCount = ref(props.limit);
    const paginatedResults = computed(() =>
      props.results.slice(0, visibleCount.value)
    );

    function loadMore() {
      visibleCount.value += props.limit;
    }
</script>

<template>
    <section class="bg-background px-4 py-10">
      <div class="container-xl lg:container m-auto">
        <div class="flex items-center justify-between mb-6">
          <h2 class="text-3xl font-bold text-secondary-light mb-6 text-center">Results</h2>
          <RouterLink
            v-if="canCreate"
            :to="`/users/${props.username}/lists/create`"
            class="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded"
          >
            + Create New List
          </Routerlink>
        </div>

        <div v-if="!props.isLoading && props.results.length === 0" class="text-center text-gray-500">
          No results found.
        </div>

        <div class="grid xl:grid-cols-2 grid-cols-1 gap-6">
          <List
            v-for="list in paginatedResults"
            :key="list.id"
            :list="list"
          />
        </div>
        
        <div v-if="visibleCount < props.results.length" class="text-center mt-4">
          <button
            @click="loadMore"
            class="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded">
            Load More
          </button>
        </div>
      </div>
    </section>
</template>