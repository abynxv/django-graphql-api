import graphene_django
from graphene_django.types import DjangoObjectType
from .models import Author, Book

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = ('id', 'name', 'email')

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'isbn', 'published_date', 'price', 'genre')