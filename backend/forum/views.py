from library.open_library import get_or_create_book
from rest_framework import viewsets

from .models import Comment, Post
from .serializers import CommentSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        ol_id = self.request.data.get('ol_id')
        book = get_or_create_book(ol_id) if ol_id else None
        serializer.save(poster=self.request.user, book=book)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        original_post_id = self.request.data.get('original_post')
        quoted_post_id = self.request.data.get('quoted_post')

        original_post = Post.objects.get(id=original_post_id)
        quoted_post = Comment.objects.get(id=quoted_post_id) if quoted_post_id else None

        serializer.save(
            poster=self.request.user, original_post=original_post, quoted_post=quoted_post
        )
