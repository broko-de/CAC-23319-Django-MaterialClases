from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.index_administracion,name='inicio_administracion'),
    path('categorias/', views.categorias_index,name='categorias_index'),
    path('categorias/nuevo/', views.categorias_nuevo,name='categorias_nuevo'),
    path('categorias/editar/<int:id_categoria>', views.categorias_editar,name='categorias_editar'),
    path('categorias/eliminar/<int:id_categoria>', views.categorias_eliminar,name='categorias_eliminar'),

    path('categoriasview/', views.CategoriaListView.as_view(),name='categorias_index_view'),
    path('categorias/viewnuevo', views.CategoriaCreateView.as_view(),name='categorias_nuevo_view'),
    path('categorias/vieweditar/<int:pk>', views.CategoriaUpdateView.as_view(),name='categorias_editar_view'),
    path('categorias/vieweliminar/<int:pk>', views.CategoriaDeleteView.as_view(),name='categorias_eliminar_view'),

]
