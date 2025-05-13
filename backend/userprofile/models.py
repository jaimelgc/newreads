from django.contrib.auth.models import AbstractUser
from django.db import models
from library.models import Book


def user_directory_path(instance, filename):
    return f'user_{instance.user.id}/{filename}'


class User(AbstractUser):
    email = models.EmailField(unique=True)
    created = models.DateField(auto_now_add=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(
        upload_to=user_directory_path, default='profile_pics/default.jpg'
    )
    is_moderator = models.BooleanField(default=False)
    is_banned = models.BooleanField(default=False)


class BookList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="book_lists")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)
    is_bookmarked = models.BooleanField(default=False)
    original_author = models.CharField(max_length=55, null=True)


class BookListItem(models.Model):
    book_list = models.ForeignKey(BookList, on_delete=models.CASCADE, related_name="items")
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('book_list', 'book')
