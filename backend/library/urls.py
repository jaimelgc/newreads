from django.urls import path

from .views import GetOrCreateBookView, OpenLibrarySearchView

urlpatterns = [
    path('search/', OpenLibrarySearchView.as_view(), name='search_and_catch'),
    path('books/<str:ol_id>/', GetOrCreateBookView.as_view(), name='get_or_create_book'),
]
