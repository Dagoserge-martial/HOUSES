from django.db import models
from django.contrib.auth.models import User
from tinymce import HTMLField

# Create your models here.

class Config(models.Model):
    logo1 = models.ImageField(upload_to='logo')
    logo2 = models.ImageField(upload_to='logo')
    adress = models.CharField(max_length=255)
    lien_map = models.CharField(max_length=255)
    cel = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    

class Slide(models.Model):
    titre = models.CharField(max_length=255)
    image = models.ImageField(upload_to='img')

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

class Avenir(models.Model):
    titre = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    prix = models.CharField(max_length=20)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titre

class Page_top(models.Model):
    nom = models.CharField(max_length=255)
    titre = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image_back = models.ImageField(upload_to='img')

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nom

class Sociaux(models.Model):
    nom = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nom

class Anonce(models.Model):
    titre = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

class Demande(models.Model):
    description = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    image = models.ImageField(upload_to='img')

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

class About(models.Model):
    titre = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

class Agenda(models.Model):
    titre = models.CharField(max_length=255)
    number = models.CharField(max_length=255)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

class About_image(models.Model):
    image = models.ImageField(upload_to='img')

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

class Footer(models.Model):
    titre = models.CharField(max_length=255)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre
    
class Footer_detail(models.Model):
    footer = models.ForeignKey(Footer, on_delete = models.CASCADE, related_name='info_foot')
    titre = models.CharField(max_length=255)
    lien = models.CharField(max_length=255)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    
    
