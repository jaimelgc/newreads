from django.contrib.auth import get_user_model
from rest_framework import filters, generics, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import BookList, BookListItem
from .serializers import (
    BooklistItemSerializer,
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
    search_fields = ['name']

    def get_permissions(self):
        if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_queryset(self):
        queryset = self.queryset
        username = self.request.query_params.get('username')
        if username:
            queryset = queryset.filter(user__username=username)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def bookmark(self, request, pk=None):
        try:
            original = self.get_object()
            if original.user == request.user:
                return Response(
                    {'error': 'You cannot bookmark your own list.'},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            new_list = BookList.objects.create(
                user=request.user,
                name=original.name,
                description=original.description,
                is_public=original.is_public,
                is_bookmarked=True,
                original_author=original.user.username,
            )
            for item in original.items.all():
                BookListItem.objects.create(book_list=new_list, book=item.book)
            serializer = self.get_serializer(new_list)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
