import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LibraryView from '@/views/library/LibraryView.vue'
import ForumView from '@/views/forum/ForumView.vue'
import UserDetailView from '@/views/user/UserDetailView.vue'
import NotFoundView from '@/views/NotFoundView.vue'
import RegisterView from '@/views/auth/RegisterView.vue'
import LoginView from '@/views/auth/LoginView.vue'
import LogoutView from '@/views/auth/LogoutView.vue'
import UserEditView from '@/views/user/UserEditView.vue'
import BookSearchView from '@/views/library/BookSearchView.vue'
import BookDetailView from '@/views/library/BookDetailView.vue'
import BookResultsView from '@/views/library/BookResultsView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView,
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/logout',
      name: 'logout',
      component: LogoutView,
    },
    {
      path: '/library/search',
      name: 'book-search',
      component: BookSearchView,
    },
    {
      path: '/library/:name',
      name: 'library',
      component: BookResultsView,
    },
    {
      path: '/library/book/:id',
      name: 'library',
      component: BookDetailView,
    },
    {
      path: '/library',
      name: 'library',
      component: LibraryView, // BookSearchView
    },
    {
      path: '/forum',
      name: 'forum',
      component: ForumView,
    },
    {
      path: '/user/:id/edit',
      name: 'user',
      component: UserEditView,
    },
    {
      path: '/user/:id',
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
