def devolver_dificultad(dificultad) -> int:

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