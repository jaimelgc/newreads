<script setup lang="ts">
    import { ref, computed, defineProps, withDefaults } from 'vue';
    import User from '@/components/user/User.vue';
   
    interface UserType {
      id: number;
      username: string;
      profile_picture: string;
      bio: string;
      is_moderator?: boolean;
      is_banned?: boolean;
    }

    const props = withDefaults(
        defineProps<{
            results: UserType[];
            isLoading: boolean;
            limit?: number;
        }>(),
        {
            limit: 12,
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
    <section class="min-h-screen bg-background text-white px-4 py-10">
    <div class="container-xl lg:container m-auto">
      <h2 class="text-3xl font-bold text-secondary-light mb-6 text-center">Results</h2>


      <div v-if="!props.isLoading && props.results.length === 0" class="text-center text-gray-500">
        No results found.
      </div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <User
          v-for="user in paginatedResults"
          :key="user.id"
          :user="user"
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