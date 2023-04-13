from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.index_administracion,name='inicio_administracion'),
]
