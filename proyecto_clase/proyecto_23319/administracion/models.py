from django.db import models

# Create your models here.
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
