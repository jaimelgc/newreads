// stores/auth.ts
import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: localStorage.getItem('token') || null,
    user: null as null | { id: number, name: string },
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
      if (!this.token) return

      try {
        const res = await fetch('/api/user/', {
          headers: {
            Authorization: `Bearer ${this.token}`,
          },
        })
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