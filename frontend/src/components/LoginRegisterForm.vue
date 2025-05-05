<script setup lang="ts">
    import { reactive } from 'vue';
    import { useRoute } from 'vue-router';
    import router from '@/router';
    import { ACCESS_TOKEN, REFRESH_TOKEN, CURRENT_USER } from '@/constants';
    import api from '@/api';
    import { useUserStore } from '@/stores/user';
    import { useAuthStore } from '@/stores/auth';
    import axios from 'axios';

    const route = useRoute();

    const props = defineProps<{
        method: 'login' | 'register';
        hasLoggedOut: boolean;
    }>();

    const title = props.method === 'login' ? 'Login' : 'Sign Up';
    const endpoint = props.method === 'login' ? '/api/token/' : '/user/register/';

    const form = reactive({
        username: '',
        email: '',
        password: '',
        isLoading: false
    });

    const handleSubmit = async () => {
        form.isLoading = true;

        const newUser: Record<string, string> = {
            username: form.username,
            password: form.password
        };

        if (props.method === 'register') {
            newUser.email = form.email;
        }

        try {
            // IF LOGIN POSTS TO TOKEN IF REGISTER POSTS TO REGISTER
            const response = await api.post(endpoint, newUser);

            if (props.method === 'login') {

                const auth = useAuthStore();
                auth.setToken(response.data.access);
                localStorage.setItem(ACCESS_TOKEN, response.data.access);
                localStorage.setItem(REFRESH_TOKEN, response.data.refresh);

                const res = await api.get(`/user/${newUser.username}/`);
                console.log("res", res.data)
                localStorage.setItem(CURRENT_USER, JSON.stringify(res.data));
                console.log('Data:', response);
                router.push('/');
                

            } else {
                const dataUser = await api.get(`/user/${newUser.username}/`, newUser);
                const userStore = useUserStore();
                userStore.setUser(dataUser.data);
                router.push('/login');
            }
        } catch (error) {
            console.error('Error:', error);
        } finally {
            form.isLoading = false;
        }
    };
</script>

<template>
    <form @submit.prevent="handleSubmit">
        <h2 class="text-3xl text-center font-semibold mb-6">{{ title }}</h2>
        <div class="mb-4">
            <label class="block text-gray-700 font-bold mb-2">
                Username
            </label>
            <input v-model="form.username"
                type="text"
                id="username"
                name="username"
                class="border rounded w-full py-2 px-3 mb-2"
                required/>
            <p></p>
            <div v-if="props.method === 'register'" class="mb-4">
                <label class="block text-gray-700 font-bold mb-2">
                    Email
                </label>
                <input v-model="form.email"
                    type="email"
                    id="email"
                    name="email"
                    class="border rounded w-full py-2 px-3 mb-2"
                    required />
            </div>
            <p></p>
            <label class="block text-gray-700 font-bold mb-2">
                Password
            </label>
            <input v-model="form.password"
                type="password"
                id="password"
                name="password"
                class="border rounded w-full py-2 px-3 mb-2"
                required/>
            <p></p>
            <button class="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-full w-full focus:outline-none focus:shadow-outline" type="submit">
                {{ title }}
            </button>
        </div>
    </form>
</template>