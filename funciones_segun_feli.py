from PIL import Image
import numpy as np
import os
 
def convert_ruta(ruta: str) -> str | np.ndarray:
    """
    Esta funcion verifica si la ruta ingresa es efectivamemte una ruta, y devuelve la forma numerica 
    de la ruta ingresada
    """
    flag = os.path.exists(ruta)
    bandera = False

    while not bandera:
         if flag:
            matriz_img = np.array(Image.open(ruta))
            return matriz_img

    if not flag:
        return "No se encontró la imagen. Por favor, verifique la ruta e intente nuevamente."
    
    if flag:
        matriz_img = np.array(Image.open(ruta))
        return matriz_img


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
            

    


