import django_filters
from .models import Author, Book

class AuthorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Author
        fields = ['name', 'email']

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    genre = django_filters.CharFilter(lookup_expr='iexact')
    price_lte = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    price_gte = django_filters.NumberFilter(field_name='price', lookup_expr='gte')

    class Meta:
        model = Book
        fields = ['title', 'isbn', 'genre']
