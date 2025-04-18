from django.urls import path

from . import views

urlpatterns = [
    path('search', views.OpenLibrarySearchView, name='search_and_catch'),
]
