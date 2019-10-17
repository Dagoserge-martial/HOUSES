"""myHouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .import views

from rest_framework.routers import DefaultRouter
from .apiviews import CategorieViewSet, HouseViewSet, ArticleViewSet, LocationViewSet, Info_houseViewSet

router = DefaultRouter()
router.register('apicategorie', CategorieViewSet, base_name='categorie')
router.register('apihouse', HouseViewSet, base_name='house')
router.register('apiarticle', ArticleViewSet, base_name='article')
router.register('apilocation', LocationViewSet, base_name='location')
router.register('apiinfo', Info_houseViewSet, base_name='info')

urlpatterns = [
    path('house', views.home, name='home'),
    path('about', views.about, name='about'),
    path('news', views.news, name='news'),
    path('developpement', views.developpement, name='developpement'),
    path('propriete', views.propriete, name='propriete'),
    path('contact', views.contact, name='contact'),
    path('views', views.views, name='views'),
    path('<int:id>/detail', views.detail, name='detail'),
    
]

urlpatterns += router.urls