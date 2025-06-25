import pygame as pg
import pygame.mixer as mixer
from funciones.pantallas.pantalla import configurar_pantalla
from funciones.modulos.menu import menu_principal
import pygame.mixer as mixer

pg.init()
mixer.init()

pantalla, fondo, fuente, colores, titulo = configurar_pantalla()

menu_principal(pantalla, fondo, fuente, colores, titulo)

pg.quit() ## arreglar que no se peguen las naves