<script setup lang="ts">
  import { onMounted, ref, computed, watchEffect } from 'vue';
  import { useRoute } from 'vue-router';
  import { useApiSearch } from '@/search';
  import Books from '@/components/library/Books.vue';
  import PulseLoader from 'vue-spinner/src/PulseLoader.vue';

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

  const route = useRoute();
  const editionId = route.params.id as string;

  const edition = ref<any>(null);
  const work = ref<any>(null);
  const authors = ref<any[]>([]);
  const selectedAuthorIndex = ref<number>(0);
  const isLoading = ref(true);

  const {
    results: editionResults,
    fetchData: fetchEdition,
  } = useApiSearch();

  const {
    results: workResults,
    fetchData: fetchWork,
  } = useApiSearch();

  const {
    results: booksResults,
    fetchData: fetchBooks,
    isLoading: booksIsLoading
  } = useApiSearch();

  const coverUrl = computed(() => {
    if (edition.value?.cover_url) return edition.value.cover_url;
    if (edition.value?.cover_i) return `https://covers.openlibrary.org/b/id/${edition.value.cover_i}-L.jpg`;
    if (edition.value?.covers?.length) return `https://covers.openlibrary.org/b/id/${edition.value.covers[0]}-L.jpg`;
  });

  const selectedAuthor = computed(() => authors.value[selectedAuthorIndex.value]);

  const fetchAuthorDetails = async (authorKey: string) => {
    const key = authorKey.replace('/authors/', '');
    const response = await fetch(`https://openlibrary.org/authors/${key}.json`);
    if (!response.ok) throw new Error('Failed to fetch author');
    return await response.json();
  };

  const fetchBooksForAuthor = async (authorKey: string, authorName: string) => {
    fetchBooks('/library/search/', {
        key: `book-search-${authorKey}`,
        type: 'author',
        q: authorName,
        });
  };

  onMounted(async () => {
    await fetchEdition('/library/search/', {
      key: `edition-${editionId}`,
      type: 'edition',
      q: editionId
    });
    edition.value = editionResults.value;
    const workKey = edition.value?.works?.[0]?.key;
    if (workKey) {
      await fetchWork('/library/search/', {
        key: `work-${workKey}`,
        type: 'work',
        q: workKey
      });
      work.value = workResults.value;
      const fullAuthors = await Promise.all(
        (work.value?.authors || []).map(async (a: any) => {
          const details = await fetchAuthorDetails(a.author.key);
          return { author: { key: a.author.key, name: details.name } };
        })
      );
      authors.value = fullAuthors;
      isLoading.value = false

      if (authors.value.length > 0) {
        const firstAuthor = authors.value[0].author;
        await fetchBooksForAuthor(firstAuthor.key.replace('/authors/', ''), firstAuthor.name);
      }
    }
  });
</script>

<template>
  <div v-if="isLoading" class="min-h-screen flex flex-col justify-center items-center text-gray-500 py-6">
    <p class="text-3xl font-semibold text-secondary-light">Loading Book</p>
    <PulseLoader />
  </div>
  <div v-if="edition && work" class="p-6">
    <div class="flex flex-col md:flex-row gap-6 mb-6">
      <div class="flex-shrink-0">
        <img :src="coverUrl" alt="Book Cover" class="w-48 h-auto rounded shadow-md" />
      </div>
      <div class="flex flex-col justify-between">
        <div>
          <h1 class="text-3xl font-bold mb-2 text-secondary-light">{{ edition.title }}</h1>
          <p class="text-gray-200 mb-1"><strong>Published by:</strong> {{ edition.publishers?.join(', ') || 'Unknown' }}</p>
          <p class="text-gray-200 mb-1"><strong>Published on:</strong> {{ edition.publish_date || 'Unknown' }}</p>
        </div>
        <div class="mt-4">
          <h2 class="text-lg font-semibold mb-1 text-gray-200">Description</h2>
          <p class="text-gray-200">
            {{ work.description?.value || work.description || 'No description available.' }}
          </p>
        </div>
      </div>
    </div>

    <div v-if="authors.length" class="mt-8">
      <h2 class="text-xl font-semibold mb-2 text-gray-200">Other Works by Author</h2>
      <div class="flex flex-wrap gap-4 border-b mb-4">
        <button
          v-for="(author, index) in authors"
          :key="author.author.key"
          @click="async () => {
            selectedAuthorIndex = index;
            const authorObj = authors[index].author;
            await fetchBooksForAuthor(authorObj.key.replace('/authors/', ''), authorObj.name);
          }"
          class="py-2 px-4 border-b-2 font-semibold transition-colors"
          :class="{
            'border-blue-500 text-blue-600': selectedAuthorIndex === index,
            'border-transparent text-gray-400 hover:text-blue-400': selectedAuthorIndex !== index
          }"
        >
          {{ author.author.name }}
        </button>
      </div>
    </div>

    <div v-if="booksResults?.length > 0">
      <Books :results="booksResults || []" :isLoading="booksIsLoading" :limit="6" method="author"/>
    </div>
    <div v-else class="text-gray-500">
      <p class="min-h-screen">No books available or still loading...</p>
    </div>
  </div>
</template>
