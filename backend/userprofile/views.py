from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import generics, permissions, viewsets

from .models import BookList
from .serializers import (  # BooklistItemSerializer,; SearchHistorySerializer,
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

    # def perform_update(self, serializer):
    #     if serializer.instance.user == self.request.user:
    #         serializer.save()

    # def perform_destroy(self, instance):
    #     if instance.user == self.request.user:
    #         instance.delete()


# class UserBookListsView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, username=None):
#         user = User.objects.filter(username=username).first()
#         if not user:
#             return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
#         book_lists = BookList.objects.filter(user=user)
#         serializer = BooklistSerializer(book_lists, many=True)
#         return Response(serializer.data)
