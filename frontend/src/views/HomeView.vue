<script setup lang="ts">
    import { storeToRefs } from 'pinia'
    import { useAuthStore } from '@/stores/auth'

    const auth = useAuthStore()
    const { isLoggedIn, loggedInUser } = storeToRefs(auth)
    console.log(isLoggedIn.value)
    console.log(loggedInUser.value)
</script>

<template>
    <h1>Home</h1> 
</template>
