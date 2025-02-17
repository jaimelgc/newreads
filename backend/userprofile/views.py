from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import BookList


@login_required
def create_book_list(request):
    if request.method == "POST":
        name = request.POST.get("name").strip()
        description = request.POST.get("description", "").strip()

        if name:
            BookList.objects.create(user=request.user, name=name, description=description)
            return redirect("user_book_lists")

    return render(request, "create_book_list.html")
