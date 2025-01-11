from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookList(ListAPIView):
    """
    View to retrieve and return a list of books
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer