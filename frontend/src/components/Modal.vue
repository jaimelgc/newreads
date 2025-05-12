<script setup lang="ts">
    defineProps<{ show: boolean }>()
    defineEmits(['close', 'confirm'])
</script>

<template>
    <Teleport to="body">
        <div v-if="show" class="fixed inset-0 bg-black bg-opacity-40 flex items-center justify-center z-50">
        <div class="bg-white rounded-lg p-6 w-full max-w-md shadow-xl">
            <slot />
            <div class="mt-4 text-right space-x-2">
                <button @click="$emit('close')" class="px-4 py-2 border rounded">Cancel</button>
                <button @click="$emit('confirm')" class="px-4 py-2 bg-blue-600 text-white rounded">Confirm</button>
            </div>
        </div>
        </div>
    </Teleport>
</template>
  
