import pygame as pg
from funciones.pantallas.pantalla_juego import *
from funciones.pantallas.pantalla import *

def dibujar_tablero(pantalla:tuple, tablero_x:int, tablero_y:int, tam_casillero:int, margen:int, matriz:list, disparos_realizados:list, naves_hundidas:list, mostrar_naves:bool, nave_intacta:int):
    '''Esta funcion se encarga de dibujar el tablero, verificar nave impactada y nave hundida, a la vez que pinta los casilleros de colores segun si esta impactada, hundida o es agua.
    
    Args:
    -pantalla:Recibe el tamaño de la pantalla del juego
    -tablero_x:Recibe la coordenada x en la que comeinza el tablero
    -tablero_y:Recibe la coordenada y en al que comienza el tablero
    -tam_casillero:Recibe el tamaño de cada casillero
    -margen:Recibe el tamaño del margen entre casillero y casillero
    -matriz:Recibe la matriz que representa el tablero de juego
    -disparos_realizados:Recibe una lista con als coordenadas de los disparos realizados
    -naves_hundidas:Recibe una lista con las coordenadas de las naves hundidas
    -mostrar_naves:Recibe el booleano del modo debug
    -nave_intacta:Recibe el numero que representa una nave intecta en el tablero
    
    Return:Ninguno'''
    # DIBUJAR TABLERO 
    for fila in range(len(matriz)):
        for col in range(len(matriz[0])):
            valor = matriz[fila][col]
            x = tablero_x + col * (tam_casillero + margen)
            y = tablero_y + fila * (tam_casillero + margen)

            if [fila, col] in disparos_realizados: # Celda ya visitada
                if valor == nave_impactada:  # Parte de nave dañada
                    es_hundida = False # flag
                    for nave in naves_hundidas:
                        if [fila, col] in nave: # si esa parte (coordenada) pertenece a la nave hundida
                            es_hundida = True 
                            break
                    if es_hundida:
                        color = colores["rojo"]
                    else:
                        color = colores["naranja"]
                else:                                       
                    color = colores["azul"] # agua impactada
            else:     # Celda sin revelar
                if mostrar_naves and valor == nave_intacta: # si recibe el evento 'D' y la posicion es 1 
                    color = colores["verde"]    
                else:
                    color = colores["celeste"]

            #pinta los casilleros
            pg.draw.rect(pantalla, color, (x, y, tam_casillero, tam_casillero))
            pg.draw.rect(pantalla, colores["negro"], (x, y, tam_casillero, tam_casillero), 1)