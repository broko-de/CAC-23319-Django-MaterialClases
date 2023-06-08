from django.db import models

from django.utils.text import slugify 
from django.contrib.auth.models import AbstractUser
from django.urls import reverse_lazy

# Create your models here.
#Modelo UNICO - SOLUCION 1
# class PersonaU(models.Model):
#     nombre = models.CharField(max_length=100,verbose_name='Nombre')
#     apellido = models.CharField(max_length=150,verbose_name='Apellido')
#     email = models.EmailField(max_length=150,null=True)
#     dni = models.IntegerField(verbose_name="DNI")
#     matricula = models.CharField(max_length=10,verbose_name='Matricula',null=True)
#     baja = models.BooleanField(default=0,null=True)
#     legajo = models.CharField(max_length=10,verbose_name='Legajo',null=True)

#Modelo Abtracto - SOLUCION 2
# class PersonaAbs(models.Model):
#     nombre = models.CharField(max_length=100,verbose_name='Nombre')
#     apellido = models.CharField(max_length=150,verbose_name='Apellido')
#     email = models.EmailField(max_length=150,null=True)
#     dni = models.IntegerField(verbose_name="DNI")

#     class Meta:
#         abstract=True

# class EstudianteAbs(PersonaAbs):
#     matricula = models.CharField(max_length=10,verbose_name='Matricula')
#     baja = models.BooleanField(default=0,null=True)

# class InstructorAbs(PersonaAbs):
#     legajo = models.CharField(max_length=10,verbose_name='Legajo')

#HERENCIA - SOLUCION 3
class Persona(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    apellido = models.CharField(max_length=150,verbose_name='Apellido')
    email = models.EmailField(max_length=150,null=True)
    dni = models.IntegerField(verbose_name="DNI")

class Estudiante(Persona):
    matricula = models.CharField(max_length=10,verbose_name='Matricula')
    baja = models.BooleanField(default=0)

    def __str__(self):
        return f"{self.matricula} - {self.nombre} {self.apellido}"
    
    def soft_delete(self):
        self.baja=True
        super().save()
    
    def restore(self):
        self.baja=False
        super().save()
    
    def obtener_baja_url(self):
        return reverse_lazy('estudiante_baja', args=[self.id])

    def obtener_modificacion_url(self):
        return reverse_lazy('estudiante_modificacion', args=[self.id])
    
    class Meta():
        verbose_name_plural = 'Estudiantes'
        # db_table = 'nombre_tabla'

class Instructor(Persona):
    legajo = models.CharField(max_length=10,verbose_name='Legajo')

class Categoria(models.Model):
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    baja = models.BooleanField(default=0)

    def __str__(self):
        return self.nombre

    def soft_delete(self):
        self.baja=True
        super().save()
    
    def restore(self):
        self.baja=False
        super().save()

class Curso(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    descripcion = models.TextField(null=True,verbose_name='Descripcion')
    fecha_inicio = models.DateField(verbose_name='Fecha de inicio',null=True,default=None)
    portada = models.ImageField(upload_to='imagenes/',null=True,verbose_name='Portada')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE) #relacion mucho a uno    

    def __str__(self):
        return self.nombre
    
    def delete(self,using=None,keep_parents=False):
        self.portada.storage.delete(self.portada.name) #borrado fisico
        super().delete()

#CONSIGNA DE TAREA: Crear el modelo de Comisión en base a estos ejemplos vistos y teniendo en 
# cuenta el diagrama de clases.
class Comision(models.Model):
    nombre = models.CharField(max_length=100,verbose_name="Nombre")
    horario = models.CharField(max_length=100,verbose_name="Horario",null=True,default=None)
    link_meet = models.URLField(max_length=100,verbose_name='Link de Meet')
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE) #relacion mucho a uno
    estudiantes = models.ManyToManyField(Estudiante,through='Inscripcion')

    def __str__(self):
        return self.nombre

    def obtener_baja_url(self):
        return reverse_lazy('comision_baja', args=[self.id])

    def obtener_modificacion_url(self):
        return reverse_lazy('comision_modificacion', args=[self.id])
    
#Modelo que genera tabla intermedia automaticamente
# class ComisionMTM(models.Model):
#     nombre = models.CharField(max_length=100,verbose_name="Nombre")
#     horario = models.CharField(max_length=100,verbose_name="Horario",null=True,default=None)
#     link_meet = models.URLField(max_length=100,verbose_name='Link de Meet')
#     curso = models.ForeignKey(Curso,on_delete=models.CASCADE) #relacion mucho a uno
#     estudiantes = models.ManyToManyField(Estudiante)

class Inscripcion(models.Model):
    
    ESTADOS = [
        (1,'Inscripto'),
        (2,'Cursando'),
        (3,'Egresado'),
    ]
    fecha_creacion = models.DateField(auto_now_add=True,verbose_name='Fecha de creacion')
    estudiante = models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    comision = models.ForeignKey(Comision,on_delete=models.CASCADE)
    estado = models.IntegerField(choices=ESTADOS,default=1)

    def __str__(self):
        return self.estudiante.nombre
    
    def obtener_baja_url(self):
        return reverse_lazy('inscripcion_baja', args=[self.id])

    def obtener_modificacion_url(self):
        return reverse_lazy('inscripcion_modificacion', args=[self.id])
    
class Usuario(AbstractUser):
    pass

class Perfil(models.Model):
    """MODELO QUE PERMITE DEL USER MODEL DE DJANGO PARA AGREGERLE CAMPOS EXTRAS"""
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE,primary_key=True)
    telefono = models.CharField(max_length=20,verbose_name='Teléfono')
    domicilio = models.CharField(max_length=20,verbose_name='Domicilio')
    foto = models.ImageField(upload_to='perfiles/',null=True,verbose_name='Foto Perfil')



class Proyecto(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    # campo del tipo slug
    nombre_slug = models.SlugField(max_length=100,verbose_name='Nombre Slug')
    anio = models.IntegerField(verbose_name='Año')
    descripcion = models.TextField(null=True,verbose_name='Descripcion')
    url = models.URLField(max_length=100,verbose_name='Url')
    portada = models.ImageField(upload_to='imagenes/proyecto/',null=True,verbose_name='Portada')    
    estudiante = models.ForeignKey(Estudiante,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.nombre_slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def delete(self,using=None,keep_parents=False):
        self.portada.storage.delete(self.portada.name) #borrado fisico
        super().delete()

    def obtener_baja_url(self):
        return reverse_lazy('proyecto_baja', args=[self.id])

    def obtener_modificacion_url(self):
        return reverse_lazy('proyecto_modificacion', args=[self.id])