import requests

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


def fetch_author_by_ol_id(ol_id):
    url = f"{ol_url}/authors/{ol_id}.json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None
