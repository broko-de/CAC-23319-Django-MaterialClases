from rest_framework import serializers
from administracion.models import Estudiante,Categoria

class EstudianteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Estudiante
        fields = ['id','nombre','apellido','email','dni','matricula']

class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = ['id', 'nombre']