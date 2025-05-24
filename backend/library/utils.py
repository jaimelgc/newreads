import requests

from .models import Book


def get_or_create_book(ol_id: str = '', id: int = -1) -> Book:
    if id >= 0:
        return Book.objects.get(pk=id)
    elif ol_id:
        try:
            return Book.objects.get(ol_id=ol_id)
        except Book.DoesNotExist:
            response = requests.get(f"https://openlibrary.org/books/{ol_id}.json")
            if response.status_code != 200:
                raise ValueError("Book not found on Open Library")

            data = response.json()
            return Book.objects.create(
                ol_id=ol_id,
                title=data.get("title", "Untitled"),
                author_names="; ".join(data.get("authors", [])),
                cover_url=(
                    f"https://covers.openlibrary.org/b/id/{data.get('covers', [])[0]}-L.jpg"
                    if data.get("covers")
                    else None
                ),
                description=(
                    data.get("description", "") if isinstance(data.get("description"), str) else ""
                ),
                publish_date=data.get("publish_date", ""),
            )
