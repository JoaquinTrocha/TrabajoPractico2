from funciones_grupotrocha import *
from PIL import Image
import numpy as np
from funciones_segun_feli.py import *


#Main code


#Ruta y verificacion de que sea una ruta
ruta = input('Ingrese la ruta de la imagen a procesar:')

#Metodo a elegir
metodo = input('Qué metodo de filtro desea usar (pixel o ascii):')

#Casos
if metodo != 'pixel' or metodo != 'ascii':
    print('Ingrese un metodo de filtro correcto')

#   Si elige pixel
if metodo == 'pixel':
    tam_bloque = input('Seleccione el tamaño del bloque (default=10):')
    nivel_color = input('Seleccione la cantidad de niveles de color (default=4):')
    pixel_art(matriz_img)


#poner en la funcion el default de 10
if metodo == 'ascii':
    ancho = input('Ingrese el ancho de la imagen (enter si no se especifica):')
    if ancho == '':
        ancho = 10 
    else:
        int(ancho)
    ascii_art(matriz_img)

    def guardar_ascii_art(ascii_art: str, ruta_salida: str):
        with open(imagen, 'w') as f:
            f.write(ascii_art)


