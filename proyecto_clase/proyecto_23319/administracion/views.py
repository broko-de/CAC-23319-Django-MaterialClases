from django.shortcuts import render, redirect

from administracion.forms import CategoriaForm, CursoForm, ComisionForm, EstudianteForm, ProyectoForm, InscripcionForm

from administracion.models import Categoria, Curso, Comision, Estudiante,Inscripcion, Proyecto

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from django.shortcuts import get_object_or_404
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
@permission_required('administracion.add_categoria')
def index_administracion(request):    
    variable = 'test variable'
    return render(request,'administracion/index_administracion.html',{'variable':variable})

"""
    CRUD Categorias
"""
def categorias_index(request):
    #queryset
    categorias = Categoria.objects.filter(baja=False)
    return render(request,'administracion/categorias/index.html',{'categorias':categorias})

def categorias_nuevo(request):
    if(request.method=='POST'):
        formulario = CategoriaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('categorias_index')
    else:
        formulario = CategoriaForm()
    return render(request,'administracion/categorias/nuevo.html',{'form':formulario})

def categorias_editar(request,id_categoria):
    try:
        categoria = Categoria.objects.get(pk=id_categoria)
    except Categoria.DoesNotExist:
        return render(request,'administracion/404_admin.html')

    if(request.method=='POST'):
        formulario = CategoriaForm(request.POST,instance=categoria)
        if formulario.is_valid():
            formulario.save()
            return redirect('categorias_index')
    else:
        formulario = CategoriaForm(instance=categoria)
    return render(request,'administracion/categorias/editar.html',{'form':formulario})

def categorias_eliminar(request,id_categoria):
    try:
        categoria = Categoria.objects.get(pk=id_categoria)
    except Categoria.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    categoria.soft_delete()
    return redirect('categorias_index')


def cursos_index(request):
    cursos = Curso.objects.all()
    return render(request,'administracion/cursos/index.html',{'cursos':cursos})

def cursos_nuevo(request):
    #forma de resumida de instanciar un formulario basado en model con los
    #datos recibidos por POST si la petición es por POST o bien vacio(None)
    #Si la petición es por GET
    formulario = CursoForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se ha creado el curso correctamente')          
        return redirect('cursos_index')
    return render(request,'administracion/cursos/nuevo.html',{'formulario':formulario})


def cursos_editar(request,id_curso):
    try:
        curso = Curso.objects.get(pk=id_curso)
    except Curso.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    formulario = CursoForm(request.POST or None,request.FILES or None,instance=curso)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se ha editado el curso correctamente')          
        return redirect('cursos_index')
    return render(request,'administracion/cursos/editar.html',{'formulario':formulario})

def cursos_eliminar(request,id_curso):
    try:
        curso = Curso.objects.get(pk=id_curso)
    except Curso.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    messages.success(request,'Se ha eliminado el curso correctamente')          
    curso.delete()
    return redirect('cursos_index')

"""
    IMPLEMENTACION DE CRUD DE CATEGORIA POR MEDIO DE VISTAS BASADAS EN CLASES (VBC)
"""
class CategoriaListView(ListView):
    model = Categoria
    context_object_name = 'categorias'
    template_name= 'administracion/categorias/index.html'
    queryset= Categoria.objects.filter(baja=False)
    ordering = ['nombre']

class CategoriaCreateView(CreateView):
    model = Categoria
    # fields = ['nombre']
    form_class = CategoriaForm
    template_name = 'administracion/categorias/nuevo.html'
    success_url = reverse_lazy('categorias_index_view')

class CategoriaUpdateView(UpdateView):
    model = Categoria
    fields = ['nombre']
    # form_class = CategoriaForm
    template_name = 'administracion/categorias/editar.html'
    success_url = reverse_lazy('categorias_index_view')

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        obj = get_object_or_404(Categoria, pk=pk)
        return obj
    
