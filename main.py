import pygame as pg
import pygame.mixer as mixer
from funciones.modulos.pantalla import configurar_pantalla
from funciones.modulos.menu import menu_principal

pg.init()
mixer.init()

pantalla, fondo, fuente, colores = configurar_pantalla()

menu_principal(pantalla, fondo, fuente, colores)

pg.quit()
