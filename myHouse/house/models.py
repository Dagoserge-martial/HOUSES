from django.db import models

# Create your models here.
from tinymce import HTMLField
from blog.models import Categorie, Article

class House(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete = models.CASCADE, related_name='categorie_house')
    titre = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    contenue = HTMLField('contenue')
    prix = models.CharField(max_length=255)
    image = models.ImageField(upload_to='img', blank=True)
    image_accueil = models.ImageField(upload_to='img', blank=True)
    image_prop = models.ImageField(upload_to='img', blank=True)
    isDisponible = models.BooleanField(default=False)
    isSoldout = models.BooleanField(default=False)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "House"
        verbose_name_plural = "Houses"

    def __str__(self):
        return self.titre

class Location(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete = models.CASCADE, related_name='categorie_location')
    titre = models.CharField(max_length=255)
    image = models.ImageField(upload_to='img', blank=True)
    image_vue = models.ImageField(upload_to='img', blank=True)
    lien_video = models.CharField(max_length=255, blank=True)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

class Info_house(models.Model):
    house = models.ForeignKey(House, on_delete = models.CASCADE, related_name='house_info')
    titre = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    noumbre = models.CharField(max_length=255)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

class image_apercu(models.Model):
    house = models.ForeignKey(House, on_delete = models.CASCADE, related_name='house_apercu')
    image = models.ImageField(upload_to='img', blank=True)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

class Presentation(models.Model):
    titre = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

#python manage.py admin_generator blog >> blog/admin.py