from rest_framework import serializers

from blog.models import Categorie, Article
from .models import Categorie, House, Location, Info_house, image_apercu
from drf_dynamic_fields import DynamicFieldsMixin

class image_apercuSerializer(serializers.ModelSerializer):
    class Meta:
        model = image_apercu
        fields = '__all__'

class Info_houseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info_house
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class HouseSerializer(serializers.ModelSerializer):
    house_info = Info_houseSerializer(many=True, required=False)
    house_apercu = image_apercuSerializer(many=True, required=False) 
    class Meta:
        model = House
        fields = '__all__'

class CategorieSerializer(serializers.ModelSerializer):
    categorie_location = LocationSerializer(many=True, required=False)
    categorie_article = ArticleSerializer(many=True, required=False) 
    categorie_house = HouseSerializer(many=True, required=False) 
    class Meta:
        model = Categorie
        fields = '__all__'
