import pygame as pg

tam_casillero = 30
margen = 2
tablero_x = 50
tablero_y = 100
boton_reiniciar = pg.Rect(550, 100, 210, 50)
#boton_salir = pg.Rect(550, 300, 210, 50)

def pantalla_juego(pantalla, fuente, colores, matriz):
    puntaje = 0
    disparos_realizados = set()
    corriendo = True
    resultado = "finalizado"  # valor por defecto
    while corriendo:
        pantalla.fill(colores["gris"])

        # dibujar tablero
        for fila in range(len(matriz)):
            for col in range(len(matriz[0])):
                valor = matriz[fila][col]
                x = tablero_x + col * (tam_casillero + margen)
                y = tablero_y + fila * (tam_casillero + margen)

                if valor == 0:
                    color = colores["azul"]
                elif valor == 1:
                    color = colores["gris_oscuro"]
                elif valor == 2:
                    color = colores["verde"]  # disparo acertado
                elif valor == 3:
                    color = colores["rojo"]   # disparo errado
                pg.draw.rect(pantalla, color, (x, y, tam_casillero, tam_casillero))

        #reiniciar
        pg.draw.rect(pantalla, colores["celeste"], boton_reiniciar)
        pg.draw.rect(pantalla, colores["negro"], boton_reiniciar, 2)
        texto_reiniciar = fuente.render("reiniciar", True, colores["negro"])
        pantalla.blit(
            texto_reiniciar,
            (boton_reiniciar.x + 20, boton_reiniciar.y + 10)
        )
        #Salir
        boton_volver = pg.Rect(550, 300, 210, 50) 
        pg.draw.rect(pantalla, colores["negro"], boton_volver, width=2, border_radius=10)
        texto_volver = fuente.render("VOLVER", True, colores["negro"])
        text_rect = texto_volver.get_rect(center=boton_volver.center) 
        pantalla.blit(texto_volver, text_rect)


        # Puntaje
        texto_puntaje = fuente.render(f"puntaje: {puntaje:04}", True, colores["negro"])
        pantalla.blit(texto_puntaje, (550, 200))

        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                corriendo = False
            elif evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
                mouse_x, mouse_y = evento.pos

                if boton_reiniciar.collidepoint(evento.pos):
                    resultado = "reiniciar"
                    corriendo = False

                # calcular posicion clickeada
                col = (mouse_x - tablero_x) // (tam_casillero + margen)
                fila = (mouse_y - tablero_y) // (tam_casillero + margen)

                if 0 <= fila < len(matriz) and 0 <= col < len(matriz[0]):
                    if (fila, col) not in disparos_realizados:
                        disparos_realizados.add((fila, col))
                        if matriz[fila][col] == 1:
                            matriz[fila][col] = 2
                            puntaje += 5
                        elif matriz[fila][col] == 0:
                            matriz[fila][col] = 3
                            puntaje -= 1
        pg.display.flip()

    return resultado, puntaje
