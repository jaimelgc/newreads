<script setup lang="ts">
    defineProps<{ 
        show: boolean; 
        title?: string; 
        message?: string; 
    }>();
    defineEmits(['close', 'confirm']);
</script>

<template>
    <Teleport to="body">
        <div v-if="show" class="fixed inset-0 bg-black bg-opacity-40 flex items-center justify-center z-50">
            <div class="bg-modal rounded-lg p-6 w-full max-w-md shadow-xl">
                <h2 class="text-lg text-white font-semibold mb-4">{{ title }}</h2>
                <p class="text-gray-200 mb-6">{{ message }}</p>
                <div class="mt-4 text-right space-x-2">
                    <button @click="$emit('close')" class="font-semibold text-white hover:text-black hover:bg-white px-4 py-2 border rounded">Cancel</button>
                    <button @click="$emit('confirm')" class="px-4 py-2 font-semibold border border-red-600 text-red-600 hover:bg-red-500 hover:text-white rounded">Confirm</button>
                </div>
            </div>
        </div>
    </Teleport>
</template>