from django.urls import path

from . import views

urlpatterns = [
    path('test/work/<str:ol_id>/', views.test_fetch_work, name='test_fetch_work'),
    path('test/book/<str:isbn>/', views.test_fetch_book, name='test_fetch_book'),
    path('test/author/<str:ol_id>/', views.test_fetch_author, name='test_fetch_author'),
]
