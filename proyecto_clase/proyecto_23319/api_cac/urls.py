from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_cac import views

router = DefaultRouter()
router.register(r'estudiantes', views.EstudianteViewSet, basename='estudiante')

urlpatterns = [
    path('', include(router.urls)),   
    path('categorias/', views.categoria_list),
    path('categorias/<int:pk>/', views.categoria_detail),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]
