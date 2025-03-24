from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from library.models import Work

from .forms import CustomUserCreationForm
from .models import BookList


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


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


@login_required
def add_book_to_list(request, list_id):
    book_list = get_object_or_404(BookList, id=list_id, user=request.user)

    if request.method == "POST":
        book_id = request.POST.get("book_id")
        book = get_object_or_404(Work, id=book_id)

        if book not in book_list.items.all():
            book_list.items.add(book)

        return redirect("view_book_list", list_id=list_id)  # Refresh view

    return redirect("view_book_list", list_id=list_id)


@login_required
def edit_profile(request):
    pass


@login_required
def dashboard(request):
    pass
