# from django.db.models import Q
from rest_framework import generics, permissions, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Author, Book, Publisher, Subject, Work
from .open_library import get_catch_data
from .serializers import (
    AuthorSerializer,
    BookSerializer,
    PublisherSerializer,
    SubjectSerializer,
    WorkSerializer,
)

# Open library views
# ---------------------------------------------------------


class OpenLibrarySearchView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        url = request.query_params.get("url", "")
        key = request.query_params.get("key", "")
        page = int(request.query_params.get("page", 1))

        data = get_catch_data(key, url, page)
        if data:
            return Response(data, status=status.HTTP_200_OK)
        return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)


# Local database views
# ---------------------------------------------------------


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
    serializer_class = PublisherSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        search_query = self.request.query_params.get('search', '')
        return Publisher.objects.filter(name__icontains=search_query)


class SubjectSearchView(generics.ListAPIView):
    serializer_class = SubjectSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        search_query = self.request.query_params.get('search', '')
        return Subject.objects.filter(name__icontains=search_query)
