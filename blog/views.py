from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms  import ArticleForm

# Create your views here.
def homepage(request):
    return render(request, 'blog/homepage.html')

def about(request):
    return render(request, 'blog/about.html')
from .models import Article

def article_list(request):
    articles = Article.objects.order_by('-created_at')
    return render(request, 'blog/article_list.html', {'articles': articles})

def article_list(request):
    articles = Article.objects.order_by('-created_at')
    return render(request, 'blog/article_list.html', {'articles': articles})

# READ: show a single article
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/article_detail.html', {'article': article})

# CREATE: show blank form & save new Article
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()           # ORM: INSERT row
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'blog/article_form.html', {'form': form})

# UPDATE: populate form with existing Article & save changes
def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = ArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        form.save()                       # ORM: UPDATE row
        return redirect('article_detail', pk=article.pk)
    return render(request, 'blog/article_form.html', {'form': form})

# DELETE: confirm & delete an Article
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()                 # ORM: DELETE row
        return redirect('article_list')
    return render(request, 'blog/article_confirm_delete.html', {'article': article})


