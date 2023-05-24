from django.contrib import admin
from administracion.models import Estudiante, Proyecto,Curso,Categoria

# Registro por defecto al admin de Django
# admin.site.register(Estudiante)
# admin.site.register(Proyecto)

# Creacion de un Admin Personalizado heredando de AdminSite
class CacAdminSite(admin.AdminSite):
    site_header = 'Administracion Codo a Codo'
    site_title = 'Administracion superuser'
    index_title= 'Administracion del sitio'
    empty_value_display = 'No hay datos para visualizar'

# Personalizacion de visualizacion de modelos en el Admin de Django
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ( 'matricula','nombre', 'apellido', 'dni',)
    list_editable = ('nombre',)
    list_filter = ('dni',)
    search_fields = ('nombre','apellido')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ( 'nombre',)

    #modificacion del listado que se quiere mostrar
    def get_queryset(self, request):
        query = super(CategoriaAdmin, self).get_queryset(request)
        filtered_query = query.filter(baja=False)
        return filtered_query

class CursoAdmin(admin.ModelAdmin):

    #modificar listados de foreingkey
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "categoria":
            kwargs["queryset"] = Categoria.objects.filter(baja=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

#registros de modelos en Admin personalizado
sitio_admin = CacAdminSite(name='cacadmin')
sitio_admin.register(Estudiante,EstudianteAdmin)
sitio_admin.register(Proyecto)
sitio_admin.register(Categoria,CategoriaAdmin)
sitio_admin.register(Curso,CursoAdmin)