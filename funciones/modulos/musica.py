import pygame.mixer as mixer

def pausar_o_renaudar_musica(musica_pausada:bool) -> bool:
    if musica_pausada:
        mixer.music.unpause()
        musica_pausada = False
    else:
        mixer.music.pause()
        musica_pausada = True

    return musica_pausada

def activar_sonido_disparo(disparo:str):

    mixer.Sound("ruta de sonido (errado, acertado)")
    mixer.Sound("ruta de sonido ()")