from django import forms

from .models import Curso, Categoria, Estudiante, Proyecto, Instructor, Comision, Inscripcion

class CategoriaForm(forms.ModelForm):
    # nombre = forms.CharField(error_messages={'required':'Hello! no te olvide de mi!'})

    class Meta:
        model=Categoria
        # fields='__all__'
        fields=['nombre']
        #exclude=('baja',)
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese un nombre'})
        }
        error_messages = {
            'nombre' :{
                'required':'No te olvides de mi!'
            }
        }

class CursoForm(forms.ModelForm):

    nombre=forms.CharField(
            label='Nombre',           
            widget=forms.TextInput(attrs={'class':'form-control'})
        )
    fecha_inicio=forms.DateField(
            label='Fecha Inicio', 
            widget=forms.DateInput(attrs={'class':'form-control','type':'date'})
        )
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5,'class':'form-control'})
    )
    """Se utiliza ModelChoiceField para poder realizar un filtrado de lo que
    quiero mostrar en el selector"""
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter(baja=False),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    portada = forms.ImageField(
        widget=forms.FileInput(attrs={'class':'form-control'})
    )

    class Meta:
        model=Curso
        fields=['nombre','fecha_inicio','portada','descripcion','categoria']


# Formularios asociados a modelos
class EstudianteForm(forms.ModelForm):

    class Meta:
        model=Estudiante
        fields=['nombre','apellido','email','dni','matricula']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'dni': forms.NumberInput(attrs={'class':'form-control'}),
            'matricula': forms.TextInput(attrs={'class':'form-control'}),
        }

class InstructorForm(forms.ModelForm):

    class Meta:
        model = Instructor
        fields = ("nombre", "apellido",'email','dni','legajo')
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'dni': forms.NumberInput(attrs={'class':'form-control'}),
            'legajo': forms.TextInput(attrs={'class':'form-control'}),
        }

class ProyectoForm(forms.ModelForm):

    class Meta:
        model=Proyecto
        fields=['nombre','descripcion','anio','url','portada','estudiante']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'cols': 80, 'rows': 5,'class':'form-control'}),
            'anio': forms.NumberInput(attrs={'class':'form-control'}),
            'url': forms.URLInput(attrs={'class':'form-control'}),
            'portada': forms.FileInput(attrs={'class':'form-control'}),
            'estudiante': forms.Select(attrs={'class':'form-control'}),
        }

# Formularios asociados a modelos
class InscripcionForm(forms.ModelForm):
    
    comision = forms.ModelChoiceField(
        queryset=Comision.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    estudiante = forms.ModelChoiceField(
        queryset=Estudiante.objects.filter(baja=False),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    estado = forms.ChoiceField(
        label='Estado',
        choices=Inscripcion.ESTADOS,
        widget=forms.Select(attrs={'class':'form-control'})
    )

    class Meta:
        model=Inscripcion
        fields=['comision','estudiante','estado']
        

class ComisionForm(forms.ModelForm):

    nombre = forms.CharField(
        label='Nombre',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    horario = forms.CharField(
        label='Horario',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    link_meet = forms.URLField(
        label='Link de meet',
        widget=forms.URLInput(attrs={'class': 'form-control'})
    )
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'})
    )
    curso = forms.ModelChoiceField(
        queryset=Curso.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Comision
        fields = ['nombre', 'horario','link_meet', 'descripcion', 'curso']

    
    