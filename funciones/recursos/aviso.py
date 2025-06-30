import pygame as pg
from funciones.recursos.botones import dibujar_botones

def aviso(pantalla:tuple, fuente:str, colores:dict, mensaje:str, ms:int=1500, color_relleno:tuple="rojo", ancho:int=440, alto:int=70, offset_y=100):
    '''Se encarga de avisar al jugador de que elija un nivel antes de tocar "jugar"
    args:
    -pantalla: Recibe el tamaño de la pantalla.
    -fuente: Recibe la fuente del texto
    -colores:Recibe el diccionario de colores.
    -mensaje:Recibe el mensaje que va a mostrar el aviso
    -ms:Recibe los milisegundos que dura el aviso que por defecto está establecido en 1500
    -color_relleno:Recibe el nombre del color de relleno del aviso definido en el diccionario colores, que por defecto esta puesto en rojo.
    -ancho:Recibe el ancho del aviso
    -alto:Recibe el alto del aviso
    -offset_y:
    Return:Ninguno
    '''
    rect = pg.Rect(0, 0, ancho, alto)
    rect.centerx = pantalla.get_width() // 2   # horizontal
    rect.y = offset_y   # un poco abajo del borde superior

    dibujar_botones(pantalla, fuente, colores,
                    rect, mensaje, color_relleno=color_relleno)

    pg.display.flip()
    pg.time.wait(ms)

    # EVENTOS DEL JUEGO
        