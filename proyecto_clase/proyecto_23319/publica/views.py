from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader

from publica.forms import ContactoForm

from datetime import datetime

# Create your views here.
def index(request):    
    mensaje=None
    if(request.method=='POST'):
        contacto_form = ContactoForm(request.POST)
        mensaje='Hemos recibido tus datos'
        # acción para tomar los datos del formulario
    else:
        contacto_form = ContactoForm()
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

    context = {                
                'cursos':listado_cursos,
                'mensaje':mensaje,
                'contacto_form':contacto_form
            }
    return render(request,'publica/index.html',context)

def quienes_somos(request):
    template = loader.get_template('publica/quienes_somos.html')
    context = {'titulo':'Codo A Codo - Quienes Somos'}
    return HttpResponse(template.render(context,request))

def ver_cursos(request):
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
    return render(request,'publica/cursos.html',{'cursos':listado_cursos})

def api_proyectos(request,):
    proyectos = [{
        'autor': 'Gustavo Villegas',
        'portada': 'https://agenciadeaprendizaje.bue.edu.ar/wp-content/uploads/2021/12/Gustavo-Martin-Villegas-300x170.png',
        'url':'https://marvi-artarg.web.app/'
    },{
        'autor': 'Enzo Martín Zotti',
        'portada': 'https://agenciadeaprendizaje.bue.edu.ar/wp-content/uploads/2022/01/Enzo-Martin-Zotti-300x170.jpg',
        'url':'https://hablaconmigo.com.ar/'
    },{
        'autor': 'María Echevarría',
        'portada': 'https://agenciadeaprendizaje.bue.edu.ar/wp-content/uploads/2022/01/Maria-Echevarria-300x170.jpg',
        'url':'https://compassionate-colden-089e8a.netlify.app/'
    },]
    response = {'status':'Ok','code':200,'message':'Listado de proyectos','data':proyectos}
    return JsonResponse(response,safe=False)

def proyectos(request):    
    return render(request,'publica/proyectos.html')

#NO USAR
def hola_mundo(request):
    return HttpResponse('Hola Mundo Django 🦄')

def index_old(request):
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