<script setup lang="ts">
    import { defineProps, computed } from 'vue';

    const props = defineProps<{
        user: {
            id: number;
            name: string;
            profile_picture: string;
            bio: string;
        };
    }>();

</script>

<template>
    <div class="border rounded shadow p-4 bg-white">
        <!-- <img :src="coverUrl" alt="Edition Cover" class="mb-4" /> -->
        <h3 class="text-xl font-semibold">{{ user.name }}</h3>
        <RouterLink
            :to="`/users/${user.name}`" 
            class="h-[36px] bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-lg text-center text-sm">
            
            Read More
        </RouterLink>
    </div>
</template>