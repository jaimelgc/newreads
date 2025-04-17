import requests

from .models import Author, Book

ol_url = "https://openlibrary.org"


def fetch_work_by_id(ol_id):
    url = f'{ol_url}/works/{ol_id}.json'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def fetch_book_by_isbn(isbn):
    url = f"{ol_url}/isbn/{isbn}.json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def fetch_author_by_id(ol_id):
    url = f"{ol_url}/authors/{ol_id}.json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


# SECOND VER

OPEN_LIBRARY_SEARCH_URL = "https://openlibrary.org/search.json"


def fetch_and_cache_books(search_query: str):
    response = requests.get(OPEN_LIBRARY_SEARCH_URL, params={'q': search_query})
    if response.status_code != 200:
        return []

    data = response.json()
    books = []

    for doc in data.get("docs", []):
        title = doc.get("title")
        author_names = doc.get("author_name", [])
        if not title:
            continue

        # Create or get authors
        authors = []
        for name in author_names:
            author, _ = Author.objects.get_or_create(name=name)
            authors.append(author)

        # Create book only if it doesn't exist
        book, created = Book.objects.get_or_create(title=title)

        if created:
            book.save()
            book.authors.set(authors)

        books.append(book)

    return books
