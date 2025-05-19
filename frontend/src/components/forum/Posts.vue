<script setup lang="ts">
    import Post from './Post.vue';
    import { ref, computed, defineProps, withDefaults } from 'vue';

    interface PostType {
        id: number;
        title: string;
        poster: { username: string } | null;
        created_at: string;
    }

    const props = withDefaults(
        defineProps<{
            results: PostType[];
            isLoading: boolean;
            limit?: number;
            method: string;
        }>(),
        {
            limit: 12,
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
  <section class="bg-background min-h-screen px-4 py-10">
    <div class="container-xl lg:container m-auto w-full">
      <h2 class="text-3xl font-bold text-secondary-default mb-6 text-center">{{ props.method }}</h2>

      <div v-if="props.isLoading" class="text-center text-gray-500 py-6">
        Loading...
      </div>

      <div v-if="!props.isLoading && props.results.length === 0" class="text-center text-gray-500">
        No posts found.
      </div>

      <div class="flex flex-col gap-4">
        <Post
          v-for="post in paginatedResults"
          :key="post.id"
          :post="post"
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

