from rest_framework import serializers
from userprofile.serializers import UserPublicSerializer

from .models import Comment, Post


class CommentSerializer(serializers.ModelSerializer):
    poster = UserPublicSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'content', 'poster', 'original_post', 'quoted_post', 'created_at']


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    poster = UserPublicSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'poster', 'book', 'created_at', 'comments']
