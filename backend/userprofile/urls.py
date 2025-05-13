from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (  # UserBookListsView,
    BookListItemViewSet,
    BookListViewSet,
    ProfileView,
    RegisterView,
    UserViewSet,
)

router = DefaultRouter()
router.register(r'blitems', BookListItemViewSet, basename='blitems')
router.register(r'booklists', BookListViewSet, basename='booklist')
router.register(r'', UserViewSet, basename='user')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('', include(router.urls)),
]
