import pygame as pg
from funciones.pantallas.pantalla import *
from funciones.recursos.botones import *

def pantalla_dificultad(pantalla, fuente, colores, botones) -> str:
    fuente2 = pg.font.SysFont("Berlin Sans FB", 42)
    dificultad = None

    while dificultad == None:
        fondo2 = pg.image.load("publico/imagenes/02.jpg")
        pantalla.blit(fondo2, (0, 0))
        titulo = fuente2.render("SELECCIONA LA DIFICULTAD", True, colores["negro"])
        pantalla.blit(titulo, (150, 80))

        dibujar_botones(pantalla, fuente, colores, botones["FACIL"], "FACIL")
        dibujar_botones(pantalla, fuente, colores, botones["MEDIO"], "MEDIO")
        dibujar_botones(pantalla, fuente, colores, botones["DIFICIL"], "DIFICIL")
        dibujar_botones(pantalla, fuente, colores, botones["VOLVER_NIVEL"], "VOLVER")
        for evento in pg.event.get():
            if evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
                for texto, rect in botones.items(): # TEXTO == KEY // RECT == VALUE
                    if rect.collidepoint(evento.pos):
                        if texto == "FACIL":
                            dificultad = "facil"
                        elif texto == "MEDIO":
                            dificultad = "medio"
                        elif texto == "DIFICIL":
                            dificultad = "dificil"
                        elif texto == "VOLVER_NIVEL":
                            dificultad = "volver"

        pg.display.flip()

    return dificultad
