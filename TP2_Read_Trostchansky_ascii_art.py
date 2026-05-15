from PIL import Image
import numpy as np
import os


#Funcion  Ascii

def ascii_art(ruta: str, ancho_nuevo: int) -> str:
    """
    Esta funcion lo que hace es convertir una imagen, a traves de la ruta ingresada
    por el usario, a una cadena respetando como es visualemte la imagen 
    """
    paleta = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

    matriz_img_gris = np.array ((Image.open(ruta)).convert('L'))
    mat_copia = matriz_img_gris.copy()
    alto, ancho = matriz_img_gris.shape
    min = matriz_img_gris.min()
    max = matriz_img_gris.max()

    for i in range(alto):
        for j in range(ancho):

            pixel = matriz_img_gris[i][j]
            intensidad_pixel = ((pixel - min)/(max - min)) * 255
            mat_copia[i][j] = intensidad_pixel

    alto_nuevo = int((alto * ancho_nuevo / ancho) * 0.45)
    img_redim = Image.fromarray(mat_copia).resize((ancho_nuevo, alto_nuevo))

    str_final = ""
    matriz_redim = np.array(img_redim)

    for i in range(alto_nuevo):
        for j in range(ancho_nuevo):

            pixel_n = matriz_redim[i][j]
            indice_paleta = round((1 - pixel_n / 255) * (70 - 1))
            str_final += paleta[indice_paleta]

        str_final += "\n"

    
    return str_final
