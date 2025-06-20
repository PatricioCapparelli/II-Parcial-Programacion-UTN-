import pygame as pg
from funciones.elegir_nivel import pantalla_dificultad
from funciones.modulos.juego import jugar
from funciones.modulos.puntajes import mostrar_puntajes_json
import pygame.mixer as mixer

mixer.init()
# Botones del menu (definidos una sola vez)
botones = {
    "NIVEL": pg.Rect(300, 200, 200, 50),
    "JUGAR": pg.Rect(300, 270, 200, 50),
    "PUNTAJES": pg.Rect(300, 340, 200, 50),
    "MUSICA": pg.Rect(300, 410, 200, 50),
    "SALIR": pg.Rect(300, 480, 200, 50)
}

def dibujar_botones(pantalla, fuente, colores):
    # Usamos la variable global botones directamente
    for texto, rect in botones.items():
        pg.draw.rect(pantalla, colores["CELESTE"], rect)
        pg.draw.rect(pantalla, colores["NEGRO"], rect, 2)
        texto_render = fuente.render(texto, True, colores["NEGRO"])
        pantalla.blit(
            texto_render,
            (rect.x + (rect.width - texto_render.get_width()) // 2,
             rect.y + (rect.height - texto_render.get_height()) // 2)
        )

def menu_principal(pantalla, fondo, fuente, colores, titulo):
    dificultad_seleccionada = None
    nivel = None
    corriendo = True
    musica_pausada = False
    mixer.music.load("Musica_Menu.mp3") #Maquillar la musica
    mixer.music.play()
    mixer.music.set_volume(0.5)
    while corriendo:
        pantalla.blit(fondo, (0, 0))
        pantalla.blit(titulo, (0, 0))
        dibujar_botones(pantalla, fuente, colores)
        for evento in pg.event.get():
            if evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
                for texto, rect in botones.items():
                    if rect.collidepoint(evento.pos):
                        if texto == "SALIR":
                            corriendo = False
                        elif texto == "NIVEL":
                            nivel = pantalla_dificultad(pantalla, fuente, colores)
                            if nivel != None:
                                dificultad_seleccionada = nivel  # guardar el nuevo nivel
                                print("Nivel seleccionado:", dificultad_seleccionada)
                        elif texto == "JUGAR" and dificultad_seleccionada != None:
                            jugar(pantalla, fuente, colores)
                            print("JUGAR")
                        elif texto == "MUSICA":
                            if musica_pausada:
                                mixer.music.unpause()
                                musica_pausada = False
                            else:
                                mixer.music.pause()
                                musica_pausada = True
                        elif texto == "PUNTAJES":
                            mostrar_puntajes_json(pantalla, fuente, colores)
        pg.display.flip()
