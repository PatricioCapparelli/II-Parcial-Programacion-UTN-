import pygame as pg

def configurar_pantalla():
    # Inicializa pygame y mixer aqui o asume que ya estan inicializados en main
    pantalla = pg.display.set_mode((800, 600))
    pg.display.set_caption("Batalla Naval - Menu Inicial")
    
    fondo = pg.image.load("01.png")
    fuente = pg.font.SysFont("Courier New", 30)
    
    colores = {
    "BLANCO": (255, 255, 255),
    "AZUL": (0, 102, 204),
    "GRIS": (200, 200, 200),
    "NEGRO": (0, 0, 0)
}

    
    return pantalla, fondo, fuente, colores
