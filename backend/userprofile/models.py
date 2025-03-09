from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class User(AbstractUser):
    email = models.EmailField(unique=True)
    created = models.DateField(auto_now_add=True)
    biography = models.TextField(blank=True)
    profile_picture = models.ImageField(default='default_pfp', upload_to='profile_pics')


class BookList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="book_lists")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class BookListItem(models.Model):
    book_list = models.ForeignKey(BookList, on_delete=models.CASCADE, related_name="items")
    ol_id = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    added_at = models.DateTimeField(auto_now_add=True)


class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="search_history")
    query = models.CharField(max_length=500)
    searched_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.user.username} - '{self.query}' - {self.searched_at}"
