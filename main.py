import pygame as pg
import pygame.mixer as mixer
from funciones.pantallas.pantalla import *
from funciones.modulos.menu import menu_principal
import pygame.mixer as mixer

pg.init()
mixer.init()

pantalla, fuente = configurar_pantalla()

menu_principal(pantalla, fuente, colores, botones)

pg.quit()
