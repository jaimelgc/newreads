from django.core.cache import cache
from django.utils.timezone import now, timedelta

from .models import Book


def get_recent_books():
    cache_key = "latest_added"
    books = cache.get(cache_key)

    if not books:
        seven_days_ago = now() - timedelta(days=7)
        books = Book.objects.filter(created_at__gte=seven_days_ago).order_by('-created_at')[:10]

        cache.set(cache_key, books, timeout=60 * 60 * 24)

    return books
