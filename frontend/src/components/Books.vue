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
            showButton?: boolean; // vestigial
        }>(),
        {
            limit: 10,
            showButton: false,
        }
    );
    console.log("props", props)

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
          :book="book"
        />
        <!-- :key="book.key" -->
      </div>
    </div>
    </section>
</template>