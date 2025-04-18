from django.urls import path

from .views import OpenLibrarySearchView

urlpatterns = [
    path('search', OpenLibrarySearchView.as_view(), name='search_and_catch'),
]
