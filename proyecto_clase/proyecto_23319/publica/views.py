from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

# Create your views here.
def hola_mundo(request):
    return HttpResponse('Hola Mundo Django 🦄')

def index(request):
    if(request.method=='GET'):
        titulo = 'Titulo cuando accedo por GET'
    else:
        titulo = 'Titulo cuando accedo por otro metodo'
    parametro_uno = request.GET.get('param')
    parametro_dos = request.GET.get('param2')
    listado_cursos = [
        {
            'nombre':'Fullstack Java',
            'descripcion':'Curso de Fullstack',
            'categoria':'Programación',
        },
        {
            'nombre':'Diseño UX/UI',
            'descripcion':'🖌🎨',
            'categoria':'Diseño',
        },
        {
            'nombre':'Big Data',
            'descripcion':'test',
            'categoria':'Análisis de Datos',
        },
        {
            'nombre':'Big Data Avanzado',
            'descripcion':'test',
            'categoria':'Análisis de Datos',
        },
    ]

    context = {'titulo':titulo,
                'parametro_uno':parametro_uno,
                'hoy':datetime.now(),
                'cursos':listado_cursos
            }
    return render(request,'publica/index.html',context)
    # return HttpResponse(f"""<h1>PROYECTO DJANGO - CODO A CODO</h1>
    #             <p>{titulo}</p>   
    #             <p>Param recibido: {parametro_uno}</p>                
    #             <p>Param2 recibido: {parametro_dos}</p>                
    #         """)

def saludar(request,nombre):
    return HttpResponse(f"""
        <h1>Hola {nombre}</h1>
        <p>Estoy haciendo una prueba</p>
    """)

def ver_proyectos(request,anio,mes):
    return HttpResponse(f"""
        <h1>Proyectos del - {mes}/{anio}</h1>
        <p>Listado de proyectos</p>
    """)

def ver_proyectos_uno(request,anio,mes=1):
    return HttpResponse(f"""
        <h1>Por defecto Proyectos del - {mes}/{anio}</h1>
        <p>Listado de proyectos</p>
    """)

def ver_proyectos_04_2023(request,):
    return HttpResponse(f"""
        <h1>Proyectos del mes de abril año 2023</h1>
        <p>Listado de proyectos</p>
    """)