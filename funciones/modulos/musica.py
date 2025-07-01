import pygame.mixer as mixer

def pausar_o_renaudar_musica(musica_pausada:bool) -> bool:
    '''Se encarga de pausar y reanudar la musica.
        Args:
        -musica_pausada:Indica si la musica esta pausada o no.
        
        Return:Retorna el estado de la musica, verdadero si esta pausada o en caso contrario falso.
        '''
    if musica_pausada:
        mixer.music.unpause()
        musica_pausada = False
    else:
        mixer.music.pause()
        musica_pausada = True

    return musica_pausada