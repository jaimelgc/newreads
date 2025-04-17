from rest_framework import serializers

from .models import Author, Book, Publisher, Subject, Work


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ['last_checked']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
