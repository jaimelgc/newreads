import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LibraryView from '@/views/LibraryView.vue'
import ForumView from '@/views/ForumView.vue'
import UserDetailView from '@/views/UserDetailView.vue'
import NotFoundView from '@/views/NotFoundView.vue'
import BookSearch from '@/views/BookSearch.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/library/search',
      name: 'book-search',
      component: BookSearch,
    },
    {
      path: '/library',
      name: 'library',
      component: LibraryView,
    },
    {
      path: '/forum',
      name: 'forum',
      component: ForumView,
    },
    {
      path: '/user/register',
      name: 'user',
      component: UserDetailView,
    },
    {
      path: '/user/login',
      name: 'user',
      component: UserDetailView,
    },
    {
      path: '/user',
      name: 'user',
      component: UserDetailView,
    },
    {
      path: '/:catchAll(.*)',
      name: 'not-found',
      component: NotFoundView,
    },
  ],
})

export default router
