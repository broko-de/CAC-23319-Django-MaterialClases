def contar_palabras(texto):
    """Función que cuenta el número de veces que aparece cada palabra en un texto.
    Parámetros:
        - texto: Es una cadena de caracteres.
    Devuelve: 
        Un diccionario con pares palabra:frecuencia con las palabras contenidas en el texto y su frecuencia.
    """
    texto = texto.split()
    palabras = {}
    for i in texto:
        if i in palabras:
            palabras[i] += 1
        else:
            palabras[i] = 1
    return palabras


texto = 'Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera'
print(f"Cantidad de palabras: {contar_palabras(texto)}")
