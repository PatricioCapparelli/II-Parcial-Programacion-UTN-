import random
from funciones.inicializar_matriz import inicializar_matriz

def colocar_naves(matriz: list, cantidad: int, tamaño: int) -> None:
    """Coloca las naves en la matriz sin superposicion."""
    filas = len(matriz)
    columnas = len(matriz[0])
    colocadas = 0

    while colocadas < cantidad:
        orientacion = random.choice(['H', 'V'])

        if orientacion == 'H':
            fila = random.randint(0, filas - 1) # 0 a 9
            col = random.randint(0, columnas - tamaño) 
            libre = True
            i = 0
            while i < tamaño:
                if matriz[fila][col + i] != 0: # verifica si esta libre la posicion
                    libre = False
                i += 1
            if libre: # si esta libre la posicion, pone el barco
                j = 0
                while j < tamaño:
                    matriz[fila][col + j] = 1
                    j += 1
                colocadas += 1

        else:  # Vertical
            fila = random.randint(0, filas - tamaño)
            col = random.randint(0, columnas - 1)
            libre = True
            i = 0
            while i < tamaño:
                if matriz[fila + i][col] != 0:
                    libre = False
                i += 1
            if libre:
                j = 0
                while j < tamaño:
                    matriz[fila + j][col] = 1
                    j += 1
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
        crear_tablero_inicial(input("Ingrese un nivel valido:"))

    matriz = inicializar_matriz(filas, columnas, 0)

    colocar_naves(matriz, submarinos, 1)
    colocar_naves(matriz, destructores, 2)
    colocar_naves(matriz, cruceros, 3)
    colocar_naves(matriz, acorazados, 4)

    return matriz