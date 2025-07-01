import pygame as pg

def dibujar_botones(pantalla, fuente, colores, rect, texto, color_relleno="celeste", color_fuente="negro"):
    '''Esta funcion se encarga de dibujar los botones del juego.
    
    Args:
    -pantalla:Recibe el tamañod e la pantalla del juego
    -fuente:Recibe la fuente del texto
    -colores:Recibe el diccionario de colores
    -rect:Recibe el tamaño que va a tener el boton
    -texto:Recibe el texto que va a msotrar el boton
    -color_relleno:Recibe el color de relleno del boton, prestableciendo el color celeste
    -color_fuente:Recibe el color de la fuente del texto, prestableciendo el color negro
    
    Return:Ninguno'''
    pg.draw.rect(pantalla, colores[color_relleno], rect)
    pg.draw.rect(pantalla, colores["negro"], rect, 2)
    texto_render = fuente.render(texto, True, colores[color_fuente])
    pantalla.blit(
        texto_render,
        (rect.x + (rect.width - texto_render.get_width()) // 2,
            rect.y + (rect.height - texto_render.get_height()) // 2)
    )

def botones_menu_principal(pantalla, fuente, colores, botones):
    '''Esta funcion se encarga de dibujar todos los botones del menu principal
    
    Args:
    -pantalla:Recibe el tamaño de la pantalla del juego
    -fuente:Recibe la fuente del texto
    -colores:Recibe el diccionario de colores
    -botones:Recibe el diccionario de botones
    
    Return:Ninguno'''
    for indice,(texto, rect) in enumerate(botones.items()):
        if indice >= 5:
            break   
        dibujar_botones(pantalla, fuente, colores, rect, texto)

def botones_juego(pantalla, fuente, colores, botones, evento, resultado, corriendo):
    '''Esta funcion se encarga de mostrar los botones de la partida
    
    Args:
    -pantalla:Recibe el tamaño de la pantalla del juego
    -fuente:Recibe la fuente del texto
    -colores:Recibe el diccionario de colores
    -botones:Recibe el diccionario de botones
    -evento:Recibe el evento de pygame
    -resultado:Recibe el estado del ultimo boton apretado
    -corriendo:Recibe el estado del la partida para cambiarlo dependiendo del boton

    Return:Retorna el boton soleccioando y el estado de la partida, en el caso de salir o reiniciar.
    '''
    for indice,(texto, rect) in enumerate(botones.items()):
            if indice == 5 or indice == 6:
                dibujar_botones(pantalla, fuente, colores, rect, texto)
            if rect.collidepoint(evento.pos):
                if texto == "REINICIAR":
                    resultado  = "reiniciar"
                    corriendo = False
                elif texto == "VOLVER":
                    resultado  = "volver"
                    corriendo = False

    return resultado, corriendo