from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer, CommentSerializer

from library.open_library import get_or_create_book

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        ol_id = self.request.data.get('ol_id')
        book = get_or_create_book(ol_id) if ol_id else None
        serializer.save(poster=self.request.user, book=book)