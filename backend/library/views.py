from django.shortcuts import render

from .caching import get_recent_books


def start(request):
    recent_books = get_recent_books()

    return render(request, "start.html", {"recent_books": recent_books})
