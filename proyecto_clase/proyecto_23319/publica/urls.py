from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('hola_mundo', views.hola_mundo, name='hola'),
]