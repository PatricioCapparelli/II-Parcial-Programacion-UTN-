import pygame as pg
import pygame.mixer as mixer
from funciones.pantallas.pantalla import *
from funciones.recursos.botones import dibujar_botones

mixer.init()

def pantalla_victoria(pantalla:tuple, fuente:str, colores:dict, botones:dict, evento:tuple):
    """Esta funcion se encarga de administrar la pantalla de victoria

    Args:
    -pantalla:Recibe la pantalla del juego
    -fuente:Recibe al fuente del texto
    -colores:Recibe el diccionario con los colores
    -botones:Recibe el diccionario con los botones
    -evento:Recibe el evento de pygame

    Return:Retorna un booleano dependiendo de si se desea volver al menu o no.
    """
    valor = False #flag    
    fondo = pg.image.load("publico/imagenes/batalla-ganada.webp")
    fondo_escalado = pg.transform.scale(fondo, (800, 600))
    pantalla.blit(fondo_escalado, (0, 0))

    dibujar_botones(pantalla, fuente, colores, botones["VOLVER A MENU"], "VOLVER A MENU", color_relleno="verde_militar", color_fuente="blanco")

    if evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
        if botones["VOLVER A MENU"].collidepoint(evento.pos):
            mixer.music.stop()
            fondo = None
            fondo_escalado = None
            valor = True      # se hizo clic

    pg.display.flip()

    return valor         
