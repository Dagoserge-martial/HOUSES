from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class CategorieAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom', 'statut', 'date_add', 'date_upd')
    list_filter = (
        'statut',
        'date_add',
        'date_upd',
        'id',
        'nom',
        'statut',
        'date_add',
        'date_upd',
    )


class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'categorie',
        'titre',
        'description',
        'contenue',
        'lien_video',
        'prix',
        'image_accueil',
        'isFitured',
        'statut',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'categorie',
        'isFitured',
        'statut',
        'date_add',
        'date_upd',
        'id',
        'categorie',
        'titre',
        'description',
        'contenue',
        'lien_video',
        'prix',
        'image_accueil',
        'isFitured',
        'statut',
        'date_add',
        'date_upd',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Categorie, CategorieAdmin)
_register(models.Article, ArticleAdmin)
