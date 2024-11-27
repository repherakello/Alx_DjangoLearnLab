from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Q
from django.http import HttpResponseBadRequest

def search_books(request):
    query = request.GET.get('q')
    if not query:
        return HttpResponseBadRequest("Missing search query")

    # Secure way to filter books
    books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    return render(request, 'bookshelf/book_list.html', {'books': books})
from django.shortcuts import render
from .forms import ExampleForm

def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Handle form data
            print(form.cleaned_data)
            return render(request, 'bookshelf/success.html')
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/example_form.html', {'form': form})



"""
    '''''''
"""
# from django.shortcuts import render
# from .models import Book

# def book_list(request):
#     books = Book.objects.all()
#     return render(request, 'bookshelf/book_list.html', {'books': books})


"""
       '''''
"""
# from django.shortcuts import render, get_object_or_404
# from django.contrib.auth.decorators import permission_required
# from django.http import HttpResponse
# from .models import Article

# @permission_required('app_name.can_view', raise_exception=True)
# def article_list(request):
#     articles = Article.objects.all()
#     return render(request, 'articles/article_list.html', {'articles': articles})

# @permission_required('app_name.can_create', raise_exception=True)
# def article_create(request):
#     if request.method == 'POST':
#         # Handle form submission and save new article
#         return HttpResponse("Article created successfully.")
#     return render(request, 'articles/article_form.html')

# @permission_required('app_name.can_edit', raise_exception=True)
# def article_edit(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     if request.method == 'POST':
#         # Handle form update
#         return HttpResponse("Article updated successfully.")
#     return render(request, 'articles/article_form.html', {'article': article})

# @permission_required('app_name.can_delete', raise_exception=True)
# def article_delete(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     article.delete()
#     return HttpResponse("Article deleted successfully.")
