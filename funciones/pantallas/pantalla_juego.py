# ---------------------------------------------
#  pantalla_juego.py
# ---------------------------------------------
import pygame as pg
from funciones.modulos.verificar_nave_hundida import verificar_nave_hundida

# (Opcional) Constantes para leer mejor el código
AGUA            = 0
NAVE_INTacta    = 1
NAVE_IMPACTADA  = 2
AGUA_ERRADA     = 3


def pantalla_juego(pantalla, fuente, colores, matriz, dificultad):
    margen = 2
    match dificultad:
        case "facil":
            tam_casillero = 30
            tablero_x, tablero_y = 120, 100
        case "medio":
            tam_casillero = 20
            tablero_x, tablero_y = 50, 90
        case "dificil":
            tam_casillero = 10
            tablero_x, tablero_y = 35, 60

    boton_reiniciar = pg.Rect(545, 100, 210, 50)
    boton_volver    = pg.Rect(545, 300, 210, 50)

    naves_hundidas = []
    puntaje = 0
    disparos_realizados = []
    corriendo = True
    resultado = "finalizado"
    juego_terminado = False
    mostrar_naves = False      # Modo debug

    while corriendo:
        pantalla.blit(pg.image.load("publico/imagenes/02.jpg"), (0, 0))

        # DIBUJAR TABLERO 
        for fila in range(len(matriz)):
            for col in range(len(matriz[0])):
                valor = matriz[fila][col]
                x = tablero_x + col * (tam_casillero + margen)
                y = tablero_y + fila * (tam_casillero + margen)

                if [fila, col] in disparos_realizados:          # Celda ya visitada
                    if valor == NAVE_IMPACTADA:                 # Parte de nave dañada
                        es_hundida = False
                        for nave in naves_hundidas:
                            if [fila, col] in nave:
                                es_hundida = True
                                break
                        color = colores["rojo"] if es_hundida else colores["naranja"]
                    else:                                       # Agua o agua errada
                        color = colores["azul"]
                else:                                           # Celda sin revelar
                    if mostrar_naves and valor == NAVE_INTacta: # Mostrar naves (debug)
                        color = colores["verde"]
                    else:
                        color = colores["celeste"]

                pg.draw.rect(pantalla, color, (x, y, tam_casillero, tam_casillero))
                pg.draw.rect(pantalla, colores["negro"],
                            (x, y, tam_casillero, tam_casillero), 1)

        pg.draw.rect(pantalla, colores["celeste"], boton_reiniciar)
        pg.draw.rect(pantalla, colores["negro"],   boton_reiniciar, 2)
        pantalla.blit(fuente.render("REINICIAR", True, colores["negro"]),
                    (boton_reiniciar.x + 20, boton_reiniciar.y + 10))

        pg.draw.rect(pantalla, colores["gris_oscuro"], boton_volver)
        pg.draw.rect(pantalla, colores["negro"],       boton_volver, 2)
        pantalla.blit(fuente.render("VOLVER", True, colores["blanco"]),
                    (boton_volver.x + 20, boton_volver.y + 10))

        pantalla.blit(fuente.render(f"Puntaje:{puntaje:04}",
                                    True, colores["negro"]), (545, 200))

        if mostrar_naves:
            pantalla.blit(fuente.render("MODO DEBUG: ACTIVADO",
                                        True, colores["rojo"]), (545, 250))

        # --------------- ¿TODAS LAS NAVES HUNDIDAS? -----
        if juego_terminado is False:
            if all(NAVE_INTacta not in fila for fila in matriz):
                juego_terminado = True
                mensaje = fuente.render("¡TODAS LAS NAVES HUNDIDAS!",
                                        True, colores["verde"])
                pantalla.blit(mensaje, (pantalla.get_width() // 2
                                        - mensaje.get_width() // 2, 50))

        # --------------- EVENTOS ------------------------
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                corriendo = False

            elif evento.type == pg.KEYDOWN and evento.key == pg.K_d:
                mostrar_naves = not mostrar_naves

            elif evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
                # Botones
                if boton_reiniciar.collidepoint(evento.pos):
                    resultado, corriendo = "reiniciar", False
                    continue
                if boton_volver.collidepoint(evento.pos):
                    resultado, corriendo = "volver", False
                    continue

                # Disparo
                col = (evento.pos[0] - tablero_x) // (tam_casillero + margen)
                fila = (evento.pos[1] - tablero_y) // (tam_casillero + margen)
                if (0 <= fila < len(matriz)
                        and 0 <= col < len(matriz[0])
                        and juego_terminado is False
                        and [fila, col] not in disparos_realizados):

                    disparos_realizados.append([fila, col])

                    if matriz[fila][col] == NAVE_INTacta:        # Impacto
                        matriz[fila][col] = NAVE_IMPACTADA
                        puntaje += 5

                        hundida, partes = verificar_nave_hundida(matriz, fila, col)
                        if hundida:
                            puntaje += 10 * len(partes)
                            naves_hundidas.append(partes)

                    elif matriz[fila][col] == AGUA:              # Agua
                        matriz[fila][col] = AGUA_ERRADA
                        puntaje -= 1

        pg.display.flip()

    return resultado, puntaje
