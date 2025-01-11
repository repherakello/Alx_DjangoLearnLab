from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class BookList(ListAPIView):
    """
    View to retrieve and return a list of books
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(ModelViewSet):
    """
     ViewSet for managing books. Requires authentication for all actions.
    - Permissions:
        * IsAuthenticated: Users must be logged in to access.
    """
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]