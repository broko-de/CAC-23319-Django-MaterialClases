class Categoria:
    
    def __init__(self,nombre):
        self.__nombre = nombre
        self.__cursos = []
        self.__baja = 0
        

    def __str__(self) -> str:
        return f'Categoria: {self.__nombre}'
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    @property
    def baja(self):
        return self.__baja

    @property
    def cursos(self):
        return self.__cursos
    
    def agregar_curso(self, curso):
        curso.categoria = self
        self.__cursos.append(curso)

    def remover_curso(self, curso):
        curso.categoria = None
        self.__cursos.remove(curso)

    def soft_delete(self):
        self.__baja = 1
    
class Curso:

    def __init__(self,nombre,descripcion,fecha_inicio,portada,categoria=None):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__fecha_inicio = fecha_inicio
        self.__portada = portada
        self.__categoria = None
        if categoria:
            categoria.agregar_curso(self)
    
    def __str__(self) -> str:
        return f'Curso: {self.__nombre} ({self.__categoria.nombre})'
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def descripcion(self):
        return self.__descripcion
    
    @descripcion.setter
    def descripcion(self,nueva_descripcion):
        self.__descripcion = nueva_descripcion

    @property
    def fecha_inicio(self):
        return self.__fecha_inicio
    
    @fecha_inicio.setter
    def fecha_inicio(self,nueva_fecha_inicio):
        self.__fecha_inicio = nueva_fecha_inicio

    @property
    def portada(self):
        return self.__portada
    
    @nombre.setter
    def portada(self,nueva_portada):
        self.__portada = nueva_portada
    
    @property
    def categoria(self):
        return self.__categoria
    
    @nombre.setter
    def categoria(self,nueva_categoria):
        self.__categoria = nueva_categoria


# categoria = Categoria('Desarrollo Web')
# curso = Curso('Django','Una descripcion','2023-02-27','portada.png',categoria)
# # print(curso)
# curso_dos = Curso('Fullstack python','Una descripcion','2023-02-27','portada2.png',categoria)

# # categoria.agregar_curso(curso)
# # categoria.agregar_curso(curso_dos)

# for curso in categoria.cursos:
#     print(curso)
