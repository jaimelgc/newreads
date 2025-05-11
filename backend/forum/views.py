from drf_yasg.utils import swagger_auto_schema
from library.open_library import get_or_create_book
from rest_framework import viewsets

from .models import Post
from .serializers import CommentSerializer, PostSerializer


@swagger_auto_schema(operation_description="CRUD Post View")
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        ol_id = self.request.data.get('ol_id')
        book = get_or_create_book(ol_id) if ol_id else None
        serializer.save(poster=self.request.user, book=book)


@swagger_auto_schema(operation_description="CRUD Comment View")
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        original_post = self.request.data.get('original_post')
        serializer.save(poster=self.request.user, original_post=original_post)
