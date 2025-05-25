<script setup lang="ts">
    import { ref, reactive, defineProps } from 'vue';
    import { useRoute } from 'vue-router';
    import router from '@/router';
    import { ACCESS_TOKEN, REFRESH_TOKEN, CURRENT_USER } from '@/constants';
    import api from '@/api';
    import { useAuthStore } from '@/stores/auth';
    import apiFree from '@/f-api';
    import type { AxiosError } from 'axios';

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
        confirmPassword: '',
        isLoading: false,
        error: ''
    });

    const showPassword = ref(false);

    const isPasswordStrong = (password: string) => {
        return password.length >= 8 &&
            /[a-z]/.test(password) &&
            /[A-Z]/.test(password) &&
            /[0-9]/.test(password);
    };

    const handleSubmit = async () => {
        form.isLoading = true;

        const newUser: Record<string, string> = {
            username: form.username,
            password: form.password
        };

        if (props.method === 'register') {
            newUser.email = form.email;
        }

        if (!form.username || !form.password || (props.method === 'register' && (!form.email || !form.confirmPassword))) {
            form.error = 'Please fill in all required fields.';
            form.isLoading = false;
            return;
        }

        if (props.method === 'register' && form.password !== form.confirmPassword) {
            form.error = 'Passwords do not match.';
            form.isLoading = false;
            return;
        }

        if (props.method === 'register' && !isPasswordStrong(form.password)) {
            form.error = 'Password must be at least 8 characters long and include upper/lowercase letters and a number.';
            form.isLoading = false;
            return;
        }

        try {
            if (props.method === 'login') {
                const response = await api.post(endpoint, newUser);

                const auth = useAuthStore();
                auth.setToken(response.data.access);
                localStorage.setItem(ACCESS_TOKEN, response.data.access);
                localStorage.setItem(REFRESH_TOKEN, response.data.refresh);
                localStorage.setItem(CURRENT_USER, JSON.stringify(newUser));
                
                const res = await api.get(`/user/${newUser.username}/`);
                auth.setUser(res.data);

                router.push('/');
            } else {
                const response = await apiFree.post(endpoint, newUser);
                router.push('/login');
            }
        } catch (err) {
            const error = err as AxiosError<any>;
            if (error.response?.data) {
                const data = error.response.data;
                if (data.detail) {
                    form.error = data.detail;
                } else if (typeof data === 'object') {
                    form.error = Object.values(data).flat().join(' ');
                } else {
                    form.error = 'An error occurred. Please try again.';
                }
            } else {
                form.error = 'An unexpected error occurred.';
            }

            console.error('Error:', error);
        }
    };
</script>

<template>
    <form @submit.prevent="handleSubmit" class="min-h-screen  flex justify-center items-center bg-background">
        <div class="w-full max-w-sm">
            <h2 class="text-3xl text-center text-secondary-light font-semibold mb-6 mt-10">{{ title }}</h2>
            <p v-if="form.error" class="text-red-500 text-sm mb-4">{{ form.error }}</p>
            <div class="mb-4">
                <label class="block text-gray-200 font-bold mb-2">
                    Username
                </label>
                <input v-model="form.username"
                    type="text"
                    id="username"
                    name="username"
                    class="border rounded w-full py-2 px-3 mb-2 "
                    required/>
                <p></p>
                <div v-if="props.method === 'register'" class="mb-4">
                    <label class="block text-gray-200 font-bold mb-2 ">
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
                <label class="block text-gray-200 font-bold mb-2">
                    Password
                </label>
                
                <div class="relative">
                    <input
                        v-model="form.password"
                        :type="showPassword ? 'text' : 'password'"
                        id="password"
                        name="password"
                        class="border rounded w-full py-2 px-3 mb-2 pr-10"
                        required
                    />
                    <button
                        type="button"
                        @click="showPassword = !showPassword"
                        class="absolute inset-y-0 right-0 px-3 text-sm text-gray-600 focus:outline-none"
                    >
                        {{ showPassword ? 'Hide' : 'Show' }}
                    </button>
                </div>
                
                <div v-if="props.method === 'register'" class="relative">
                    <label class="block text-gray-200 font-bold mb-2">
                        Confirm password
                    </label>
                    <input
                        v-model="form.confirmPassword"
                        :type="showPassword ? 'text' : 'password'"
                        id="confirmPassword"
                        name="confirmPassword"
                        class="border rounded w-full py-2 px-3 mb-2 pr-10"
                        required
                    />
                    <button
                        type="button"
                        @click="showPassword = !showPassword"
                        class="absolute inset-y-0 right-0 px-3 text-sm text-gray-200 focus:outline-none"
                    >
                        {{ showPassword ? 'Hide' : 'Show' }}
                    </button>
                </div>
                <p class="text-gray-200">8 chars, upper and lower case and numbers</p>
                <button class="border border-secondary-light hover:bg-secondary-light text-secondary-light hover:text-white mt-3 font-bold py-2 px-4 rounded-full w-full focus:outline-none focus:shadow-outline" type="submit">
                    {{ title }}
                </button>
            </div>
        </div>
    </form>
</template>