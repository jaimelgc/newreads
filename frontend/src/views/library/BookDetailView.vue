<script setup lang="ts">
    import { onMounted, ref } from 'vue';
    import { useRoute } from 'vue-router';
    import axios from 'axios';
    import { useApiSearch } from '@/search';

    const route = useRoute();
    const editionId = route.params.id as string;

    const edition = ref<any>(null);
    const work = ref<any>(null);
      const editions = ref<any>(null);

    const { results, error, isLoading, fetchData } = useApiSearch()

    onMounted(async () => {

      await fetchData('/api/library/search/', {
        key: `edition-search-${editionId}`,
        url: `https://openlibrary.org/books/${editionId}.json`,
      });
      edition.value = results.value;

      const workKey = edition.value?.works?.[0]?.key;

      if (workKey) {
        await fetchData('/api/library/search/', {
          key: `work-get-${workKey}`,
          url: `https://openlibrary.org${workKey}.json`,
        });
        work.value = results.value;
        console.log(work)

        await fetchData('/api/library/search/', {
            key: `work-get-${workKey}`,
            url: `https://openlibrary.org${workKey}editions.json?limit=10`,
          });
          editions.value = results.value;
          console.log(editions)
        }
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
    <div>
      {{ work.json }}
    </div>
    <div>
      {{ editions.json }}
    </div>
  </div>
</template>