<script setup lang="ts">
    import Book from './Book.vue';
    import { onMounted, reactive, defineProps, withDefaults } from 'vue';
    import api from '@/api';
   
    interface BookType {
        key: string;
        title: string;
        author_name?: string[];
        first_publish_year?: number;
        cover_i?: number;
    }

    const props = withDefaults(
        defineProps<{
            results: BookType[];
            isLoading: boolean;
            limit?: number;
            showButton?: boolean;
        }>(),
        {
            limit: 10,
            showButton: false,
        }
    );

    const state = reactive({
        books: [],
        isLoading: true
    });

    console.log("it gets to books.vue");
</script>

<template>
    <section class="bg-blue-50 px-4 py-10">
    <div class="container-xl lg:container m-auto">
      <h2 class="text-3xl font-bold text-green-500 mb-6 text-center">Results</h2>

      <!-- <div v-if="props.isLoading" class="text-center text-gray-500 py-6">
        <PulseLoader />
      </div> -->

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <Book
          v-for="book in props.results.slice(0, props.limit)"
          :key="book.key"
          :book="book"
        />
      </div>

      <div v-if="props.showButton" class="text-center mt-6">
        <button class="btn btn-primary">Show More</button>
      </div>
    </div>
    </section>

    <section v-if="showButton" class="m-auto max-w-lg my-10 px-6">
      <RouterLink to="/jobs" class="block bg-black text-white text-center py-4 px-6 rounded-xl hover:bg-gray-700"
        >View All Jobs
      </RouterLink>
    </section>
</template>