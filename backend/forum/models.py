from django.db import models
from library.models import Book
from userprofile.models import User


class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    poster = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="user_posts"
    )
    book = models.ForeignKey(
        Book, on_delete=models.SET_NULL, null=True, blank=True, related_name="book_posts"
    )
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    content = models.TextField()
    poster = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="posts")
    original_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    quoted_post = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="quoted"
    )
    created_at = models.DateTimeField(auto_now_add=True)
