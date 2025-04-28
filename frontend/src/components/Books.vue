<script setup lang="ts">
    import Book from './Book.vue';
    import { onMounted, reactive } from 'vue';
    import api from '@/api';
   
    interface showButton {
        type: boolean
        default: false
    }

    const state = reactive({
        books: [],
        isLoading: true
    });

    const props = defineProps<{ showButton: showButton, limit: Number }>()

    onMounted(async () => {
        try {
            const response = await api.get('ruta');
            state.books = response.data;
        } catch (error) {
            console.error('Error fetching jobs');
        } finally {
            state.isLoading = false;
        }
    });
</script>

<template>
    <!-- <Book /> -->
</template>