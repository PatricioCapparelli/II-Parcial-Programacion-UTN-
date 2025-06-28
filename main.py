import pygame as pg
import pygame.mixer as mixer
from funciones.pantallas.pantalla import *
from funciones.modulos.menu import menu_principal
import pygame.mixer as mixer

pg.init()
mixer.init()

pantalla, fondo, fuente, titulo = configurar_pantalla()

menu_principal(pantalla, fondo, fuente, colores, titulo, botones)

pg.quit()   