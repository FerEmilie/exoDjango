from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^accueil$', views.home),  # Accueil du blog

    url(r'^gestionrestaurant/(\d+)$', views.view_restaurant),  # Vue d'un menu

    url(r'^date$', views.date_actuelle), # Vue date actuelle

    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', views.addition)  # Vue addition
]
