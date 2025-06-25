import pygame as pg
from funciones.modulos.puntajes import guardar_puntaje_json
from funciones.modulos.tablero import crear_tablero_inicial
from funciones.pantallas.pantalla_juego import pantalla_juego

def pedir_nick(pantalla, fuente, colores):
    nick = ""
    activo = True
    while activo:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                activo = False
            elif evento.type == pg.KEYDOWN:
                if evento.key == pg.K_RETURN and len(nick) > 0:
                    activo = False
                elif evento.key == pg.K_BACKSPACE:
                    nick = nick[:-1]
                elif len(nick) < 10:
                    nick += evento.unicode

        pantalla.fill(colores["gris"])
        texto = fuente.render("Ingresa tu nick y presiona ENTER:", True, colores["negro"])
        pantalla.blit(texto, (50, 100))
        caja = pg.Rect(50, 150, 500, 40)
        pg.draw.rect(pantalla, colores["blanco"], caja)
        pg.draw.rect(pantalla, colores["negro"], caja, 2)
        texto_nick = fuente.render(nick, True, colores["negro"])
        pantalla.blit(texto_nick, (caja.x + 5, caja.y + 5))
        pg.display.flip()

    return nick

def jugar(pantalla, fuente, colores, dificultad, nick=None):
    if nick == None:
        nick = pedir_nick(pantalla, fuente, colores)

    matriz = crear_tablero_inicial(dificultad)
    resultado, puntaje = pantalla_juego(pantalla, fuente, colores, matriz, dificultad)

    if resultado == "reiniciar":
        valor = jugar(pantalla, fuente, colores, dificultad, nick)
    else:
        guardar_puntaje_json(nick, puntaje)
        valor = nick  # nick actualizado
        
    return valor