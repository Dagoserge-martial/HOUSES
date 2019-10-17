from django.db import models

# Create your models here.
from tinymce import HTMLField

class Categorie(models.Model):
    nom = models.CharField(max_length=255)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Categorie"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.nom

class Article(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete = models.CASCADE, related_name='categorie_article')
    titre = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    contenue = HTMLField('contenue')
    lien_video = models.CharField(max_length=255, blank=True)
    prix = models.CharField(max_length=255, blank=True)
    image_accueil = models.ImageField(upload_to='img', blank=True)
    isFitured = models.BooleanField(default=False)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    




# class MyModel(models.Model):
#     ...
#     content = HTMLField('Content')

#./manage.py admin_generator APP_NAME >> APP_NAME/admin.py