from PIL import Image
import numpy as np
from funciones_metodos import *
from ascii_art import *
from pixel_art import *

#Main code   


#Ruta y verificacion de que sea una ruta
tupla = convert_ruta(input('Ingrese la ruta de la imagen a procesar:'))

while type(tupla) == str:
    tupla = convert_ruta(input('No se encontró la imagen. Por favor, verifique la ruta e intente nuevamente:'))

matriz_img, ruta = tupla

#Metodo a elegir
metodo = input('Qué metodo de filtro desea usar (pixel o ascii):')

#Casos
while metodo != 'pixel' and metodo != 'ascii':
    print('Ingrese un metodo de filtro correcto')
    metodo = input('pixel o ascii:')

#   Si elige pixel:
if metodo == 'pixel':

    tam_bloque = input('Seleccione el tamaño del bloque (default = 10):')
    if tam_bloque == "":
        tam_bloque = 10
    else:
        while not (tam_bloque.isdecimal()):
            tam_bloque = input('Seleccione el tamaño del bloque (default = 10):')
        
        while int(tam_bloque) <= 0: 
            tam_bloque = input("Ingrese un numero positvo de tamaño de bloque (default = 10)")
        tam_bloque = int(tam_bloque)

    niveles = input('Seleccione la cantidad de niveles de color (default = 4):')
    if niveles == "":
        niveles = 4
    else:
        while not (niveles.isdecimal()):
            niveles = input("Seleccione la cantidad de niveles de color correctamente(default = 4):")
        
        while int(niveles) <= 0:
            niveles = input("Ingrese una cantidad de niveles de color positiva (default = 4):")

        niveles = int(niveles)

    nombre_archivo = input("Ingrese un nombre para el archivo de salida:")
    ruta_guardado = "Imagenes_resultados/" + nombre_archivo + ".png"
    (Image.fromarray(pixel_art(matriz_img, tam_bloque, niveles))).save(ruta_guardado)

#   Si elige ascii:
if metodo == 'ascii':

    ancho_nuevo = input('Ingrese el ancho de la imagen ASCII (default=100):')
    if ancho_nuevo == '':
        ancho_nuevo = 100
    else:
        while not (ancho_nuevo.isdecimal()):
            ancho_nuevo = input("Ingrese el ancho de la imagen ASCII (default=100):")
        
        while int(ancho_nuevo) <= 0:
            ancho_nuevo = input("El ancho de la imagen ASCII debe ser un número positivo:")

        ancho_nuevo = int(ancho_nuevo)
    
    nombre_archivo = input("Ingrese un nombre para el archivo de salida:")
    ruta_guardado = "Imagenes_resultados/" + nombre_archivo + ".txt"
    guardar_ascii_art(ascii_art(ruta, ancho_nuevo), ruta_guardado)
            



