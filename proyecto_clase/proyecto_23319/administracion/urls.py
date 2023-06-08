from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.index_administracion,name='inicio_administracion'),
    path('categorias/', views.categorias_index,name='categorias_index'),
    path('categorias/nuevo/', views.categorias_nuevo,name='categorias_nuevo'),
    path('categorias/editar/<int:id_categoria>', views.categorias_editar,name='categorias_editar'),
    path('categorias/eliminar/<int:id_categoria>', views.categorias_eliminar,name='categorias_eliminar'),

    path('cursos/', views.cursos_index,name='cursos_index'),
    path('cursos/nuevo/', views.cursos_nuevo,name='cursos_nuevo'),
    path('cursos/editar/<int:id_curso>', views.cursos_editar,name='cursos_editar'),
    path('cursos/eliminar/<int:id_curso>', views.cursos_eliminar,name='cursos_eliminar'),


    path('categoriasview/', views.CategoriaListView.as_view(),name='categorias_index_view'),
    path('categorias/viewnuevo', views.CategoriaCreateView.as_view(),name='categorias_nuevo_view'),
    path('categorias/vieweditar/<int:pk>', views.CategoriaUpdateView.as_view(),name='categorias_editar_view'),
    path('categorias/vieweliminar/<int:pk>', views.CategoriaDeleteView.as_view(),name='categorias_eliminar_view'),

    path('comision/', views.ComisionListView.as_view(), name='comision_index'),
    path('comision/alta', views.ComisionCreateView.as_view(), name='comision_alta'),
    path('comision/modificacion/<int:pk>', views.ComisionUpdateView.as_view(), name='comision_modificacion'),
    path('comision/baja/<int:pk>', views.ComisionDeleteView.as_view(), name='comision_baja'),

    path('estudiante/', views.EstudianteListView.as_view(), name='estudiante_index'),
    path('estudiante/alta', views.EstudianteCreateView.as_view(), name='estudiante_alta'),
    path('estudiante/modificacion/<int:pk>', views.EstudianteUpdateView.as_view(), name='estudiante_modificacion'),
    path('estudiante/baja/<int:pk>', views.EstudianteDeleteView.as_view(), name='estudiante_baja'),

    path('inscripcion/', views.InscripcionListView.as_view(), name='inscripcion_index'),
    path('inscripcion/alta', views.InscripcionCreateView.as_view(), name='inscripcion_alta'),
    path('inscripcion/modificacion/<int:pk>', views.InscripcionUpdateView.as_view(), name='inscripcion_modificacion'),
    path('inscripcion/baja/<int:pk>', views.InscripcionDeleteView.as_view(), name='inscripcion_baja'),

    path('proyecto/', views.ProyectoListView.as_view(), name='proyecto_index'),
    path('proyecto/alta', views.ProyectoCreateView.as_view(), name='proyecto_alta'),
    path('proyecto/modificacion/<int:pk>', views.ProyectoUpdateView.as_view(), name='proyecto_modificacion'),
    path('proyecto/baja/<int:pk>', views.ProyectoDeleteView.as_view(), name='proyecto_baja'),
]
