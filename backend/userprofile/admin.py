from django.contrib import admin

from .models import BookList, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'bio', 'is_moderator', 'is_banned']


@admin.register(BookList)
class BooklistAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'name',
        'description',
        'created_at',
        'is_public',
        'is_bookmarked',
        'original_author',
    ]
    raw_id_fields = ['user']
