from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

#Initialize the router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

# Define the URL patterns
urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'), # Maps to the BookList view

    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)), # Include all routers registered with the router
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), # Include the URL for obtaining the auth token
    path('',include('api.urls'))
]