class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'administracion/categorias/eliminar.html'
    success_url = reverse_lazy('categorias_index_view')
    
    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        obj = get_object_or_404(Categoria, pk=pk)
        return obj
    
    #se puede sobreescribir el metodo delete por defecto de la VBC, para que no se realice una baja fisica
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.soft_delete()  # Llamada al método soft_delete() del modelo
        return HttpResponseRedirect(self.get_success_url())


class ComisionListView(ListView):
    model = Comision
    template_name = 'administracion/abm/index.html'
    ordering = ['nombre']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Comisiones"
        context['url_alta'] = reverse_lazy('comision_alta')
        # context['url_modificacion'] = reverse_lazy('comision_modificacion')
        # context['url_baja'] = reverse_lazy('comision_baja')
        return context


class ComisionCreateView(CreateView):
    model = Comision
    form_class = ComisionForm
    template_name = 'administracion/abm/alta_modificacion.html'
    success_url = reverse_lazy('comision_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Nueva Comision"
        context['url_accion'] = reverse_lazy('comision_alta')
        return context


class ComisionUpdateView(UpdateView):
    model = Comision
    form_class = ComisionForm
    template_name = 'administracion/abm/alta_modificacion.html'
    success_url = reverse_lazy('comision_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Modificar Comision"
        return context


class ComisionDeleteView(DeleteView):
    model = Comision
    template_name = 'administracion/abm/baja.html'
    success_url = reverse_lazy('comision_index')


class EstudianteListView(LoginRequiredMixin, ListView):
    model = Estudiante
    template_name = 'administracion/abm/index.html'
    ordering = ['nombre']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Estudiantes"
        context['url_alta'] = reverse_lazy('estudiante_alta')
        return context


class EstudianteCreateView(CreateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'administracion/abm/alta_modificacion.html'
    success_url = reverse_lazy('estudiante_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Nuevo Estudiante"
        return context


class EstudianteUpdateView(UpdateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'administracion/abm/alta_modificacion.html'
    success_url = reverse_lazy('estudiante_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Modificar Estudiante"
        return context


class EstudianteDeleteView(DeleteView):
    model = Estudiante
    template_name = 'administracion/abm/baja.html'
    success_url = reverse_lazy('estudiante_index')


class InscripcionListView(ListView):
    model = Inscripcion
    template_name = 'administracion/inscripcion/index.html'
    ordering = ['fecha_creacion']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Inscripciones"
        context['url_alta'] = reverse_lazy('inscripcion_alta')
        return context


class InscripcionCreateView(CreateView):
    model = Inscripcion
    form_class = InscripcionForm
    # fields = ['estudiante', 'comision', 'estado']
    template_name = 'administracion/abm/alta_modificacion.html'
    success_url = reverse_lazy('inscripcion_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Nueva Inscripcion"
        return context


class InscripcionUpdateView(UpdateView):
    model = Inscripcion
    form_class = InscripcionForm
    # fields = ['estudiante', 'comision', 'estado']
    template_name = 'administracion/abm/alta_modificacion.html'
    success_url = reverse_lazy('inscripcion_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Modificar Inscripcion"
        return context


class InscripcionDeleteView(DeleteView):
    model = Inscripcion
    template_name = 'administracion/abm/baja.html'
    success_url = reverse_lazy('inscripcion_index')


class ProyectoListView(ListView):
    model = Proyecto
    template_name = 'administracion/abm/index.html'
    ordering = ['nombre']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Proyectos"
        context['url_alta'] = reverse_lazy('proyecto_alta')
        return context


class ProyectoCreateView(CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'administracion/abm/alta_modificacion.html'
    success_url = reverse_lazy('proyecto_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Nuevo Proyecto"
        return context


class ProyectoUpdateView(UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'administracion/abm/alta_modificacion.html'
    success_url = reverse_lazy('proyecto_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Modificar Proyecto"
        return context


class ProyectoDeleteView(DeleteView):
    model = Proyecto
    template_name = 'administracion/abm/baja.html'
    success_url = reverse_lazy('proyecto_index')