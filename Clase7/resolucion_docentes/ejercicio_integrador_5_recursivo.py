from re import A


def get_int():
    user_input = input('Por favor ingrese un número: ')
    try:
        value = int(user_input)
    except ValueError:
        print('No es un entero válido. Intente nuevamente!')
        return get_int()
    else:
        return value


print(f"Número ingresado: {get_int()}")
