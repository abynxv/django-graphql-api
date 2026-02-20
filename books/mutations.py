import graphene
from .types import AuthorType, BookType
from .models import Author, Book

class CreateAuthor(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)

    author = graphene.Field(AuthorType)

    def mutate(root, info, name, email):
        author = Author.objects.create(
            name=name,
            email=email
        )
        return CreateAuthor(author=author)

class UpdateAuthor(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()
        email = graphene.String()

    author = graphene.Field(AuthorType)

    def mutate(root, info, id, name, email):
        author = Author.objects.get(id=id)
        if name:
            author.name = name
        if email:
            author.email = email
        author.save()
        return UpdateAuthor(author=author)

class DeleteAuthor(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    author = graphene.Field(AuthorType)

    def mutate(root, info, id):
        author = Author.objects.get(id=id)
        author.delete()
        return DeleteAuthor(author=author)
 
class CreateBook(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        author_id = graphene.Int(required=True)
        isbn = graphene.String(required=True)
        published_date = graphene.Date(required=True)
        price = graphene.Decimal(required=True)
        genre = graphene.String(required=True)

    book = graphene.Field(BookType)

    def mutate(root, info, title, author_id, isbn, published_date, price, genre):
        try:
            author = Author.objects.get(id=author_id)
        except Author.DoesNotExist:
            raise Exception("Author not found")

        book = Book.objects.create(
            title=title,
            author=author,
            isbn=isbn,
            published_date=published_date,
            price=price,
            genre=genre
        )
        return CreateBook(book=book)

class Mutation(graphene.ObjectType):
    create_author = CreateAuthor.Field()
    update_author = UpdateAuthor.Field()
    delete_author = DeleteAuthor.Field()
    create_book = CreateBook.Field()


