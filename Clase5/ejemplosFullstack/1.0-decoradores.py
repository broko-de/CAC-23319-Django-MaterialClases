# Son funciones que añaden funcionalidades a otras, lo estan decorando
# Esta formada por 3 funciones A,B y C,donde A recibe
# como parametro a B para devolver C. Siempre devuelve una funcion
#  Devolviendo esta funcion le da nuevas funcionalidades
# a la funcion que queremos decorar

#1- definir funciones suma - resta
#2- crear funcion decorador
#3- agregar decorador

def funcion_decoradora(funcion_parametro):
    
    def funcion_interior():

        #acciones adicionales que decoran
        print('Se inicia el calculo')
        funcion_parametro()
        #acciones adicionales que decoran
        print('Se ha terminado con el calculo')
    
    return funcion_interior


@funcion_decoradora
def suma():
    #print(a+b)
    print(10+2)

def resta():
    #print(a-b)
    print(23-4)

suma()
resta()
#suma(4,5)

#resta(10,45)