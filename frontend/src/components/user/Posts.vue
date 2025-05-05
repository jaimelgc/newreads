<script setup lang="ts">
    import { ref, computed, defineProps, withDefaults } from 'vue';
    import Post from './Post.vue';

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

    interface PostType {
        id: number;
        title: string;
        author: UserType;
        created_at: string;
        book: EditionType;
        comments: PostType[];
    }

    const props = withDefaults(
        defineProps<{
            results: PostType[];
            isLoading: boolean;
            limit?: number;
        }>(),
        {
            limit: 20,
        }
    );
    console.log("props", props)

    const visibleCount = ref(props.limit);
    const paginatedResults = computed(() =>
      props.results.slice(0, visibleCount.value)
    );

    function loadMore() {
      visibleCount.value += props.limit;
    }
</script>

<template>
    <section class="bg-blue-50 px-4 py-10">
    <div class="container-xl lg:container m-auto">
      <h2 class="text-3xl font-bold text-green-500 mb-6 text-center">Results</h2>


      <div v-if="!props.isLoading && props.results.length === 0" class="text-center text-gray-500">
        No results found.
      </div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
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