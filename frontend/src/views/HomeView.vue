<script setup lang="ts">
    import { storeToRefs } from 'pinia'
    import { useAuthStore } from '@/stores/auth'

    const auth = useAuthStore()
    const { isLoggedIn } = storeToRefs(auth)
    console.log(isLoggedIn.value)
</script>

<template>
    <h1>Home</h1> 
</template>
