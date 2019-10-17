from rest_framework import viewsets
from rest_framework import generics
from rest_framework import filters

from blog.models import Categorie, Article
from .models import House, Location, Info_house
from .serializers import CategorieSerializer, HouseSerializer, ArticleSerializer, LocationSerializer, Info_houseSerializer

class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])

class CategorieViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class Info_houseViewSet(viewsets.ModelViewSet):
    queryset = Info_house.objects.all()
    serializer_class = Info_houseSerializer