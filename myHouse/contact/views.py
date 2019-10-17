from django.shortcuts import render
from django.http import JsonResponse
import json
from django.core.validators import validate_email
from django.contrib.auth.models import User
from .models import *
# Create your views here.

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


def senddata(request):
    #postdata = json.loads(request.body.decode('utf-8'))

    isSucces = False
    compt = 1 
    while compt < 10000000:
        compt+=1

    name = postdata['name']
    email = postdata['email']
    message = postdata['message']
    # name = postdata['name'] 
    print('====================')
    print(name)
    emailOk=False
    print(email)
    print(message)
    if ((name is not None) and (message is not None) ):
        try:
            validate_email(email)
            emailOk=True
        except:
            result = {
                'succes':True,
                'name':name,
                'email':email,
                'message':message,
            }
        if emailOk:
            try:
                user = Message(name =name, email = email,message=message)
                user.save()
                result={
                    'succes':True,
                    'message':'Enregistrement Effectue avec success '
                }
            except Exception as err:
                print(err)
                result={
                    'succes':False,
                    'message':'Error lor de l\'enregistrement '
                }
    else:
        result={
            'success':False,
            'message':'Veille verifier tous vos champs'
        }
    return JsonResponse(result, safe=False)

