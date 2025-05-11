<script setup lang="ts">
    import Book from '@/components/library/Book.vue';
    import { ref, computed, defineProps, withDefaults } from 'vue';
   
    interface BookType {
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
    }

    const props = withDefaults(
        defineProps<{
            results: BookType[];
            isLoading: boolean;
            limit?: number;
            showButton?: boolean; // vestigial
        }>(),
        {
            limit: 12,
            showButton: false,
        }
    );
    console.log("props", props)

    const filteredResults = computed(() =>
      props.results.filter(book =>
        book.cover_edition_key || book.edition_key?.[0] || book.ol_id
      )
    );
    const visibleCount = ref(props.limit);
    const paginatedResults = computed(() =>
    filteredResults.value.slice(0, visibleCount.value)
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
        <Book
          v-for="book in paginatedResults"
          :key="book.key || book.ol_id"
          :book="book"
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

      <!-- <div v-if="props.isLoading" class="text-center text-gray-500 py-6">
        <PulseLoader />
      </div> -->