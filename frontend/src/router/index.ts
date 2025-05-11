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
import BookDetailView from '@/views/library/BookDetailView.vue'
import ListDetailView from '@/views/list/ListDetailView.vue'
import ListEditView from '@/views/list/ListEditView.vue'
import ListCreateView from '@/views/list/ListCreateView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
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
      path: '/books/:id',
      name: 'BookDetail',
      component: BookDetailView,
      meta: { breadcrumb: 'Book' },
    },
    {
      path: '/',
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
      path: '/users/:username/lists/:listId/edit',
      name: 'ListEdit',
      component: ListEditView
    },
    {
      path: '/users/:username/lists/:listId',
      name: 'ListDetail',
      component: ListDetailView
    },
    {
      path: '/users/:username/lists/create',
      name: 'ListCreate',
      component: ListCreateView
    },
    {
      path: '/users/:username/edit',
      name: 'UserEdit',
      component: UserEditView,
      meta: { breadcrumb: 'Edit' },
    },
    {
      path: '/users/:username',
      name: 'UserDetailView',
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
