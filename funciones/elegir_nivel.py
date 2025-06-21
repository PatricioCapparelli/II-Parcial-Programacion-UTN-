import pygame as pg
from funciones.modulos.pantalla import *

def pantalla_dificultad(pantalla, fuente, colores) -> str:
    fuente2 = pg.font.SysFont("Berlin Sans FB", 42)

    rect_facil = pg.Rect(300, 180, 200, 50)
    rect_medio = pg.Rect(300, 260, 200, 50)
    rect_dificil = pg.Rect(300, 340, 200, 50)
    rect_volver = pg.Rect(300, 420, 200, 50)

    dificultad = None

    while dificultad == None:
        fondo2 = pg.image.load("II-Parcial-Programacion-UTN-/Publico/imagenes/02.jpg")
        pantalla.blit(fondo2, (0, 0))

        titulo = fuente2.render("SELECCIONA LA DIFICULTAD", True, colores["NEGRO"])
        pantalla.blit(titulo, (150, 80))

        # Dibujar botones
        pg.draw.rect(pantalla, colores["NEGRO"], rect_facil, width=2, border_radius=10)
        pg.draw.rect(pantalla, colores["NEGRO"], rect_medio, width=2, border_radius=10)
        pg.draw.rect(pantalla, colores["NEGRO"], rect_dificil, width=2, border_radius=10)
        pg.draw.rect(pantalla, colores["NEGRO"], rect_volver, width=2, border_radius=10)

        pantalla.blit(fuente.render("FACIL", True, colores["NEGRO"]), (rect_facil.x + 40, rect_facil.y + 10))
        pantalla.blit(fuente.render("MEDIO", True, colores["NEGRO"]), (rect_medio.x + 40, rect_medio.y + 10))
        pantalla.blit(fuente.render("DIFICIL", True, colores["NEGRO"]), (rect_dificil.x + 40, rect_dificil.y + 10))
        pantalla.blit(fuente.render("VOLVER", True, colores["NEGRO"]), (rect_volver.x + 40, rect_volver.y + 10))

        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                pg.quit()
                exit()
            if evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
                if rect_facil.collidepoint(evento.pos):
                    dificultad = "FACIL"
                elif rect_medio.collidepoint(evento.pos):
                    dificultad = "MEDIO"
                elif rect_dificil.collidepoint(evento.pos):
                    dificultad = "DIFICIL"
                elif rect_volver.collidepoint(evento.pos):
                    dificultad = "VOLVER"

        pg.display.flip()

    return dificultad
