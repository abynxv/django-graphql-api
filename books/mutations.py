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

class UpdateBook(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String()
        author_id = graphene.Int()
        isbn = graphene.String()
        published_date = graphene.Date()
        price = graphene.Decimal()
        genre = graphene.String()

    book = graphene.Field(BookType)

    def mutate(root, info, id, title, author_id, isbn, published_date, price, genre):
        book = Book.objects.get(id=id)
        if title:
            book.title = title
        if author_id:
            book.author_id = author_id
        if isbn:
            book.isbn = isbn
        if published_date:
            book.published_date = published_date
        if price:
            book.price = price
        if genre:
            book.genre = genre
        book.save()
        return UpdateBook(book=book)

class DeleteBook(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    book = graphene.Field(BookType)

    def mutate(root, info, id):
        book = Book.objects.get(id=id)
        book.delete()
        return DeleteBook(book=book)

class Mutation(graphene.ObjectType):
    create_author = CreateAuthor.Field()
    update_author = UpdateAuthor.Field()
    delete_author = DeleteAuthor.Field()
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()
    delete_book = DeleteBook.Field()


