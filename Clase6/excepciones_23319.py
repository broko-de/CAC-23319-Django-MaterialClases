class DivisorNegativoError(Exception):
    """Excepción lanzada se divide por números negativos"""
    def __init__(self, message='OJO! Estas intentando dividir por un valor negativo') :
        super().__init__(message)

def mostrar_division_entera(dividendo, divisor):
    """
        parametros:
            dividendo: numero entero que sera divido
            divisor: numero por el que se va a dividir
        excepciones:
            lanzará una excepción Cuando hay una division por Cero
    """
    try:
        # assert divisor >= 0, "Mandaron un número negativo"

        if divisor < 0:            
            raise DivisorNegativoError()
        print("Intentando hacer la división") 
        resultado = dividendo // divisor 
        print(f"El resultado entero de la divisón es: {resultado}")
    
    except AssertionError as assert_error:
        print(assert_error)
        print('Le erraste a un dato...')
    except TypeError: 
        print('Revisar los operandos hay un dato mal cargado...')
    except ZeroDivisionError:
        print('No se puede dividir por cero...')        
    except DivisorNegativoError as dne:
        print(f'Algo anduvo mal personalizado: {dne}')
    except Exception as ex:
        print(f'Algo anduvo mal: {ex}')
    else:
        print("Este programa nunca falla..")
    finally:
        print('El super programa ha finalizado..')
    



mostrar_division_entera(2, -1)
print(10*'-*')
# mostrar_division_entera(2, 0)
# print(10*'-*')
# mostrar_division_entera("1", "2")
# print(10*'-*')
# mostrar_division_entera(1, 2)


# raise DivisorNegativoError("Mandaron un número negativo")
# https://docs.python.org/es/3/tutorial/errors.html