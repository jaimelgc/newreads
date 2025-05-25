# from django.db.models import Q
from rest_framework import permissions, status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .open_library import build_openlibrary_url, get_catch_data, get_or_create_book
from .serializers import BookSerializer


class OpenLibrarySearchView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        key = request.query_params.get("key", "")
        search_type = request.query_params.get("type", "search")
        query = request.query_params.get("q", "")
        page = int(request.query_params.get("page", 1))

        try:
            url = build_openlibrary_url(search_type, query, page)
        except ValueError:
            return Response({"error": "Invalid search type"}, status=400)

        data = get_catch_data(key, url)
        if data:
            return Response(data, status=200)

        return Response({"error": "Not found"}, status=404)


class GetOrCreateBookView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, ol_id):
        try:
            book = get_or_create_book(ol_id)
        except ValueError as e:
            return Response({'detail': str(e)}, status=status.HTTP_404_NOT_FOUND)

        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return [AllowAny()]
        return [IsAuthenticated()]
