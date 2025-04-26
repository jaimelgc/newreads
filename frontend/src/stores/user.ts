// stores/userStore.ts
import { defineStore } from 'pinia';

export const useUserStore = defineStore('user', {
  state: () => ({
    id: null as number | null,
    username: '',
    profilePicture: '',
    bio: '',
    isModerator: false,
  }),
  actions: {
    setUser(userData: {
      id: number;
      username: string;
      profile_picture: string;
      bio: string;
      is_moderator: boolean;
    }) {
      this.id = userData.id;
      this.username = userData.username;
      this.profilePicture = userData.profile_picture;
      this.bio = userData.bio;
      this.isModerator = userData.is_moderator;
    },
    clearUser() {
      this.id = null;
      this.username = '';
      this.profilePicture = '';
      this.bio = '';
      this.isModerator = false;
    },
  },
});