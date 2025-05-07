# from datetime import timedelta

from django.db import models
from django.utils.timezone import now
from slugify import slugify

class Book(models.Model):
    ol_id = models.CharField(primary_key=True, max_length=100, unique=True, db_index=True)
    title = models.CharField(max_length=250, db_index=True)
    authors = models.CharField(max_length=250, blank=True, null=True)
    publish_date = models.CharField(max_length=50, blank=True, null=True)
    cover_url = models.URLField(blank=True, null=True)