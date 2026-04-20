from funciones_grupotrocha import *
from PIL import Image
import numpy as np

#Main code

imagen = Image.open(input('Ingrese la ruta de la imagen a procesar:'))
matriz_img = np.array(imagen)

metodo = input('Qué metodo de filtro desea usar (pixel o ascii):')

if metodo != 'pixel' or metodo != 'ascii':
    print('Ingrese un metodo de filtro correcto')

if metodo == 'pixel':
    pixel = input('Seleccione el tamaño del bloque:')
    nivel_color = input('Seleccione la cantidad de niveles de color')
    filtro_pixel(matriz_img)


#poner en la funcion el default de 10
if metodo == 'ascii':
    ancho = input('Ingrese el ancho de la imagen (enter si no se especifica):')
    if ancho == '':
        ancho = 10 
    else:
        int(ancho)
    filtro_ascii(matriz_img)


