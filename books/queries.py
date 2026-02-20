import graphene
from .types import AuthorType, BookType
from .models import Author, Book

class Query(graphene.ObjectType):
    # List all
    all_books = graphene.List(BookType)
    all_authors = graphene.List(AuthorType)
    
    # Get by id
    book = graphene.Field(BookType, id=graphene.Int(required=True))
    author = graphene.Field(AuthorType, id=graphene.Int(required=True))

    def resolve_all_books(root, info):
        return Book.objects.select_related('author').all()

    def resolve_all_authors(root, info):
        return Author.objects.prefetch_related('books').all()

    def resolve_book(root, info, id):
        try:
            return Book.objects.select_related('author').get(id=id)
        except Book.DoesNotExist:
            return None

    def resolve_author(root, info, id):
        try:
            return Author.objects.prefetch_related('books').get(id=id)
        except Author.DoesNotExist:
            return None

    

    
