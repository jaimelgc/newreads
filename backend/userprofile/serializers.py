from django.contrib.auth import get_user_model
from library.serializers import BookSerializer
from rest_framework import serializers

from .models import BookList, BookListItem  # SearchHistory

User = get_user_model()


class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'created',
            'profile_picture',
            'bio',
            'is_moderator',
            'is_banned',
        ]


class UserPrivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class BooklistItemSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = BookListItem
        fields = ['id', 'book', 'title', 'added_at']


class BooklistSerializer(serializers.ModelSerializer):
    author = UserPublicSerializer(source='user', read_only=True)
    items = BooklistItemSerializer(many=True, read_only=True)

    class Meta:
        model = BookList
        fields = ['id', 'name', 'description', 'created_at', 'is_public', 'author', 'items']

    # def create(self, validated_data):
    #     user = self.context['request'].user
    #     return BookList.objects.create(user=user, **validated_data)
