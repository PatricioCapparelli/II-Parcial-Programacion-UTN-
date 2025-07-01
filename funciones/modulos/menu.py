import pygame as pg
from funciones.pantallas.pantalla_nivel import pantalla_dificultad
from funciones.modulos.juego import jugar
from funciones.modulos.puntajes import mostrar_puntajes_json
import pygame.mixer as mixer
from funciones.modulos.tablero import *
from funciones.recursos.botones import *
from funciones.modulos.musica import pausar_o_renaudar_musica
from funciones.recursos.aviso import aviso

mixer.init()

def menu_principal(pantalla:tuple, fuente:str, colores:dict, botones:dict)->None:
    '''Se encarga de la interaccion con el menú
    
        Args:
        -pantalla:Recibe el tamaño de la pantalla
        -fuente:Recibe la fuente del texto
        -colores:Recibe el diccionario de los colores
        -botones:Recibe el diccionario de los botones

        Returno:Ninguno
        '''
    titulo = pg.image.load("publico/imagenes/05.png")
    titulo = pg.transform.scale(titulo,(800,140))
    fondo = pg.image.load("publico/imagenes/03.jpg")
    dificultad_seleccionada = None
    nick = None
    corriendo = True
    musica_pausada = False
    mixer.init()
    mixer.music.load("publico/musica/Musica_Menu2.mp3")
    mixer.music.play(-1)
    mixer.music.set_volume(0.5)

    while corriendo:
        pantalla.blit(fondo, (0, 0))
        pantalla.blit(titulo, (0, 0))
        botones_menu_principal(pantalla, fuente, colores, botones)

        for evento in pg.event.get():
            if evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
                for texto, rect in botones.items():
                    if rect.collidepoint(evento.pos):
                        if texto == "SALIR":
                            corriendo = False

                        elif texto == "NIVEL":
                            nivel = pantalla_dificultad(pantalla, fuente, colores, botones)
                            if nivel != "volver" and nivel != None:
                                dificultad_seleccionada = nivel
                                print(f"Nivel seleccionado: {dificultad_seleccionada}")

                        elif texto == "JUGAR":
                            if dificultad_seleccionada:
                                nick = jugar(pantalla, fuente, colores, dificultad_seleccionada, nick)
                            else:
                                aviso(pantalla, fuente, colores, "Elige una dificultad")

                        elif texto == "MUSICA":
                            musica_pausada = pausar_o_renaudar_musica(musica_pausada)

                        elif texto == "PUNTAJES":
                            mostrar_puntajes_json(pantalla, fuente, colores)

        pg.display.flip()
