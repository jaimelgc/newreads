from django.db.models import Q
from rest_framework import generics, permissions

from .models import Author, Book, Publisher, Subject, Work
from .serializers import (
    AuthorSerializer,
    BookSerializer,
    PublisherSerializer,
    SubjectSerializer,
    WorkSerializer,
)


class WorkSearchView(generics.ListAPIView):
    serializer_class = WorkSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        search_query = self.request.query_params.get('search', '')
        return Work.objects.filter(title__icontains=search_query)


class BookSearchView(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        search_query = self.request.query_params.get('search', '')
        return Book.objects.filter(title__icontains=search_query)


class AuthorSearchView(generics.ListAPIView):
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        search_query = self.request.query_params.get('search', '')
        return Author.objects.filter(name__icontains=search_query)


class PublisherSearchView(generics.ListAPIView):
    serializer_class = Publisher
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        search_query = self.request.query_params.get('search', '')
        return Publisher.objects.filter(name__icontains=search_query)


class SubjectSearchView(generics.ListAPIView):
    serializer_class = Subject
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        search_query = self.request.query_params.get('search', '')
        return Subject.objects.filter(name__icontains=search_query)
