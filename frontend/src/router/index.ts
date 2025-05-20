import { createRouter, createWebHistory } from 'vue-router'
import LibraryView from '@/views/library/LibraryView.vue'
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
import ListSearchView from '@/views/list/ListSearchView.vue'
import SearchView from '@/views/library/SearchView.vue'
import ForumListView from '@/views/forum/ForumListView.vue'
import ForumDetailView from '@/views/forum/ForumDetailView.vue'
import CreatePostView from '@/views/forum/CreatePostView.vue'
import PostSearchView from '@/views/forum/PostSearchView.vue'
import UserSearchView from '@/views/user/UserSearchView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
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
      path: '/books/:id',
      name: 'BookDetail',
      component: BookDetailView,
    },
    {
      path: '/',
      name: 'Library',
      component: LibraryView,
    },
    {
      path: '/search',
      name: 'SearchView',
      component: SearchView,
    },
    {
      path: '/forum/search',
      name: 'PostSearchView',
      component: PostSearchView,
    },
    {
      path: '/booklists/search',
      name: 'ListSearchView',
      component: ListSearchView,
    },    {
      path: '/users/search',
      name: 'UserSearchView',
      component: UserSearchView,
    },
    { 
      path: '/forum', 
      name: 'ForumList', 
      component: ForumListView 
    },
    { 
      path: '/:username/forum/new', 
      name: 'CreatePostView', 
      component: CreatePostView 
    },
    { 
      path: '/post/:id', 
      name: 'PostDetail', 
      component: ForumDetailView 
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
    },
    {
      path: '/users/:username',
      name: 'UserDetailView',
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
