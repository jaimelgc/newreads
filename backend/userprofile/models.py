from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    created = models.DateField(auto_now_add=True)
    biography = models.TextField(blank=True)
