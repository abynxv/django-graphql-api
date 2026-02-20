import graphene
from graphql_jwt.decorators import superuser_required
from graphql_relay import from_global_id
from .types import AuthorType, BookType
from .models import Author, Book

class AuthorInput(graphene.InputObjectType):
    name = graphene.String()
    email = graphene.String()

class BookInput(graphene.InputObjectType):
    title = graphene.String()
    author_id = graphene.ID()
    isbn = graphene.String()
    published_date = graphene.Date()
    price = graphene.Decimal()
    genre = graphene.String()

class CreateAuthor(graphene.Mutation):
    class Arguments:
        input = AuthorInput(required=True)

    author = graphene.Field(AuthorType)

    @classmethod
    @superuser_required
    def mutate(cls, root, info, input):
        author = Author.objects.create(
            name=input.get('name'),
            email=input.get('email')
        )
        return CreateAuthor(author=author)

class UpdateAuthor(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = AuthorInput(required=True)

    author = graphene.Field(AuthorType)

    @classmethod
    @superuser_required
    def mutate(cls, root, info, id, input):
        _, db_id = from_global_id(id)
        author = Author.objects.get(id=db_id)
        if input.get('name'):
            author.name = input.get('name')
        if input.get('email'):
            author.email = input.get('email')
        author.save()
        return UpdateAuthor(author=author)

class DeleteAuthor(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    author = graphene.Field(AuthorType)

    @classmethod
    @superuser_required
    def mutate(cls, root, info, id):
        _, db_id = from_global_id(id)
        author = Author.objects.get(id=db_id)
        author.delete()
        return DeleteAuthor(author=author)

class CreateBook(graphene.Mutation):
    class Arguments:
        input = BookInput(required=True)

    book = graphene.Field(BookType)

    @classmethod
    @superuser_required
    def mutate(cls, root, info, input):
        try:
            _, author_db_id = from_global_id(input.get('author_id'))
            author = Author.objects.get(id=author_db_id)
        except Exception:
            raise Exception("Author not found or invalid ID")

        book = Book.objects.create(
            title=input.get('title'),
            author=author,
            isbn=input.get('isbn'),
            published_date=input.get('published_date'),
            price=input.get('price'),
            genre=input.get('genre')
        )
        return CreateBook(book=book)

class UpdateBook(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = BookInput(required=True)

    book = graphene.Field(BookType)

    @classmethod
    @superuser_required
    def mutate(cls, root, info, id, input):
        _, db_id = from_global_id(id)
        book = Book.objects.get(id=db_id)
        
        if input.get('title'):
            book.title = input.get('title')
        if input.get('author_id'):
            _, author_db_id = from_global_id(input.get('author_id'))
            book.author_id = author_db_id
        if input.get('isbn'):
            book.isbn = input.get('isbn')
        if input.get('published_date'):
            book.published_date = input.get('published_date')
        if input.get('price'):
            book.price = input.get('price')
        if input.get('genre'):
            book.genre = input.get('genre')
            
        book.save()
        return UpdateBook(book=book)

class DeleteBook(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    book = graphene.Field(BookType)

    @classmethod
    @superuser_required
    def mutate(cls, root, info, id):
        _, db_id = from_global_id(id)
        book = Book.objects.get(id=db_id)
        book.delete()
        return DeleteBook(book=book)

class Mutation(graphene.ObjectType):
    create_author = CreateAuthor.Field()
    update_author = UpdateAuthor.Field()
    delete_author = DeleteAuthor.Field()
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()
    delete_book = DeleteBook.Field()


