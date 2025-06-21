import pygame as pg
import pygame.mixer as mixer

mixer.init()

def configurar_pantalla():
    pantalla = pg.display.set_mode((800, 600))
    pg.display.set_caption("Batalla Naval - Menu Inicial")
    fondo = pg.image.load("II-Parcial-Programacion-UTN-/Publico/imagenes/03.jpg")
    titulo = pg.image.load("II-Parcial-Programacion-UTN-/Publico/imagenes/05.png")
    titulo = pg.transform.scale(titulo,(800,140))
    fuente = pg.font.SysFont("CASTELLAR", 30)

    colores = {
    "blanco": (255, 255, 255),
    "azul": (0, 102, 204),
    "gris": (200, 200, 200),
    "gris_oscuro": (100, 100, 100),
    "verde": (0, 255, 0),
    "rojo": (255, 0, 0),
    "celeste": (135, 206, 235),
    "negro": (0, 0, 0),
    "transparente": (0, 0, 0, 0)
    }

    return pantalla, fondo, fuente, colores, titulo