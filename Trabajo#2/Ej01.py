import time

""" Lee el archivo carácter por carácter """
def leer_caracter_por_caracter(ruta):
    inicio = time.time()
    with open(ruta, "r") as f:
        while True:
            caracter = f.read(1)  
            if not caracter:
                break
    fin = time.time()
    return fin - inicio

""" Lee el archivo línea por línea """
def leer_linea_por_linea(ruta):
    inicio = time.time()
    with open(ruta, "r") as f:
        for linea in f:  
            pass
    fin = time.time()
    return fin - inicio

""" Lee el archivo por bloques de un tamaño específico """
def leer_por_bloques(ruta, tam_bloque=4096):
    inicio = time.time()
    with open(ruta, "r") as f:
        while True:
            bloque = f.read(tam_bloque)  
            if not bloque:
                break
    fin = time.time()
    return fin - inicio

""" En el archivo se incluyo la biblioteca time para medir el tiempo de ejecución de cada método de lectura."""

"""
1. Caracter por caracter es la más lenta, por mucho. Cada llamada tiene un "overhead" que se repite millones de veces lo cual lo vuelve la mas lenta

2. Línea por línea es más rápida porque Python ya usa buffering internamente. no hace una llamada al sistema por cada carácter.

3. Por bloques de 4096 bytes suele ser la más rápida , porque 4096 bytes coincide con el tamaño típico de página/bloque del sistema de archivos, así que se aprovecha mejor la forma en que el disco entrega datos, con pocas llamadas al sistema."""