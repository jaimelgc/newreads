from rest_framework import serializers

from .models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'poster', 'book', 'created_at']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'poster', 'original_post', 'quoted_post', 'created_at']
