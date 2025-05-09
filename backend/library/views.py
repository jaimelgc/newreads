# from django.db.models import Q
from rest_framework import permissions, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

# from .models import Book
from .open_library import get_catch_data, get_or_create_book
from .serializers import BookSerializer


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


class GetOrCreateBookView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, ol_id):
        try:
            book = get_or_create_book(ol_id)
        except ValueError as e:
            return Response({'detail': str(e)}, status=status.HTTP_404_NOT_FOUND)

        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
