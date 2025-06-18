from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'blog/homepage.html')

def about(request):
    return render(request, 'blog/about.html')
from .models import Article

def article_list(request):
    articles = Article.objects.order_by('-created_at')
    return render(request, 'blog/article_list.html', {'articles': articles})
