// stores/auth.ts
import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: localStorage.getItem('token') || null,
    user: null as null | { id: number, username: string, name: string },
  }),
  getters: {
    isLoggedIn: (state) => !!state.token,
  },
  actions: {
    setToken(newToken: string) {
      this.token = newToken
      localStorage.setItem('token', newToken)
    },
    clearAuth() {
      this.token = null
      this.user = null
      localStorage.removeItem('token')
    },
    async fetchUser() {
      if (!this.token || !this.user?.username) return;

      try {
        const backendUrl = import.meta.env.VITE_BACKEND_URL;
        const res = await fetch(`${backendUrl}/api/user/${this.user.username}/`, {
          headers: {
            Authorization: `Bearer ${this.token}`,
          },
        });

        if (res.ok) {
          this.user = await res.json()
        } else {
          this.clearAuth()
        }
      } catch (error) {
        this.clearAuth()
      }
    }
  }
})