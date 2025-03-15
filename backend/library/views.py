# from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# from .caching import get_recent_books
from .ol import fetch_author_by_id, fetch_book_by_isbn, fetch_work_by_id

# from django.shortcuts import get_object_or_404, redirect, render


# from userprofile.models import BookList, BookListItem


def test_fetch_work(request, ol_id):
    data = fetch_work_by_id(ol_id)
    if data:
        return JsonResponse(data)
    else:
        return JsonResponse({"error": "Work not found"}, status=404)


def test_fetch_book(request, isbn):
    data = fetch_book_by_isbn(isbn)
    if data:
        return JsonResponse(data)
    else:
        return JsonResponse({"error": "Book not found"}, status=404)


def test_fetch_author(request, ol_id):
    data = fetch_author_by_id(ol_id)
    if data:
        return JsonResponse(data)
    else:
        return JsonResponse({"error": "Author not found"}, status=404)


# def start(request):
#     recent_books = get_recent_books()

#     return render(request, "start.html", {"recent_books": recent_books})


# @login_required
# def add_book_to_list(request, list_id, book_ol_id, book_title):
#     book_list = get_object_or_404(BookList, id=list_id, user=request.user)

#     if not BookListItem.objects.filter(book_list=book_list, book_ol_id=book_ol_id).exists():
#         BookListItem.objects.create(
#             book_list=book_list, book_ol_id=book_ol_id, book_title=book_title
#         )

#     return redirect("view_book_list", list_id=list_id)
