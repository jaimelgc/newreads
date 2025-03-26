from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    BookListItemViewSet,
    BookListViewSet,
    SearchHistoryViewSet,
    UserViewSet,
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'booklists', BookListViewSet)
router.register(r'booklist-items', BookListItemViewSet)
router.register(r'search-history', SearchHistoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
