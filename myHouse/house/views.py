from django.shortcuts import render
from blog.models import Categorie, Article
from mainConf.models import *
from contact.models import *
from .models import *
from django.core.paginator import Paginator
from blog.form import ArticleSearchForm
from search_views.search import SearchListView
from search_views.filters import BaseFilter

# Create your views here.*

def home(request):
    categorieList = Categorie.objects.filter(statut=True)
    article_all = Article.objects.filter(statut=True)
    page_top = Page_top.objects.filter(statut=True)
    sociaux = Sociaux.objects.filter(statut=True)
    data = {
        'categorieList': categorieList,
        'article_all': article_all,
        'page_top': page_top,
        'sociaux': sociaux,
    }
    return render(request, 'pages/index.html', data)

def about(request):
    categorieList = Categorie.objects.filter(statut=True)
    article_all = Article.objects.filter(statut=True)
    page_top = Page_top.objects.filter(statut=True)
    sociaux = Sociaux.objects.filter(statut=True)
    data = {
        'categorieList': categorieList,
        'article_all': article_all,
        'page_top': page_top,
        'sociaux': sociaux,
    }
    return render(request, 'pages/about.html', data)

def propriete(request):
    categorieList = Categorie.objects.filter(statut=True)
    house = House.objects.filter(statut=True)
    houseimg = image_apercu.objects.filter(statut=True)
    page_top = Page_top.objects.filter(statut=True)
    sociaux = Sociaux.objects.filter(statut=True)
    data = {
        'categorieList': categorieList,
        'house': house,
        'houseimg': houseimg,
        'page_top': page_top,
        'sociaux': sociaux,
    }
    return render(request, 'pages/propriete.html', data)

def developpement(request):
    categorieList = Categorie.objects.filter(statut=True)
    house = House.objects.filter(statut=True)
    page_top = Page_top.objects.filter(statut=True)
    sociaux = Sociaux.objects.filter(statut=True)
    houseDispo = House.objects.filter(isDisponible=True)
    houseOut = House.objects.filter(isSoldout=True)
    apel = Apel.objects.filter(statut=True)
    data = {
        'categorieList': categorieList,
        'house': house,
        'page_top': page_top,
        'sociaux': sociaux,
        'houseDispo': houseDispo,
        'houseOut': houseOut,
        'apel': apel,
    }
    return render(request, 'pages/dev.html', data)

def news(request):
    categorieList = Categorie.objects.filter(statut=True)
    article_all = Article.objects.filter(statut=True)
    page_top = Page_top.objects.filter(statut=True)
    sociaux = Sociaux.objects.filter(statut=True)

    data = {
        'categorieList': categorieList,
        'article_all': article_all,
        'page_top': page_top,
        'sociaux': sociaux,
    }
    return render(request, 'pages/news.html', data)

def contact(request):
    categorieList = Categorie.objects.filter(statut=True)
    article_all = Article.objects.filter(statut=True)
    page_top = Page_top.objects.filter(statut=True)
    sociaux = Sociaux.objects.filter(statut=True)
    data = {
        'categorieList': categorieList,
        'article_all': article_all,
        'page_top': page_top,
        'sociaux': sociaux,
    }
    return render(request, 'pages/contact.html', data)

def views(request):
    categorieList = Categorie.objects.filter(statut=True)
    article_all = Article.objects.filter(statut=True)
    page_top = Page_top.objects.filter(statut=True)
    sociaux = Sociaux.objects.filter(statut=True)
    paginator = Paginator(article_all, 4)
    page = request.GET.get('page') 

    article_all = paginator.get_page(page)
    data = {
        'categorieList': categorieList,
        'article_all': article_all,
        'page_top': page_top,
        'sociaux': sociaux,
    }
    return render(request, 'pages/view.html', data)

def detail(request, id):
    try:
        house = House.objects.get(pk=id)
        
    except:
        return redirect('home')
        
    data = {
        'house': house,
    }
    print(id)
    return render(request, 'pages/detail.html', data)



class articleFilter(BaseFilter):
    search_fields = {
        'search_text' : ['categorie'],
        'search_categorie_exact' :  ['categorie'],
        'search_prix' :  ['prix'],

    }

class articleSearchList(SearchListView):
    model = Article
    paginate_by = 4
    template_name = 'pages/news.html'
    form_class = ArticleSearchForm
    filter_class = articleFilter

def news(request):
    try:
        q = request.GET['q']
        posts = Article.objects.filter(title__search=q) | \
                Article.objects.filter(intro__search=q) | \
                Article.objects.filter(content__search=q)
        data = {
            'q': q,
            'posts': posts,
        }
        return render(request, 'pages/view.html', data)
    except KeyError:
        return render(request, 'pages/view.html')