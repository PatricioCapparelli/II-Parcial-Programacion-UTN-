import pygame as pg
from funciones.modulos.juego import jugar
from funciones.modulos.puntajes import mostrar_puntajes_json

# Botones del menu (definidos una sola vez)
botones = {
    "Nivel": pg.Rect(300, 100, 200, 50),
    "Jugar": pg.Rect(300, 180, 200, 50),
    "Ver Puntajes": pg.Rect(280, 260, 250, 50),
    "Salir": pg.Rect(300, 340, 200, 50)
}

def dibujar_botones(pantalla, fuente, colores):
    # Usamos la variable global botones directamente
    for texto, rect in botones.items():
        pg.draw.rect(pantalla, colores["AZUL"], rect)
        pg.draw.rect(pantalla, colores["NEGRO"], rect, 2)
        texto_render = fuente.render(texto, True, colores["BLANCO"])
        pantalla.blit(
            texto_render,
            (rect.x + (rect.width - texto_render.get_width()) // 2,
             rect.y + (rect.height - texto_render.get_height()) // 2)
        )

def menu_principal(pantalla, fondo, fuente, colores):
    corriendo = True
    while corriendo:
        pantalla.blit(fondo, (0, 0))
        dibujar_botones(pantalla, fuente, colores)
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                corriendo = False
            elif evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
                for texto, rect in botones.items():
                    if rect.collidepoint(evento.pos):
                        if texto == "Salir":
                            corriendo = False
                        elif texto == "Nivel":
                            print("Elegir nivel...")
                        elif texto == "Jugar":
                            jugar(pantalla, fuente, colores)
                        elif texto == "Ver Puntajes":
                            mostrar_puntajes_json(pantalla, fuente, colores)
        pg.display.flip()
