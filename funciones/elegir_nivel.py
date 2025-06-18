import pygame as pg

def pantalla_dificultad(pantalla, fuente, colores) -> str:
    botones_niveles = {
        "Facil": pg.Rect(300, 150, 200, 50),
        "Medio": pg.Rect(300, 230, 200, 50),
        "Difcil": pg.Rect(300, 310, 200, 50),
        "Volver": pg.Rect(300, 390, 200, 50),
    }

    while True:
        pantalla.fill(colores["BLANCO"])
        titulo = fuente.render("Selecciona la dificultad", True, colores["NEGRO"])
        pantalla.blit(titulo, (250, 80))

        for texto, rect in botones_niveles.items():
            pg.draw.rect(pantalla, colores["NEGRO"], rect, border_radius=10)
            render = fuente.render(texto, True, colores["BLANCO"])
            pantalla.blit(render, (rect.x + 40, rect.y + 10))

        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                pg.quit()
                exit()
            elif evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
                for texto, rect in botones_niveles.items():
                    if rect.collidepoint(evento.pos):
                        if texto == "Volver":
                            return None
                        else:
                            return texto.lower()  # Devuelve "facil", "medio" o "dificil"

        pg.display.flip()
