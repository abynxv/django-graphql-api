import graphene
from graphene_django.types import DjangoObjectType
from .models import Author, Book

class AuthorType(DjangoObjectType):
    book_count = graphene.Int()

    class Meta:
        model = Author
        interfaces = (graphene.relay.Node, )
        fields = ('id', 'name', 'email')
        filter_fields = ['name', 'email']

    @classmethod
    def get_node(cls, info, id):
        if not info.context.user.is_authenticated:
            raise Exception('Not logged in!')
        return Author.objects.get(id=id)

    def resolve_book_count(self, info):
        return self.books.count()

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        interfaces = (graphene.relay.Node, )
        fields = ('id', 'title', 'author', 'isbn', 'published_date', 'price', 'genre')
        filter_fields = ['title', 'isbn', 'genre']

    @classmethod
    def get_node(cls, info, id):
        if not info.context.user.is_authenticated:
            raise Exception('Not logged in!')
        return Book.objects.get(id=id)