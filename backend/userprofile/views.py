from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import BookList


@login_required
def user_book_lists(request):
    lists = BookList.objects.filter(user=request.user)
    return render(request, "user_book_lists.html", {"lists": lists})


@login_required
def view_book_list(request, list_id):
    book_list = get_object_or_404(BookList, id=list_id, user=request.user)
    books = book_list.items.all()  # Fetch books in the list
    return render(request, "view_book_list.html", {"book_list": book_list, "books": books})


@login_required
def create_book_list(request):
    if request.method == "POST":
        name = request.POST.get("name").strip()
        description = request.POST.get("description", "").strip()

        if name:
            BookList.objects.create(user=request.user, name=name, description=description)
            return redirect("user_book_lists")

    return render(request, "create_book_list.html")
