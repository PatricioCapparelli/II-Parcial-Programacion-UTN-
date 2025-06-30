import pygame as pg
import pygame.mixer as mixer
from funciones.modulos.verificar_nave_hundida import verificar_nave_hundida
from funciones.recursos.botones import dibujar_botones
from funciones.pantallas.pantalla_juego_terminado import pantalla_victoria
from funciones.recursos.dificultad import devolver_dificultad
from funciones.recursos.botones import botones_juego
from funciones.modulos.dibujar_tablero import dibujar_tablero
from funciones.pantallas.pantalla import *

mixer.init()

def pantalla_juego(pantalla, fuente, matriz, dificultad):
    
    tam_casillero, tablero_x, tablero_y = devolver_dificultad(dificultad)
    margen = 2
    naves_hundidas = []
    puntaje = 0
    disparos_realizados = []
    corriendo = True
    resultado = "finalizado"
    juego_terminado = False
    mostrar_naves = False      # Modo debug

    while corriendo:
        pantalla.blit(pg.image.load("publico/imagenes/02.jpg"), (0, 0))
        dibujar_tablero(pantalla, tablero_x, tablero_y, tam_casillero, margen, matriz, disparos_realizados, naves_hundidas, mostrar_naves, nave_intacta)
        dibujar_botones(pantalla, fuente, colores, botones["REINICIAR"], "REINICIAR")
        dibujar_botones(pantalla, fuente, colores, botones["VOLVER"], "VOLVER")
        pantalla.blit(fuente.render(f"Puntaje:{puntaje:04}",
                                    True, colores["negro"]), (545, 200))
        pantalla.blit(fuente.render(f"Puntaje:{puntaje:04}",
                                    True, colores["negro"]), (545, 200))

        if mostrar_naves:
            pantalla.blit(fuente.render("MODO DEBUG: ACTIVADO", True, colores["rojo"]), (545, 250))
            
        # TODAS LAS NAVES HUNDIDAS?
        if juego_terminado == False:
            if sum(fila.count(nave_intacta) for fila in matriz) == 0: # suma todas las naves intactas y si da 0, termina el juego
                juego_terminado = True
                mixer.music.load("publico/musica/Musica_victoria.mp3")
                mixer.music.set_volume(0.4)
                mixer.music.play(-1)

        # EVENTOS DEL JUEGO
        for evento in pg.event.get():
            if evento.type == pg.KEYDOWN and evento.key == pg.K_d: # debug 'D'
                if mostrar_naves:
                    mostrar_naves = False
                else:
                    mostrar_naves = True
            elif evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
                # Botones
                resultado, corriendo = botones_juego(pantalla, fuente, colores, botones, evento, resultado, corriendo)
                    # Disparo
                col = (evento.pos[0] - tablero_x) // (tam_casillero + margen) # convierte las el click en una coordenada del tablero en columna
                fila = (evento.pos[1] - tablero_y) // (tam_casillero + margen) # ... en fila

                if (0 <= fila < len(matriz) and 0 <= col < len(matriz[0]) and juego_terminado == False and [fila, col] not in disparos_realizados): # validacion para poder jugar, clickear un casillero valido

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
                            matriz[fila][col] = agua_impactada
                            puntaje -= 1
                            disparo_errado = mixer.Sound("publico/sonidos/agua.mp3")
                            disparo_errado.set_volume(0.4)
                            disparo_errado.play()

        if juego_terminado:
            accion = pantalla_victoria(pantalla, fuente, colores, botones, evento)
            if accion == 1: # VOLVER AL MENU
                resultado = "volver a menu"
                corriendo = False

        pg.display.flip()

    return resultado, puntaje