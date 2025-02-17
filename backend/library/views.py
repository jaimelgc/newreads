from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from userprofile.models import BookList, ListedBook

from .caching import get_recent_books


def start(request):
    recent_books = get_recent_books()

    return render(request, "start.html", {"recent_books": recent_books})


@login_required
def add_book_to_list(request, list_id, book_ol_id, book_title):
    book_list = get_object_or_404(BookList, id=list_id, user=request.user)

    if not ListedBook.objects.filter(book_list=book_list, book_ol_id=book_ol_id).exists():
        ListedBook.objects.create(book_list=book_list, book_ol_id=book_ol_id, book_title=book_title)

    return redirect("view_book_list", list_id=list_id)
