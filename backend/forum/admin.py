from django.contrib import admin

from .models import Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'poster', 'book', 'created_at']
    raw_id_fields = ['poster']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'poster', 'original_post', 'quoted_post', 'created_at']
    raw_id_fields = ['poster', 'original_post', 'quoted_post']
