from django.contrib.auth import get_user_model

# from django.db.models import Q
from rest_framework import filters, generics, permissions, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import BookList, BookListItem
from .serializers import (  # SearchHistorySerializer,
    BooklistItemSerializer,
    BooklistSerializer,
    RegisterSerializer,
    UserPrivateSerializer,
    UserPublicSerializer,
)

# from library.utils import get_or_create_book


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
    serializer_class = UserPublicSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']


class BookListItemViewSet(viewsets.ModelViewSet):
    queryset = BookListItem.objects.all()
    serializer_class = BooklistItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return [AllowAny()]
        return [IsAuthenticated()]


class BookListViewSet(viewsets.ModelViewSet):
    queryset = BookList.objects.all()
    serializer_class = BooklistSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]

    def get_permissions(self):
        if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_search_fields(self):
        search_field = self.request.query_params.get('field', None)

        match search_field:
            case 'name':
                return ['name']
            case 'author__username':
                return ['author__username']
            case _:
                return ['name']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
