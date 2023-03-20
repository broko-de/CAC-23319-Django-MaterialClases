from persona import Estudiante,Docente
from curso import Categoria,Curso

class Comision:

    def __init__(self,nombre,horario,link_meet,curso,docente):
        self.__nombre = nombre
        self.__horario = horario
        self.__link_meet = link_meet
        self.__curso = curso
        self.__docente = docente
        self.__inscripciones = []

    def __str__(self) -> str:
        return f'C#{self.__nombre} ({self.__curso.nombre}) - Docente: {self.__docente.nombre_completo}'
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def horario(self):
        return self.__horario
    
    @horario.setter
    def horario(self,nuevo_horario):
        self.__horario = nuevo_horario

    @property
    def link_meet(self):
        return self.__link_meet
    
    @link_meet.setter
    def link_meet(self,nuevo_link_meet):
        self.__link_meet = nuevo_link_meet

    @property
    def curso(self):
        return self.__nombre
    
    @curso.setter
    def curso(self,nuevo_curso):
        self.__curso = nuevo_curso
    
    @property
    def docente(self):
        return self.__docente
    
    @docente.setter
    def docente(self,nuevo_docente):
        self.__docente = nuevo_docente
    
    @property
    def inscripciones(self):
        return self.__inscripciones
    
    def agregar_inscripcion(self,inscripcion):
        self.__inscripciones.append(inscripcion)

    def remover_inscripcion(self, inscripcion):
        inscripcion.comision = None
        self.__inscripciones.remove(inscripcion)

    def imprimir_nomima_inscripciones(self):
        for inscripcion in self.__inscripciones:
            if isinstance(inscripcion,Inscripcion):
                print(f'{inscripcion.estudiante.nombre_completo} esta inscripto')

class Inscripcion:

    def __init__(self,fecha,estado,comision,estudiante):
        self.__fecha = fecha
        self.__estado = estado
        self.__estudiante = estudiante  
        self.__comision = comision
        if comision:
            comision.agregar_inscripcion(self)

    @property
    def fecha(self):
        return self.__fecha
    
    @fecha.setter
    def fecha(self,nuevo_fecha):
        self.__fecha = nuevo_fecha
    
    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self,nuevo_estado):
        self.__estado = nuevo_estado
    
    @property
    def comision(self):
        return self.__comision

    @comision.setter
    def comision(self,nueva_comision):
        self.__comision = nueva_comision

    @property
    def estudiante(self):
        return self.__estudiante
    
    @estudiante.setter
    def estudiante(self,nuevo_estudiante):
        self.__estudiante = nuevo_estudiante      

categoria_web = Categoria('Desarrollo Web')
curso_django = Curso('Django','Una descripcion','2023-02-27','portada.png',categoria_web)
print(curso_django)


docente_django = Docente('Fede','Liquin',23444111,'fede@liquin.com','DT-23344')
print(docente_django.nombre_completo)

comision_23319 = Comision('23319','Martes y Jueves 10:00-11:30','link',curso_django,docente_django)
print(comision_23319)


estudiante_uno = Estudiante('Susana','Horia',23444111,'Susana@Horia.com','ES-6666')

estudiante_dos = Estudiante('Fulanito','Cosme',21555111,'Fulanito@Cosme.com','ES-5555')


inscripcion_uno = Inscripcion('2023-03-22','Inscripto',comision_23319,estudiante_uno)
inscripcion_dos = Inscripcion('2023-03-10','Inscripto',comision_23319,estudiante_dos)

comision_23319.imprimir_nomima_inscripciones()


