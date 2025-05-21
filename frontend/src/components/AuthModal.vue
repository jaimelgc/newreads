<script setup lang="ts">
    defineProps<{ show: boolean }>();
    defineEmits(['close', 'login', 'register']);
</script>

<template>
  <Teleport to="body">
    <div v-if="show" class="fixed inset-0 bg-black bg-opacity-40 flex items-center justify-center z-50">
      <div class="bg-modal rounded-lg p-6 w-full max-w-md shadow-xl">
        <h2 class="text-white text-lg font-semibold mb-4">You need to log in or register</h2>
        <p class="text-gray-200 mb-6">Please log in or create an account to add books to your lists.</p>
        <div class="mt-4 text-right space-x-2">
          <button @click="$emit('close')" class="text-white hover:text-black hover:bg-white px-4 py-2 border rounded">Cancel</button>
          <button @click="$emit('login')" class="px-4 py-2 font-semibold border border-blue-600 text-blue-600 hover:bg-blue-500 hover:text-white rounded">Log In</button>
          <button @click="$emit('register')" class="px-4 py-2 font-semibold border border-green-600 text-green-600 hover:bg-green-500 hover:text-white rounded">Register</button>
        </div>
      </div>
    </div>
  </Teleport>
</template>