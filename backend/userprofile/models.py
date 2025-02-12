from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class User(AbstractUser):
    email = models.EmailField(unique=True)
    created = models.DateField(auto_now_add=True)
    biography = models.TextField(blank=True)
    # book list next


class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="search_history")
    query = models.CharField(max_length=500)
    searched_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.user.username} - '{self.query}' - {self.searched_at}"
