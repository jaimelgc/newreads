import requests
from django.core.cache import cache

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
    cached_data = cache.get(key)

    if cached_data:
        print("✔️ Loaded from cache")
        return cached_data

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        cache.set(key, data, timeout)
        print("📡 Fetched from Open Library and cached")
        return data

    print("❌ Not found or error")
    return None

get_catch_data('test_key', 'https://openlibrary.org/isbn/9780261103344.json')
