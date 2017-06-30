from django.http import Http404
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from gestionDesPlats.models import Plat

#-*- coding: utf-8 -*-

def accueil(request):

    """ Afficher les plats """
    plats = Plat.objects.all()
    return render(request, 'gestionDesPLats/accueil.html', {'dernier_plat' : plats})

def lire(request, id):
    plat = get_object_or_404(Plat, id=id)
    return render(request, 'gestionDesPlats/lire.html', {'plat': plat})

def addition(request, nombre1, nombre2):

    total = int(nombre1) + int(nombre2)
    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'gestionDesPlats/addition.html', locals())
