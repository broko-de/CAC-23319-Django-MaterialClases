"""
En algunas ocasiones nuestros programas pueden fallar ocasionando su detención.
Ya sea por errores de sintaxis o de lógica, 
tenemos que ser capaces de detectar esos momentos y tratarlos debidamente para prevenirlos
Las excepciones son bloques de código que nos permiten continuar con la ejecución de un programa pese a que ocurra un error.

"""
#MANEJO DE UNA EXCEPCION
def division(a,b):
    try:
        resultado = a/b
        print(resultado)
    except ZeroDivisionError:
        print('No se puede realizar la división por 0')

#MULTIPLE EXCEPCIONES
def division_excepciones(a):
    try:
        divisor = float(input('Ingrese el divisor: '))
        resultado = a/divisor
        print(resultado)
    except TypeError:
        print("No se puede dividir el número con un string")
    except ValueError:
        print('Debe ingresar un valor numerico')
    except ZeroDivisionError:
        print('No se puede dividir por 0')

def division_sin_exc(a,b):
    return a/b

def seleccionEquipo(listaEquipos):
    try:
        print(listaEquipos)
        index = int(input('Elige tu equipo favorito (indica el numero): '))
        print(f'Tu equipo favorito ies {listaEquipos[index]}')
    except Exception as e: #cambiarlo por ZeroDivisionError
        print(e)
        print(type(e).__name__)
        print("Ha ocurrido un error, algo a salido mal")


def main():
    
    #1-EXPECIONES
    #a = 20/0 mostrar la excepcion
    #n = int(input('ingrese un numero entero: '))
    #print(n)

    #2-Ejemplo Ex
    # division(10,0)
    # division(10,3)

    #3-Multiple ex
    #division_excepciones(20)

    #4- EXCEPCION GENERICA y PROPAGACION
    # division_sin_exc(20,3)
    # try:
    #     division_sin_exc(20,0)
    # except Exception as e:
    #     print('Algo raro paso',e)
    

    #5 Else, Finally, Raise (permite lanzar una excepcion)
    while True:
        try:
            total = 0
            sumandos = input("Ingresa numeros separados por espacios: ")
            sumandos = sumandos.split() #convierto en una lista
            for num in sumandos:
                if num.isnumeric():
                    total += float(num)
                else:
                    raise ValueError('El valor ingresado no es numerico')
        except ValueError as e:
            print(e)
            print('Vuelve a ingresar los numeros: ')
        else: # se ejecuta si el bloque try se completa sin excepciones
            print(f'La suma es: {total}')
            break
        finally: #bloque que se ejecuta independiente si ocurrio una exp o no
            print("ha terminado el proceso, se vemos")

    print('Continuo la ejecución del main')


if __name__ == '__main__':
    main()