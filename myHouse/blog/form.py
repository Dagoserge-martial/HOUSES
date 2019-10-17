from .models import *
from django import forms

class ArticleSearchForm(forms.Form):
    search_text =  forms.CharField(
                    required = False,
                    label='Search name or surname!',
                    widget=forms.TextInput(attrs={'placeholder': 'search here!'})
                  )

    search_categorie_exact = forms.CharField(
                    required = False,
                    label='Search age (exact match)!'
                  )

    search_prix = forms.CharField(
                    required = False,
                    label='prix'
                  )

