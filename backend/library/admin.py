from django.contrib import admin

from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'ol_id', 'title', 'author_name', 'publish_date', 'cover_url']