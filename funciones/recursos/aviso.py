import pygame as pg
from funciones.recursos.botones import dibujar_botones

def aviso(pantalla, fuente, colores, mensaje, ms=1500, color_relleno="rojo", w=440, h=70, offset_y=100):
    rect = pg.Rect(0, 0, w, h)
    rect.centerx = pantalla.get_width() // 2   # horizontal
    rect.y = offset_y   # un poco abajo del borde superior

    dibujar_botones(pantalla, fuente, colores,
                    rect, mensaje, color_relleno=color_relleno)

    pg.display.flip()
    pg.time.wait(ms)

    # EVENTOS DEL JUEGO
        