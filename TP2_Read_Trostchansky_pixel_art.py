from PIL import Image
import numpy as np
import os

#Funcion Pixel art 

def pixel_art(matriz_img: np.ndarray, tam_bloque: int = 10, niveles: int = 4) -> np.ndarray:
    """
    Esta funcion recibe la forma numerica de una imagen, y con un tamaño de bloque determinado, y una
    cantidad de niveles determinada, devuelve una nueva forma numerica de la imagen con el metodo de pixel 
    art
    """

    alto, ancho, canales = matriz_img.shape 
    salida = matriz_img.copy()
    valores = np.linspace(0, 255, niveles)

    for i in range(0, alto, tam_bloque):
        for j in range(0, ancho, tam_bloque):
            bloque = matriz_img[i: i + tam_bloque, j: j+ tam_bloque, : ]

            color_promedio = bloque.mean(axis = (0, 1))
            color_final = []

            for canal in color_promedio:
                valor_cercano = valores[0]
                menor_distancia = abs(canal - valor_cercano)
                
                for valor in valores:
                    distancia = abs(canal - valor)
                    if distancia < menor_distancia:
                        menor_distancia = distancia
                        valor_cercano = valor 

                color_final.append(valor_cercano)

            salida[i: i + tam_bloque, j: j + tam_bloque, :] = color_final

    return salida.astype(np.uint8)
