import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: localStorage.getItem('ACCESS_TOKEN') || null,
    user: null as null | { id: number, username: string, name: string },
  }),
  getters: {
    isLoggedIn: (state) => !!state.token,
    loggedInUser: (state) => state.user,
  },
  actions: {
    setToken(newToken: string) {
      this.token = newToken
      localStorage.setItem('ACCESS_TOKEN', newToken)
    },
    clearAuth() {
      this.token = null
      this.user = null
      localStorage.removeItem('ACCESS_TOKEN')
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