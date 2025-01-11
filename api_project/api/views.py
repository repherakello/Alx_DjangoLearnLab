from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class BookList(ListAPIView):
    """
    View to retrieve and return a list of books
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(ModelViewSet):
    """
    A viewset for handling CRUD operations for the Book model.
    """
    serializer_class = BookSerializer
    queryset = Book.objects.all()
