# from django.http import HttpResponse
from django.urls import path
from .  import  views 

urlpatterns = [
  path('', views.menu, name='home' ),
  # path('menu', views.menu, name='menu'),
  path('authenticite', views.authenticite, name='authenticite'),
  path('raport', views.raport, name='raport'),
  path('end', views.end, name='end'),
  path('deconnexion', views.deconnexion, name='deconnexion'),
]