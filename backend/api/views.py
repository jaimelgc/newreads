from django.contrib.auth import get_user_model
from rest_framework import viewsets
from userprofile.models import BookList, BookListItem, SearchHistory

from .serializers import (
    BookListItemSerializer,
    BookListSerializer,
    SearchHistorySerializer,
    UserSerializer,
)

User = get_user_model()


# viewset or api view??
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookListViewSet(viewsets.ModelViewSet):
    queryset = BookList.objects.all()
    serializer_class = BookListSerializer


class BookListItemViewSet(viewsets.ModelViewSet):
    queryset = BookListItem.objects.all()
    serializer_class = BookListItemSerializer


class SearchHistoryViewSet(viewsets.ModelViewSet):
    queryset = SearchHistory.objects.all()
    serializer_class = SearchHistorySerializer
