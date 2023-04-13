from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('quienes_somos/',views.quienes_somos,name='quienes_somos'),

    path('hola_mundo', views.hola_mundo, name='hola'),
    path('saludar/<str:nombre>/', views.saludar, name='saludar'),
    
    path('proyectos/2023/04/', views.ver_proyectos_04_2023, name='ver_proyectos_04_2023'),
    path('proyectos/<int:anio>/', views.ver_proyectos_uno, name='ver_proyectos'),
    path('proyectos/<int:anio>/<int:mes>/', views.ver_proyectos, name='ver_proyectos'),
    
]