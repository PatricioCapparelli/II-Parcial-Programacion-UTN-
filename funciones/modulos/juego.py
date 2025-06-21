import pygame as pg
from funciones.modulos.puntajes import guardar_puntaje_json

def pedir_nick(pantalla, fuente, colores):
    nick = ""
    activo = True
    while activo:
        for evento in pg.event.get():
            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_RETURN and len(nick) > 0:
                    activo = False
                elif evento.key == pg.K_BACKSPACE:
                    nick = nick[:-1]
                else:
                    if len(nick) < 10:
                        nick += evento.unicode
        pantalla.fill(colores["GRIS"])
        texto = fuente.render("Ingresa tu nick y presiona ENTER:", True, colores["NEGRO"])
        pantalla.blit(texto, (50, 100))
        caja = pg.Rect(50, 150, 500, 40)
        pg.draw.rect(pantalla, colores["BLANCO"], caja)
        pg.draw.rect(pantalla, colores["NEGRO"], caja, 2)
        texto_nick = fuente.render(nick, True, colores["NEGRO"])
        pantalla.blit(texto_nick, (caja.x + 5, caja.y + 5))
        pg.display.flip()
    return nick

def jugar(pantalla, fuente, colores, dificultad):
    nick = pedir_nick(pantalla, fuente, colores)
    puntaje = 123  # Aquí va la lógica del juego real
    guardar_puntaje_json(nick, puntaje)
