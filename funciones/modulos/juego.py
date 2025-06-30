import pygame as pg
from funciones.modulos.puntajes import guardar_puntaje_json
from funciones.modulos.tablero import crear_tablero_inicial
from funciones.pantallas.pantalla_juego import pantalla_juego
from funciones.pantallas.pantalla import *
from funciones.pantallas.pantalla_pedir_nick import pedir_nick

def jugar(pantalla, fuente, colores, dificultad, nick=None):
    '''Se encarga de mostrar la pantalla del juego iniciado.
        args:
        -pantalla:Tuple
        -fuente:Str
        -colores:Tuple
        -dificultad:Str
        -nick:Str
        return:int
        '''
    if nick == None:
        fondo = pg.image.load("publico/imagenes/02.jpg").convert()
        nick = pedir_nick(pantalla, fondo, fuente, colores)

    matriz = crear_tablero_inicial(dificultad)
    resultado, puntaje = pantalla_juego(pantalla, fuente, matriz, dificultad)

    if resultado == "reiniciar":
        valor = jugar(pantalla, fuente, colores, dificultad, nick)
    else:
        guardar_puntaje_json(nick, puntaje)
        valor = nick  # nick actualizado
        
    return valor