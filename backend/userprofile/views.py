from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import generics, permissions

from .models import BookList
from .serializers import (  # BooklistItemSerializer,; SearchHistorySerializer,
    BooklistSerializer,
    RegisterSerializer,
    UserPrivateSerializer,
    UserPublicSerializer,
)

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


class UserPublicView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserPublicSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'username'


class UserSearchView(generics.ListAPIView):
    serializer_class = UserPublicSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        search_query = self.request.query_params.get('search', '')
        return User.objects.filter(username__icontains=search_query)


class BookListCreateView(generics.CreateAPIView):
    serializer_class = BooklistSerializer
    permission_classes = [permissions.IsAuthenticated]


class MyBookListsView(generics.ListAPIView):
    serializer_class = BooklistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BookList.objects.filter(user=self.request.user)


class UserBookListsView(generics.ListAPIView):
    serializer_class = BooklistSerializer
    lookup_field = 'username'

    def get_queryset(self):
        username = self.kwargs.get('username')
        return BookList.objects.filter(user__username=username, is_public=True)


class BookListDetailView(generics.RetrieveAPIView):
    serializer_class = BooklistSerializer

    def get_queryset(self):
        user = self.request.user
        return BookList.objects.filter(Q(is_public=True) | Q(user=user))