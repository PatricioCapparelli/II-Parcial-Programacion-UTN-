import pygame as pg

def pedir_nick(pantalla, fondo, fuente, colores):
    nick = ""
    activo = True
    caja = pg.Rect(50, 150, 500, 40) 

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
