from rest_framework import viewsets
from rest_framework import permissions
from administracion.models import Estudiante,Categoria, Curso
from api_cac import serializers


from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.response import Response

# Create your views here.
class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all().order_by('apellido')
    serializer_class = serializers.EstudianteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def categoria_list(request):
    """
    Lista todos los proyecto, o crea un nuevo proyecto.
    """
    if request.method == 'GET':
        categorias = Categoria.objects.filter(baja=False)
        serializer = serializers.CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            #agrega mi logica
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def categoria_detail(request, pk):
    """
    Muestra, actualiza o elimina una categoria.
    """
    try:
        categoria = Categoria.objects.get(pk=pk)
    except Categoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.CategoriaSerializer(categoria)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        categoria.soft_delete()
        return Response({'message':'Se elimino la categoria'},status=status.HTTP_204_NO_CONTENT)
    