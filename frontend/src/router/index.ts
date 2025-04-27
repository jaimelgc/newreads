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
      meta: { breadcrumb: 'Home' },
    },
    {
      path: '/register',
      name: 'Register',
      component: RegisterView,
      meta: { breadcrumb: 'Register' },
    },
    {
      path: '/login',
      name: 'Login',
      component: LoginView,
      meta: { breadcrumb: 'Login' },
    },
    {
      path: '/logout',
      name: 'Logout',
      component: LogoutView,
      meta: { breadcrumb: 'Logout' },
    },
    {
      path: '/library/search',
      name: 'BookSearch',
      component: BookSearchView,
      meta: { breadcrumb: 'Search' },
    },
    {
      path: '/library/:name',
      name: 'BookResults',
      component: BookResultsView,
      meta: { breadcrumb: ':name' },
    },
    {
      path: '/library/book/:id',
      name: 'BookDetail',
      component: BookDetailView,
      meta: { breadcrumb: 'Book' },
    },
    {
      path: '/library',
      name: 'Library',
      component: LibraryView, // BookSearchView
      meta: { breadcrumb: 'Library' },
    },
    {
      path: '/forum',
      name: 'Forum',
      component: ForumView,
      meta: { breadcrumb: 'Forum' },
    },
    {
      path: '/user/:id/edit',
      name: 'UserEdit',
      component: UserEditView,
      meta: { breadcrumb: 'Edit' },
    },
    {
      path: '/user/:name',
      name: 'UserDetail',
      component: UserDetailView,
      meta: { breadcrumb: ':name' },
    },
    {
      path: '/:catchAll(.*)',
      name: 'NotFound',
      component: NotFoundView,
      meta: { breadcrumb: 'NotFound' },
    },
  ],
})

export default router
