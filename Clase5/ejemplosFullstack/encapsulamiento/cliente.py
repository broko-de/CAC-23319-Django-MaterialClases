class Cliente:

    def __init__(self):
        ## Definimos un atributo privado
        self.__nombre =''
        self.__email = ''
    
    def __str__(self):
        return f'Nombre: {self.__nombre} - ({self.__email})'

    #Con el decorador property definimos el getter para obtener su valor
    @property
    def nombre(self):
        return f'Nombre: {self.__nombre}'

    #Asociamos el getter con su setter Nombre_funcion.setter para indicar que la funcion 
    #sera un setter y en este caso modificar el valor de la propiedad
    @nombre.setter
    def nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def email(self):
        return f'Email: {self.__email}'

    @email.setter
    def email(self,nuevo_email):
        self.__email=nuevo_email


