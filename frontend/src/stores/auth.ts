import { defineStore } from 'pinia'
import { ACCESS_TOKEN, REFRESH_TOKEN, CURRENT_USER } from '@/constants'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: localStorage.getItem('ACCESS_TOKEN') || null,
    user: null as null | {
      id: number,
      username: string,
      profilePicture: string,
      bio: string,
      isModerator: boolean,
      isBanned: boolean,
    },
  }),
  getters: {
    isLoggedIn: (state) => !!state.token,
  },
  actions: {
    setToken(newToken: string, userData?: typeof this.user) {
      this.token = newToken
      localStorage.setItem('ACCESS_TOKEN', newToken)

      if (userData) {
        this.user = userData
        localStorage.setItem('CURRENT_USER', JSON.stringify(userData))
      }
    },
    setUser(userData: typeof this.user) {
      this.user = userData
      localStorage.setItem('CURRENT_USER', JSON.stringify(userData))
    },
    clearAuth() {
      this.token = null
      this.user = null
      localStorage.removeItem('ACCESS_TOKEN')
      localStorage.removeItem('CURRENT_USER')
    },
    loadAuthFromStorage() {
      const storedToken = localStorage.getItem(ACCESS_TOKEN);
      const storedUser = localStorage.getItem(CURRENT_USER);
    
      if (storedToken) this.token = storedToken;
    
      if (storedUser) {
        try {
          this.user = JSON.parse(storedUser);
        } catch (e) {
          console.error("Failed to parse user from localStorage:", e);
          this.user = null;
        }
      }
    
      if (this.token && !this.user) {
        this.fetchUser();
      }
    },
    async fetchUser() {
      if (!this.token || !this.user?.username) return

      try {
        const backendUrl = import.meta.env.VITE_BACKEND_URL
        const res = await fetch(`${backendUrl}/api/user/${this.user.username}/`, {
          headers: {
            Authorization: `Bearer ${this.token}`,
          },
        })

        if (res.ok) {
          const data = await res.json()
          this.setUser(data)
        } else {
          this.clearAuth()
        }
      } catch {
        this.clearAuth()
      }
    },
  },
})