#-*- coding: utf-8 -*-

# Create your views here.
from django.http import HttpResponse
def home(request):

    """ Exemple de page HTML, non valide pour que l'exemple soit concis """

    text = """<h1>Bienvenue sur la gestion du restaurant Pile ou Face!</h1>

             """

    return HttpResponse(text)
def view_restaurant(request, id_restaurant):

    """

    Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)

    Son ID est le second paramètre de la fonction (pour rappel, le premier

    paramètre est TOUJOURS la requête de l'utilisateur)

    """

    return HttpResponse(
        "Vous avez demandé l'article #{0} !".format(id_restaurant)
    )
from datetime import datetime
from django.shortcuts import render

def date_actuelle(request):
    return render(request, 'gestionrestaurant/date.html', {'date': datetime.now()})

def addition(request, nombre1, nombre2):
    total = int(nombre1) + int(nombre2)
    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'gestionrestaurant/addition.html', locals())
# Retourne nombre1, nombre2 et la somme des deux au tpl

    return render(request, 'gestionrestaurant/addition.html', locals())
