# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render

# from .models import SearchHistory

# LAST search book function

from django.urls import path

from .views import register

urlpatterns = [
    path('register/', register, name='register'),
]
