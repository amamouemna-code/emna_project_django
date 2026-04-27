from django.shortcuts import render, get_object_or_404
from .models import Article

# Cette fonction affiche TOUS les articles (Page d'accueil)
def home(request):
    tous_les_articles = Article.objects.all()
    return render(request, 'blog/index.html', {'articles': tous_les_articles})

# Cette fonction affiche UN SEUL article (Page de détail)
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/detail.html', {'article': article})