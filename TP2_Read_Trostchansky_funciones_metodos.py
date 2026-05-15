from PIL import Image
import numpy as np
import os
 
def convert_ruta(ruta: str) -> str | tuple :
    """
    Esta funcion verifica si la ruta ingresa es efectivamemte una ruta, y devuelve la forma numerica 
    de la ruta ingresada
    """
    flag = os.path.exists(ruta)

    if not flag:
        return "No se encontró la imagen. Por favor, verifique la ruta e intente nuevamente."
    
    if flag:
        matriz_img = np.array(Image.open(ruta))
        return (matriz_img, ruta)

def guardar_ascii_art(ascii_art: str, ruta_guardado: str):
    with open(ruta_guardado, 'w') as f:
        f.write(ascii_art)
            

    


