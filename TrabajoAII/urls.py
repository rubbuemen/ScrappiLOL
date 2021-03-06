"""TrabajoAII URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('populate_django/', views.populateDjango),
    path('populate_whoosh/', views.populateWhoosh),
    path('list_campeones/', views.list_campeones),
    path('list_jugadores/', views.list_jugadores),
    path('mejores_campeones/', views.mejores_campeones),
    path('mejores_jugadores/', views.mejores_jugadores),
    path('counterest_campeones/', views.counterestChamps),
    path('weak_campeones/', views.weakChamps),
    path('campeones_posicion/', views.list_campeones_por_posicion),
    path('list_campeones_por_posicion_tier/', views.list_campeones_por_posicion_tier),
    path('seach_champion/', views.getChampionByName),
    path('seach_champions_dates/', views.getChampionByRangeDates),
    path('seach_player/', views.getPlayerByName),
    path('recomend_champion/', views.recomendacionChampion),
    path('recomend_player/', views.recomendacionPlayer),
    path('ingresar_whoosh/', views.ingresarWhoosh),
    path('ingresar_django/', views.ingresarDjango),
    path('admin/',admin.site.urls)
]
