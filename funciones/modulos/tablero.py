import random
from funciones.recursos.inicializar_matriz import inicializar_matriz
import pygame as pg

longitud_submarino = 1
longitud_destructor = 2
longitud_crucero = 3
longitud_acorazado = 4

def celda_valida(matriz, f, c):
    """Devuelve True si (f,c) y sus 8 vecinos están vacíos (0)."""
    filas, columnas = len(matriz), len(matriz[0])
    for i in range(f-1, f+2):
        for j in range(c-1, c+2):
            if 0 <= i < filas and 0 <= j < columnas and matriz[i][j] != 0:
                return False
    return True


def colocar_naves(matriz, cantidad, tamaño):
    """Coloca `cantidad` barcos de `tamaño` sin superponerse ni tocarse."""
    filas, columnas = len(matriz), len(matriz[0])
    colocadas = 0

    while colocadas < cantidad:
        horiz = random.choice([True, False])

        if horiz:                              # Horizontal
            f = random.randint(0, filas - 1)
            c = random.randint(0, columnas - tamaño)
            libre = all(celda_valida(matriz, f, c+i) for i in range(tamaño))
            if libre:
                for i in range(tamaño):
                    matriz[f][c+i] = 1
                colocadas += 1
        else:                                  # Vertical
            f = random.randint(0, filas - tamaño)
            c = random.randint(0, columnas - 1)
            libre = all(celda_valida(matriz, f+i, c) for i in range(tamaño))
            if libre:
                for i in range(tamaño):
                    matriz[f+i][c] = 1
                colocadas += 1

def crear_tablero_inicial(nivel: str) -> list:
    """Crea un tablero con las naves colocadas segun el nivel."""
    if nivel == "facil":
        filas = 10
        columnas = 10
        submarinos = 4
        destructores = 3
        cruceros = 2
        acorazados = 1
    elif nivel == "medio":
        filas = 20
        columnas = 20
        submarinos = 8
        destructores = 6
        cruceros = 4
        acorazados = 2
    elif nivel == "dificil":
        filas = 40
        columnas = 40
        submarinos = 12
        destructores = 9
        cruceros = 6
        acorazados = 3
    else:
        print("nivel invalido")
        crear_tablero_inicial()

    matriz = inicializar_matriz(filas, columnas, 0)

    colocar_naves(matriz, submarinos, longitud_submarino)
    colocar_naves(matriz, destructores, longitud_destructor)
    colocar_naves(matriz, cruceros, longitud_crucero)
    colocar_naves(matriz, acorazados, longitud_acorazado)

    return matriz

