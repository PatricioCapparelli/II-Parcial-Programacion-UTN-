import pygame as pg
from funciones.pantallas.pantalla_juego import *
from funciones.pantallas.pantalla import *

def dibujar_tablero(pantalla, tablero_x, tablero_y, tam_casillero, margen, matriz, disparos_realizados, naves_hundidas, mostrar_naves, nave_intacta):
    # DIBUJAR TABLERO 
        for fila in range(len(matriz)):
            for col in range(len(matriz[0])):
                valor = matriz[fila][col]
                x = tablero_x + col * (tam_casillero + margen)
                y = tablero_y + fila * (tam_casillero + margen)

                if [fila, col] in disparos_realizados: # Celda ya visitada
                    if valor == nave_impactada:  # Parte de nave dañada
                        es_hundida = False
                        for nave in naves_hundidas:
                            if [fila, col] in nave:
                                es_hundida = True
                                break
                        if es_hundida:
                            color = colores["rojo"]
                        else:
                            color = colores["naranja"]
                    else:                                       
                        color = colores["azul"] # agua impactada
                else:     # Celda sin revelar
                    if mostrar_naves and valor == nave_intacta: # Mostrar naves (debug)
                        color = colores["verde"]    
                    else:
                        color = colores["celeste"]

                pg.draw.rect(pantalla, color, (x, y, tam_casillero, tam_casillero))
                pg.draw.rect(pantalla, colores["negro"],
                            (x, y, tam_casillero, tam_casillero), 1)