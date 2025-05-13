from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BookViewSet, GetOrCreateBookView, OpenLibrarySearchView

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')

urlpatterns = [
    path('search/', OpenLibrarySearchView.as_view(), name='search_and_catch'),
    path('getbook/<str:ol_id>/', GetOrCreateBookView.as_view(), name='get_or_create_book'),
    path('', include(router.urls)),
]
