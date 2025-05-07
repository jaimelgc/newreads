<script setup lang="ts">
    import { ref, computed, defineProps, withDefaults } from 'vue';
    import List from '@/components/user/List.vue'

    interface UserType {
        id: number;
        name: string;
        profile_picture: string;
    }
   
    interface EditionType {
        key: string;
        title: string;
        author_name?: string[];
        first_publish_year?: number;
        cover_i?: number;
        publishers?: string[];
        number_of_pages?: number;
        by_statement?: string;
        cover_edition_key?: string, 
    }

    interface ListType {
        id: number;
        title: string;
        author: UserType;
        created_at: string;
        books: EditionType[];
    }

    const props = withDefaults(
        defineProps<{
          results: ListType[];
          isLoading: boolean;
          limit?: number;
          context?: 'user' | 'search';
          canCreate?: boolean;
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

    const sectionTitle = computed(() => {
      if (props.context === 'user') {
        return props.canCreate ? 'My Lists' : "User's Lists";
      }
      return 'Search Results';
    });

    function loadMore() {
      visibleCount.value += props.limit;
    }
</script>

<template>
    <section class="bg-blue-50 px-4 py-10">
      <div class="container-xl lg:container m-auto">
        <div class="flex items-center justify-between mb-6">
          <h2 class="text-3xl font-bold text-green-500 mb-6 text-center">Results</h2>
          <button
            v-if="canCreate"
            class="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded"
          >
            + Create New List
          </button>
        </div>

        <div v-if="!props.isLoading && props.results.length === 0" class="text-center text-gray-500">
          No results found.
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
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