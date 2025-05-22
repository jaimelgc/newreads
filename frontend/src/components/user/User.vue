<script setup lang="ts">
import { defineProps } from 'vue';

const props = defineProps<{
    user: {
        id: number;
        username: string;
        profile_picture: string;
        bio: string;
        is_moderator?: boolean;
        is_banned?: boolean;
    };
}>();
</script>

<template>
    <div class="bg-white shadow-md rounded-2xl overflow-hidden flex flex-col items-center text-center p-6">
        <img
            src="/def.jpg"
            alt="Profile picture"
            class="w-24 h-24 rounded-full object-cover border-4 border-secondary-light mb-4"
        />
        <h3 class="text-xl font-bold text-gray-800">{{ user.username }}</h3>
        <div class="text-sm mt-1">
            <span v-if="user.is_moderator" class="text-green-600 font-semibold">Moderator</span>
            <span v-if="user.is_banned" class="text-red-600 font-semibold ml-2">Banned</span>
        </div>
        <p class="text-gray-600 mt-3 line-clamp-3">
            {{ user.bio || 'No bio available.' }}
        </p>
        <RouterLink
            :to="`/users/${user.username}`"
            class="mt-4 inline-block bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-lg text-sm transition">
            View Profile
        </RouterLink>
    </div>
</template>
