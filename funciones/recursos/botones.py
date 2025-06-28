import pygame as pg

def dibujar_botones(pantalla, fuente, colores, rect, texto, color_relleno="celeste", color_fuente="negro"):
    pg.draw.rect(pantalla, colores[color_relleno], rect)
    pg.draw.rect(pantalla, colores["negro"], rect, 2)
    texto_render = fuente.render(texto, True, colores[color_fuente])
    pantalla.blit(
        texto_render,
        (rect.x + (rect.width - texto_render.get_width()) // 2,
            rect.y + (rect.height - texto_render.get_height()) // 2)
    )

def botones_menu_principal(pantalla, fuente, colores, botones):
    for indice,(texto, rect) in enumerate(botones.items()):
        if indice >= 5:
            break\
        
        dibujar_botones(pantalla, fuente, colores, rect, texto)
    