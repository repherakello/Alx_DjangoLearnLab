from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from .models import Article

@permission_required('app_name.can_view', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles})

@permission_required('app_name.can_create', raise_exception=True)
def article_create(request):
    if request.method == 'POST':
        # Handle form submission and save new article
        return HttpResponse("Article created successfully.")
    return render(request, 'articles/article_form.html')

@permission_required('app_name.can_edit', raise_exception=True)
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        # Handle form update
        return HttpResponse("Article updated successfully.")
    return render(request, 'articles/article_form.html', {'article': article})

@permission_required('app_name.can_delete', raise_exception=True)
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return HttpResponse("Article deleted successfully.")
