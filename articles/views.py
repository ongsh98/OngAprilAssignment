# my_first_pjt/articles/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "index.html")

def articles(request):
    articles = Article.objects.all().order_by("created_at")
    context = {
        "articles": articles,
    }
    return render(request, "articles.html", context)

def article_detail(request, pk):
    article = get_object_or_404(Article, id=pk)
    context = {"article":article}
    return render(request, "article_detail.html", context)

def new(request):
    forms = ArticleForm()
    context = {"forms":forms}
    return render(request, "new.html", context)

@login_required
def create(request):
    if request.method == "POST":
        input_image = request.FILES.get("image")
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect("articles:article_detail", article.id)
    else:
        form = ArticleForm()

    context = {"form": form}
    return render(request, "articles/create.html", context)

    # title = request.GET.get("title")
    # content = request.GET.get("content")
    # article = Article.objects.create(title=title, content=content)
    # return redirect("article_detail", article.pk)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect("article_detail", article.pk)
        
    else:
        form = ArticleForm(instance=article)

    context = {
        "form":form,
        "article":article
    }
    return render(request, "update.html", context)


    # title = request.POST.get("title")
    # content = request.POST.get("content")

    # article = Article.objects.get(pk=pk)
    # article.title = title
    # article.content = content
    # article.save()

    # return redirect("article_detail", article.pk)

def delete(request, pk):
    if request.method == "POST":
        article = Article.objects.get(pk=pk)
        article.delete()
        return redirect("articles")
    
    return redirect("article_detail", pk)