# from datetime import timedelta

from django.db import models
from django.utils.timezone import now
from slugify import slugify


class Work(models.Model):
    ol_id = models.CharField(primary_key=True, max_length=100, unique=True, db_index=True)
    title = models.CharField(max_length=500, db_index=True)
    description = models.TextField(blank=True, null=True)
    authors = models.ManyToManyField('Author', related_name='works')
    subjects = models.ManyToManyField('Subject', related_name='works')
    cover_url = models.URLField(blank=True, null=True)
    first_published = models.CharField(max_length=50, blank=True, null=True)


class Book(models.Model):
    ol_id = models.CharField(primary_key=True, max_length=100, unique=True, db_index=True)
    work = models.ForeignKey(Work, on_delete=models.CASCADE, related_name='editions')
    title = models.CharField(max_length=500, db_index=True)  # Longer titles?
    subtitle = models.CharField(max_length=500, db_index=True, blank=True, null=True)
    authors = models.ManyToManyField('Author', related_name='editions')
    publishers = models.ManyToManyField('Publisher', related_name='books')
    publish_date = models.CharField(max_length=50, blank=True, null=True)
    isbn_10 = models.CharField(max_length=10, blank=True, null=True, unique=True)
    isbn_13 = models.CharField(max_length=13, blank=True, null=True, unique=True)
    page_count = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    cover_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_checked = models.DateTimeField(default=now)

    def update_last_checked(self):
        self.last_checked = now()
        self.save()


class Author(models.Model):
    ol_id = models.CharField(max_length=100, unique=True, db_index=True)
    name = models.CharField(max_length=255, db_index=True)
    birth_date = models.CharField(max_length=100, blank=True, null=True)
    death_date = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    photo_url = models.URLField(blank=True, null=True)
    openlibrary_url = models.URLField(blank=True, null=True)


class Publisher(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Subject(models.Model):
    name = models.CharField(max_length=250, unique=True, db_index=True)
