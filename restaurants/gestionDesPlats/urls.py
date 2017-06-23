from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.accueil, name='accueil'), 
        url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', views.addition),

]
