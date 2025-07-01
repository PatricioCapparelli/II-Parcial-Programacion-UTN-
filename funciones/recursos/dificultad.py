def devolver_dificultad(dificultad:str) -> tuple[int, int, int]:
    '''Esta funcion se encarga de definir el tamaño del tablero a partir de la dificultad seleccionada.
    
    Args:Recibe la dificultad seleccionada por el jugador

    Return: Retorna el tamaño de cada casillero y la posicion en la que se ubica el inicio del tablero dependiendo de la dificultad seleccionada'''

    match dificultad:
        case "facil":
            tam_casillero = 30
            tablero_x = 120
            tablero_y = 100
        case "medio":
            tam_casillero = 20
            tablero_x = 50
            tablero_y = 90
        case "dificil":
            tam_casillero = 10
            tablero_x = 35
            tablero_y = 60

    return tam_casillero, tablero_x, tablero_y