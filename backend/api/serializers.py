from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from userprofile.models import BookList, BookListItem, SearchHistory

User = get_user_model()


# overrides to hash password
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'bio', 'profile_picture']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookList
        fields = '__all__'


class BookListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookListItem
        fields = '__all__'


class SearchHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchHistory
        fields = '__all__'
