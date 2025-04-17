from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    BookListDetailView,
    ProfileView,
    RegisterView,
    UserBookListsView,
    UserPublicView,
    UserSearchView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('search/', UserSearchView.as_view(), name='user-search'),
    path('<str:username>/lists/', UserBookListsView.as_view(), name='user-lists'),
    path('<str:username>/', UserPublicView.as_view(), name='public_profile'),
    path('lists/<int:pk>', BookListDetailView.as_view(), name='detail-list'),
]
