import graphene
from graphene_django.filter import DjangoFilterConnectionField
from graphql_jwt.decorators import login_required
from .types import AuthorType, BookType
from .models import Author, Book
from .filters import BookFilter, AuthorFilter

class Query(graphene.ObjectType):
    # List all
    all_books = DjangoFilterConnectionField(BookType, filterset_class=BookFilter)
    all_authors = DjangoFilterConnectionField(AuthorType, filterset_class=AuthorFilter)
    
    # Get by Relay id
    book = graphene.relay.Node.Field(BookType)
    author = graphene.relay.Node.Field(AuthorType)

    @login_required
    def resolve_all_books(root, info, **kwargs):
        return Book.objects.all()

    @login_required
    def resolve_all_authors(root, info, **kwargs):
        return Author.objects.all()

    

    
