from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CreateArticle
from .models import Article
from django.contrib.auth.decorators import login_required

# Create your views here.

def article_list(request):
    articles = Article.objects.all().order_by('createdAt')
    return render(request,'articles/article_list.html',{'articles':articles})




def article_details(request,slug):
    article = get_object_or_404(Article, slug=slug)  # Fetch article using slug
    return render(request,'articles/article_details.html',{'article': article})



@login_required(login_url='login') 
def create_article(request):
    if request.method == "POST":
        form = CreateArticle(request.POST, request.FILES)  # Include request.FILES for image uploads
        if form.is_valid():
            article = form.save(commit=False)  # Don't save yet to modify before saving
            article.author=request.user #current user
            article.save()  # Save the article to the database
            return redirect('article_list')  # Redirect to article list after successful creation
    else:
        form = CreateArticle()  # Empty form for GET request

    return render(request, 'articles/create_article.html', {'form': form})
