import pygame as pg
from funciones.modulos.pantalla import*


def pantalla_dificultad(pantalla, fuente, colores) -> str:
    botones_niveles = {
        "FACIL": pg.Rect(300, 180, 200, 50),
        "MEDIO": pg.Rect(300, 260, 200, 50),
        "DIFICIL": pg.Rect(300, 340, 200, 50),
        "VOLVER": pg.Rect(300, 420, 200, 50),
    }
    fuente2 = pg.font.SysFont("Berlin Sans FB", 42)


    while True:
        fondo2 = pg.image.load("02.jpg")
        pantalla.blit(fondo2, (0, 0))
        titulo = fuente2.render("SELECCIONA LA DIFICULTAD", True, colores["NEGRO"])
        pantalla.blit(titulo, (150, 80))

        for texto, rect in botones_niveles.items():
            pg.draw.rect(pantalla,colores["NEGRO"], rect, width=2, border_radius=10)
            render = fuente.render(texto, True, colores["NEGRO"])
            pantalla.blit(render, (rect.x + 40, rect.y + 10))

        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                pg.quit()
                exit()
            elif evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
                for texto, rect in botones_niveles.items():
                    if rect.collidepoint(evento.pos):
                        if texto == "VOLVER":
                            return None
                        
        pg.display.flip()
