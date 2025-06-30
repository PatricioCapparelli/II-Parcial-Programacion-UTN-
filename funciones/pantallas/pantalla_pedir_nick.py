import pygame as pg

def pedir_nick(pantalla:tuple, fuente:str, colores:dict):
    '''Esta funcion se encarga de solicitar al jugador que introduzca el nick
    
    Args:
    -pantalla:Recibe el tamaño de la pantalla
    -fuente:Recibe la fuente seleccionada para el texto
    -colores:Recibe el diccionario colores.
    
    Return:Retorna el nick introducido por el jugador'''
    nick = ""
    activo = True
    caja = pg.Rect(50, 150, 500, 40) 
    fondo = pg.image.load("publico/imagenes/02.jpg").convert()

    while activo:
        for evento in pg.event.get():
            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_RETURN and len(nick) > 0:
                    activo = False
                elif evento.key == pg.K_BACKSPACE:
                    nick = nick[:-1]
                elif len(nick) < 10:
                    nick += evento.unicode

        pantalla.blit(fondo, (0, 0))

        texto = fuente.render("Ingresa tu nick y presiona ENTER:", True, colores["negro"])
        pantalla.blit(texto, (50, 100))

        pg.draw.rect(pantalla, colores["blanco"], caja)
        pg.draw.rect(pantalla, colores["negro"], caja, 2)

        texto_nick = fuente.render(nick, True, colores["negro"])
        pantalla.blit(texto_nick, (caja.x + 5, caja.y + 5))

        pg.display.flip()

    return nick
