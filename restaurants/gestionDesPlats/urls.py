from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.accueil, name='accueil'),
        url(r'^plat/(\d+)$', views.lire, name='lire'),
        url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', views.addition)

]
