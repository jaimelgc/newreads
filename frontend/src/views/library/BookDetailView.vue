<script setup lang="ts">
    import { onMounted, ref, computed } from 'vue';
    import { useRoute } from 'vue-router';
    import { useApiSearch } from '@/search';
    import Books from '@/components/library/Books.vue';

    const route = useRoute();
    const editionId = route.params.id as string;

    const edition = ref<any>(null);
    const work = ref<any>(null);
    const authors = ref<any[]>([]);
    const books = ref<any[]>([]); // To store the books for the selected author
    const selectedAuthorIndex = ref<number>(0); // Track which author is selected

    const { results: editionResults, error: ediitionError, isLoading: editionIsLoading, fetchData: editionFetchData } = useApiSearch();
    const { results: workResults, error: workError, isLoading: workIsLoading, fetchData: workFetchData } = useApiSearch();
    const { results: booksResults, error: booksError, isLoading: booksIsLoading, fetchData: booksFetchData } = useApiSearch();

    onMounted(async () => {
        // Fetch edition data
        await editionFetchData('/api/library/search/', {
            key: `edition-search-${editionId}`,
            url: `https://openlibrary.org/books/${editionId}.json`,
        });
        edition.value = editionResults.value;
        const workKey = edition.value?.works?.[0]?.key;

        if (workKey) {
            // Fetch work data
            await workFetchData('/api/library/search/', {
                key: `work-get-${workKey}`,
                url: `https://openlibrary.org/${workKey}.json`,
            });
            work.value = workResults.value;

            // Extract authors and initialize the first one
            authors.value = work.value.authors || [];
            if (authors.value.length > 0) {
                await fetchBooksForAuthor(authors.value[selectedAuthorIndex.value].author.key);
            }
        }
    });

    const fetchBooksForAuthor = async (authorKey: string) => {
      const formattedAuthorKey = authorKey.replace('/authors/', '');
      await booksFetchData('/api/library/search/', {
          key: `author-books-${formattedAuthorKey}`,
          url: `https://openlibrary.org/authors/${formattedAuthorKey}/works.json`,
      });
      books.value = booksResults.value?.entries || [];
      console.log('books', booksResults)
    };

    const selectedAuthor = computed(() => {
        return authors.value[selectedAuthorIndex.value];
    });
</script>

<template>
  <div v-if="edition && work">
    <h1 class="text-2xl font-bold mb-2">{{ edition.title }}</h1>
    <p class="text-gray-600">Published by: {{ edition.publishers?.join(', ') }}</p>
    <p class="text-gray-600">Published on: {{ edition.publish_date }}</p>

    <div class="mt-4">
      <h2 class="text-lg font-semibold">Description</h2>
      <p>{{ work.description?.value || work.description || 'No description available.' }}</p>
    </div>

    <!-- Tabs for Authors -->
    <div class="mt-4">
      <div class="flex space-x-4 border-b">
        <button 
          v-for="(author, index) in authors" 
          :key="author.author.key" 
          :class="{'border-b-2 border-blue-500': selectedAuthorIndex === index, 'text-gray-600': selectedAuthorIndex !== index}"
          class="py-2 px-4 font-semibold"
          @click="selectedAuthorIndex = index"
        >
          {{ author.author.name }}
        </button>
      </div>
    </div>

    <div v-if="books && books.length > 0">
      <Books :results="books" :isLoading="booksIsLoading" :limit="10" />
    </div>
    <div v-else>
      <p>No books available or still loading...</p>
    </div>
  </div>
</template>