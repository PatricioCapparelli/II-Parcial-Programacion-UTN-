import pygame as pg
from funciones.modulos.verificar_nave_hundida import verificar_nave_hundida
from funciones.recursos.botones import dibujar_botones
import pygame.mixer as mixer
mixer.init()

agua = 0
nave_intacta = 1
nave_impactada = 2
agua_errada = 3

def pantalla_juego(pantalla, fuente, colores, matriz, dificultad, botones):
    
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
            
    margen = 2
    naves_hundidas = []
    puntaje = 0
    disparos_realizados = []
    corriendo = True
    resultado = "finalizado"
    juego_terminado = False
    mostrar_naves = False      # Modo debug
    musica_victoria_iniciada = False
    fondo_victoria_cargado = False

    
    while corriendo:
        pantalla.blit(pg.image.load("publico/imagenes/02.jpg"), (0, 0))

        # DIBUJAR TABLERO 
        for fila in range(len(matriz)):
            for col in range(len(matriz[0])):
                valor = matriz[fila][col]
                x = tablero_x + col * (tam_casillero + margen)
                y = tablero_y + fila * (tam_casillero + margen)

                if [fila, col] in disparos_realizados:          # Celda ya visitada
                    if valor == nave_impactada:                 # Parte de nave dañada
                        es_hundida = False
                        for nave in naves_hundidas:
                            if [fila, col] in nave:
                                es_hundida = True
                                break
                        color = colores["rojo"] if es_hundida else colores["naranja"]
                    else:                                       
                        color = colores["azul"] # Agua o agua errada
                else:        # Celda sin revelar
                    if mostrar_naves and valor == nave_intacta: # Mostrar naves (debug)
                        color = colores["verde"]
                    else:
                        color = colores["celeste"]

                pg.draw.rect(pantalla, color, (x, y, tam_casillero, tam_casillero))
                pg.draw.rect(pantalla, colores["negro"],
                            (x, y, tam_casillero, tam_casillero), 1)

        dibujar_botones(pantalla, fuente, colores, botones["REINICIAR"], "REINICIAR")
        dibujar_botones(pantalla, fuente, colores, botones["VOLVER"], "VOLVER")

        pantalla.blit(fuente.render(f"Puntaje:{puntaje:04}",
                                    True, colores["negro"]), (545, 200))
        
        pantalla.blit(fuente.render(f"Puntaje:{puntaje:04}",
                                    True, colores["negro"]), (545, 200))

        if mostrar_naves:
            pantalla.blit(fuente.render("MODO DEBUG: ACTIVADO",
                                        True, colores["rojo"]), (545, 250))
            
        #print(sum(fila.count(nave_intacta) for fila in matriz))

        # TODAS LAS NAVES HUNDIDAS?
        if juego_terminado == False:
            if sum(fila.count(nave_intacta) for fila in matriz) == 0:
                juego_terminado = True

        # EVENTOS
        for evento in pg.event.get():
            if evento.type == pg.KEYDOWN and evento.key == pg.K_d:
                mostrar_naves = not mostrar_naves

            elif evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
                # Botones
                for texto, rect in botones.items(): # TEXTO == KEY // RECT == VALUE
                    if rect.collidepoint(evento.pos):
                        if texto == "REINICIAR":
                            resultado  = "reiniciar"
                            corriendo = False
                        elif texto == "VOLVER":
                            resultado  = "volver"
                            corriendo = False

                    # Disparo
                    col = (evento.pos[0] - tablero_x) // (tam_casillero + margen)
                    fila = (evento.pos[1] - tablero_y) // (tam_casillero + margen)
                    if (0 <= fila < len(matriz)
                            and 0 <= col < len(matriz[0])
                            and juego_terminado == False
                            and [fila, col] not in disparos_realizados):

                        disparos_realizados.append([fila, col])

                        if matriz[fila][col] == nave_intacta:        # Impacto
                            matriz[fila][col] = nave_impactada
                            puntaje += 5
                            disparo_acertado = mixer.Sound("publico/sonidos/explosion.mp3")
                            disparo_acertado.set_volume(0.2)
                            disparo_acertado.play()

                            hundida, partes = verificar_nave_hundida(matriz, fila, col)
                            if hundida:
                                puntaje += 10 * len(partes)
                                naves_hundidas.append(partes)

                        elif matriz[fila][col] == agua:              # Agua 3
                            matriz[fila][col] = agua_errada
                            puntaje -= 1
                            disparo_errado = mixer.Sound("publico/sonidos/agua.mp3")
                            disparo_errado.set_volume(0.4)
                            disparo_errado.play()

        if juego_terminado == True:
            if fondo_victoria_cargado == False:
                fondo = pg.image.load("publico/imagenes/batalla-ganada.webp")
                fondo_escalado = pg.transform.scale(fondo, (800, 600))
                fondo_victoria_cargado = True

            if musica_victoria_iniciada == False:
                mixer.music.load("publico/musica/Musica_victoria.mp3")
                mixer.music.play(-1)
                mixer.music.set_volume(0.5)
                musica_victoria_iniciada = True

            pantalla.fill(colores["negro"])
            pantalla.blit(fondo_escalado, (0, 0))
            dibujar_botones(
                pantalla, fuente, colores,
                botones["VOLVER A MENU"], "VOLVER A MENU",
                color_relleno="verde_militar", color_fuente="blanco"
            )

            if evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
                if botones["VOLVER A MENU"].collidepoint(evento.pos):
                    mixer.music.stop()
                    resultado = "volver a menu"
                    corriendo = False
                    musica_victoria_iniciada = False
                    fondo_victoria_cargado = False

        pg.display.flip()

    return resultado, puntaje