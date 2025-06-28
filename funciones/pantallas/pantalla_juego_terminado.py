import pygame as pg
import pygame.mixer as mixer
from funciones.pantallas.pantalla import *
from funciones.recursos.botones import dibujar_botones

mixer.init()

def pantalla_victoria(pantalla, fuente, colores, botones, evento):
    """
    Devuelve:
        valor = 0  → no se hizo clic
        valor = 1  → clic en "VOLVER A MENU"
    """
    valor = 0 #flag    
    fondo = pg.image.load("publico/imagenes/batalla-ganada.webp")
    fondo_escalado = pg.transform.scale(fondo, (800, 600))
    pantalla.blit(fondo_escalado, (0, 0))

    dibujar_botones(pantalla, fuente, colores,  botones["VOLVER A MENU"], "VOLVER A MENU",color_relleno="verde_militar", color_fuente="blanco")

    if evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
        if botones["VOLVER A MENU"].collidepoint(evento.pos):
            mixer.music.stop()
            fondo = None
            fondo_escalado = None
            valor = 1      # se hizo clic

    pg.display.flip()

    return valor         
