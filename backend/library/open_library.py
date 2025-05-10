import requests

from .models import Book

# from django.core.cache import cache

ol_url = "https://openlibrary.org"

# Get singular
# Search by title: https://openlibrary.org/search.json?title=The+Hobbit
# Search by author: https://openlibrary.org/search.json?author=Tolkien
# Get WORK by id: https://openlibrary.org/works/OL262758W.json
# Get EDITION by ISBN: https://openlibrary.org/isbn/9780261103344.json
# Get edition by id: https://openlibrary.org/books/{olid}.json
# Genre search: https://openlibrary.org/subjects/{name}.json

# Search query
# by title: https://openlibrary.org/search.json?q={query}&page={page}
# by author: https://openlibrary.org/search/authors.json?q={query}&page={page}
# search by isbn? : https://openlibrary.org/isbn/{isbn}.json

# Complex filtering
# def advanced_search(title=None, author=None, subject=None, language=None, year_range=None):
# Build query string like:
# https://openlibrary.org/search.json?title=...&author=...&subject=...


def get_catch_data(key, url, timeout=60 * 60 * 24):
    # cached_data = cache.get(key)
    cached_data = False

    if cached_data:
        print("✔️ Loaded from cache")
        return cached_data

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # cache.set(key, data, timeout)
        print("📡 Fetched from Open Library and cached")
        return data

    print("❌ Not found or error")
    return None


def get_or_create_book(ol_id: str) -> Book:
    try:
        return Book.objects.get(ol_id=ol_id)
    except Book.DoesNotExist:
        response = requests.get(f"https://openlibrary.org/books/{ol_id}.json")
        if response.status_code != 200:
            raise ValueError("Book not found on Open Library")

        data = response.json()

        # Extract author keys and fetch names
        authors = []
        for author_ref in data.get("authors", []):
            author_key = author_ref.get("key")
            if author_key:
                author_resp = requests.get(f"https://openlibrary.org{author_key}.json")
                if author_resp.status_code == 200:
                    author_data = author_resp.json()
                    name = author_data.get("name")
                    if name:
                        authors.append(name)

        return Book.objects.create(
            ol_id=ol_id,
            title=data.get("title", "Untitled"),
            author_name="; ".join(authors),
            cover_url=(
                f"https://covers.openlibrary.org/b/id/{data.get('covers', [])[0]}-L.jpg"
                if data.get("covers")
                else None
            ),
            publish_date=data.get("publish_date", ""),
        )
