import pygame as pg
import pygame.mixer as mixer

mixer.init()

def configurar_pantalla():
    pantalla = pg.display.set_mode((800, 600))
    pg.display.set_caption("Batalla Naval - Menu Inicial")
    
    fondo = pg.image.load("03.jpg")

    fuente = pg.font.SysFont("CASTELLAR", 30)
    fondo = pg.image.load("batalla-naval.webp")
    fuente = pg.font.SysFont("CASTELLAR", 30)
    
    colores = {
    "BLANCO": (255, 255, 255),
    "AZUL": (0, 102, 204),
    "GRIS": (200, 200, 200),
    "NEGRO": (0, 0, 0),
    "CELESTE":(135,206,235),
    "color_con_alpha": (0, 0, 0, 0)
}

    return pantalla, fondo, fuente, colores
