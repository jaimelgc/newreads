from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    BookListViewSet,
    ProfileView,
    RegisterView,
    UserBookListsView,
    UserViewSet,
)

router = DefaultRouter()
router.register(r'', UserViewSet, basename='user')
router.register(r'booklists', BookListViewSet, basename='booklist')


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('<str:username>/lists/', UserBookListsView.as_view(), name='user-book-lists'),
    path('', include(router.urls)),
] + router.urls
