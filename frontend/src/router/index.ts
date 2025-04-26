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
      name: 'Home',
      component: HomeView,
    },
    {
      path: '/register',
      name: 'Register',
      component: RegisterView,
    },
    {
      path: '/login',
      name: 'Login',
      component: LoginView,
    },
    {
      path: '/logout',
      name: 'Logout',
      component: LogoutView,
    },
    {
      path: '/library/search',
      name: 'BookSearch',
      component: BookSearchView,
    },
    {
      path: '/library/:name',
      name: 'BookResults',
      component: BookResultsView,
    },
    {
      path: '/library/book/:id',
      name: 'BookDetail',
      component: BookDetailView,
    },
    {
      path: '/library',
      name: 'Library',
      component: LibraryView, // BookSearchView
    },
    {
      path: '/forum',
      name: 'Forum',
      component: ForumView,
    },
    {
      path: '/user/:id/edit',
      name: 'UserEdit',
      component: UserEditView,
    },
    {
      path: '/user/:id',
      name: 'UserDetail',
      component: UserDetailView,
    },
    {
      path: '/:catchAll(.*)',
      name: 'NotFound',
      component: NotFoundView,
    },
  ],
})

export default router
