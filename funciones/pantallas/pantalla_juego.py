import pygame as pg
from funciones.modulos.verificar_nave_hundida import verificar_nave_hundida

def pantalla_juego(pantalla, fuente, colores, matriz, dificultad):
    # Configuracion de dimensiones
    match dificultad:
        case "facil":
            tam_casillero = 30
            margen = 2
            tablero_x = 50
            tablero_y = 100
        case "medio":
            tam_casillero = 20
            margen = 1
            tablero_x = 30
            tablero_y = 80
        case "dificil":
            tam_casillero = 10
            margen = 1
            tablero_x = 20
            tablero_y = 60

    # Botones
    boton_reiniciar = pg.Rect(550, 100, 210, 50)
    boton_volver = pg.Rect(550, 300, 210, 50)
    
    # Estado del juego
    naves_hundidas = []
    puntaje = 0
    disparos_realizados = []
    corriendo = True
    resultado = "finalizado"
    juego_terminado = False
    mostrar_naves = False  # Modo debug para ver naves

    while corriendo:
        pantalla.fill(colores["gris"])

        # Dibujar tablero
        for fila in range(len(matriz)):
            for col in range(len(matriz[0])):
                valor = matriz[fila][col]
                x = tablero_x + col * (tam_casillero + margen)
                y = tablero_y + fila * (tam_casillero + margen)


                # Determinar color según el estado de la celda
                if [fila, col] in disparos_realizados:
                    if valor == 0:  # Disparo al agua
                        color = colores["azul_oscuro"]
                    elif valor == 2:  # Nave impactada
                        # Verificar si es parte de una nave hundida
                        es_hundida = False
                        for nave in naves_hundidas:
                            if [fila, col] in nave:
                                es_hundida = True
                                break
                        color = colores["rojo"] if es_hundida else colores["naranja"]
                else:  # Celda no revelada
                    if mostrar_naves and valor == 1:  # Mostrar naves en modo debug
                        color = colores["verde"]
                    else:
                        color = colores["celeste"]

                pg.draw.rect(pantalla, color, (x, y, tam_casillero, tam_casillero))
                pg.draw.rect(pantalla, colores["negro"], (x, y, tam_casillero, tam_casillero), 1)

        # Dibujar botones
        pg.draw.rect(pantalla, colores["celeste"], boton_reiniciar)
        pg.draw.rect(pantalla, colores["negro"], boton_reiniciar, 2)
        texto_reiniciar = fuente.render("REINICIAR", True, colores["negro"])
        pantalla.blit(texto_reiniciar, (boton_reiniciar.x + 20, boton_reiniciar.y + 10))

        pg.draw.rect(pantalla, colores["gris_oscuro"], boton_volver)
        pg.draw.rect(pantalla, colores["negro"], boton_volver, 2)
        texto_volver = fuente.render("VOLVER", True, colores["blanco"])
        pantalla.blit(texto_volver, (boton_volver.x + 20, boton_volver.y + 10))

        # Mostrar puntaje
        texto_puntaje = fuente.render(f"Puntaje: {puntaje:04}", True, colores["negro"])
        pantalla.blit(texto_puntaje, (550, 200))

        # Mostrar estado del modo debug
        if mostrar_naves:
            texto_debug = fuente.render("MODO DEBUG: ACTIVADO", True, colores["rojo"])
            pantalla.blit(texto_debug, (550, 250))

        # Verificar si todas las naves han sido hundidas
        if not juego_terminado:
            todas_hundidas = True
            for fila in matriz:
                if 1 in fila:
                    todas_hundidas = False
                    break
            
            if todas_hundidas:
                juego_terminado = True
                mensaje = fuente.render("¡TODAS LAS NAVES HUNDIDAS!", True, colores["verde"])
                pantalla.blit(mensaje, (pantalla.get_width() // 2 - mensaje.get_width() // 2, 50))

        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                corriendo = False

            elif evento.type == pg.KEYDOWN:
                if evento.key == pg.K_d:  # Presionar 'D' para alternar modo debug
                    mostrar_naves = not mostrar_naves

            elif evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
                mouse_x, mouse_y = evento.pos

                if boton_reiniciar.collidepoint(evento.pos):
                    resultado = "reiniciar"
                    corriendo = False

                elif boton_volver.collidepoint(evento.pos):
                    resultado = "volver"
                    corriendo = False

                # Verificar disparo en el tablero
                col = (mouse_x - tablero_x) // (tam_casillero + margen)
                fila = (mouse_y - tablero_y) // (tam_casillero + margen)

                if 0 <= fila < len(matriz) and (0 <= col < len(matriz[0])) and not juego_terminado:
                    if [fila, col] not in disparos_realizados:
                        disparos_realizados.append([fila, col])

                        if matriz[fila][col] == 1:  # Impacto en nave
                            matriz[fila][col] = 2  # Marcar como impactado
                            puntaje += 5  # Sumar 5 puntos por impacto
                            
                            # Verificar si se hundió una nave completa
                            nave_hundida, partes_hundidas = verificar_nave_hundida(matriz, fila, col)

                            if nave_hundida and len(partes_hundidas) <= 4:
                                puntaje += 10 * len(partes_hundidas)
                                naves_hundidas.append(partes_hundidas)
                            
                        elif matriz[fila][col] == 0:  # Disparo al agua
                            matriz[fila][col] = 3
                            puntaje -= 1  # Penalización por disparo fallado

        pg.display.flip()

    return resultado, puntaje


