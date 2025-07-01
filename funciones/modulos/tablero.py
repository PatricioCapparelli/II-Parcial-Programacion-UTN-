import random
from funciones.recursos.inicializar_matriz import inicializar_matriz

longitud_submarino = 1
longitud_destructor = 2
longitud_crucero = 3
longitud_acorazado = 4

def celda_valida(matriz:list, fila:int, columna:int)->bool:
    """Indica si el casillero seleccionado y sus 8 vecinos estan vacios.
    
    Args:
    -matriz:Recibe la matriz del tablero
    -fila:Recibe la coordenada x del casillero seleccionado
    -columna:Recibe la coordenada y del casillero seleccionado
    
    Return:Retorna un booleano dependiendo de si al celda es valida para colocar un barco o no
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    es_valido = True

    for i in range(fila - 1, fila + 2):
        for j in range(columna - 1, columna + 2):
            if 0 <= i < filas and 0 <= j < columnas and matriz[i][j] != 0: #para que no tenga ninguna celda vecina como barco
                es_valido = False
    return es_valido

def colocar_naves(matriz:list, cantidad:int, tamaño:int) -> None:
    """Coloca 'cantidad' barcos de 'tamaño' sin superponerse ni tocarse.
    
    Args:
    -matriz:Recibe la amtriz que representa el tablero del juego
    -cantidad:Recibe la cantidad de barcos que debe colocar 
    -tamaño:Recibe el tamañod de los barcos que debe colocar en el tablero
    
    Return:Ninguno"""
    filas = len(matriz)
    columnas = len(matriz[0])
    colocadas = 0

    while colocadas < cantidad:
        horiz = random.choice([True, False]) # al azar elige en que orientacion colocolar la nave (h/v)

        if horiz:                              # Horizontal
            fila = random.randint(0, filas - 1)
            columna = random.randint(0, columnas - tamaño)
            libre = all(celda_valida(matriz, fila, columna + i) for i in range(tamaño))
            if libre:
                for i in range(tamaño):
                    matriz[fila][columna + i] = 1
                colocadas += 1
        else:                                  # Vertical
            fila = random.randint(0, filas - tamaño)
            columna = random.randint(0, columnas - 1)
            libre = all(celda_valida(matriz, fila + i, columna) for i in range(tamaño))
            if libre:
                for i in range(tamaño):
                    matriz[fila + i][columna] = 1
                colocadas += 1

def crear_tablero_inicial(nivel: str) -> list:
    """Crea un tablero con las naves colocadas segun el nivel.
        Args:
        -nivel: Recibe el nivel seleccionado por el jugador

        Return: Retorna una matriz que representa el tablero dependiendo  del nivel seleccionado"""
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

    matriz = inicializar_matriz(filas, columnas, 0)
    colocar_naves(matriz, submarinos, longitud_submarino)
    colocar_naves(matriz, destructores, longitud_destructor)
    colocar_naves(matriz, cruceros, longitud_crucero)
    colocar_naves(matriz, acorazados, longitud_acorazado)

    return matriz

