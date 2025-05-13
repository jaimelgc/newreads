from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import generics, permissions, viewsets
# from library.utils import get_or_create_book

from .models import BookList, BookListItem
from .serializers import (  # SearchHistorySerializer,
    BooklistItemSerializer,
    BooklistSerializer,
    RegisterSerializer,
    UserPrivateSerializer,
    UserPublicSerializer,
)

# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView


User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserPrivateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    lookup_field = 'username'
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserPublicSerializer
        return UserPublicSerializer

    def get_queryset(self):
        search_query = self.request.query_params.get('search', '')
        return User.objects.filter(username__icontains=search_query)


class BookListItemViewSet(viewsets.ModelViewSet):
    queryset = BookListItem.objects.all()
    serializer_class = BooklistItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def perform_create(self, serializer):
    #     book_data = self.request.data.get('book')
    #     if book_data:
    #         if isinstance(book_data, str):
    #             book = get_or_create_book(book_data)
    #             serializer.save(book=book, book_list_id=self.request.data.get('book_list'))
    #         else:
    #             serializer.save()


class BookListViewSet(viewsets.ModelViewSet):
    queryset = BookList.objects.all()
    serializer_class = BooklistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        username = self.request.query_params.get('username')

        if self.action == 'list':
            if username:
                return BookList.objects.filter(user__username=username, is_public=True)
            else:
                return BookList.objects.filter(user=user)

        return BookList.objects.filter(Q(is_public=True) | Q(user=user))

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
