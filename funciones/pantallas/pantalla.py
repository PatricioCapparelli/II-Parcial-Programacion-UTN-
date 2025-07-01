import pygame as pg
import pygame.mixer as mixer

mixer.init()
# globales
agua = 0
nave_intacta = 1
nave_impactada = 2
agua_impactada = 3

botones = {
    "NIVEL": pg.Rect(300, 200, 200, 50),
    "JUGAR": pg.Rect(300, 270, 200, 50),
    "PUNTAJES": pg.Rect(300, 340, 200, 50),
    "MUSICA": pg.Rect(300, 410, 200, 50),
    "SALIR": pg.Rect(300, 480, 200, 50),
    "REINICIAR": pg.Rect(545, 100, 210, 50),
    "VOLVER": pg.Rect(545, 300, 210, 50),
    "VOLVER_NIVEL": pg.Rect(300, 420, 200, 50),
    "FACIL": pg.Rect(300, 180, 200, 50),
    "MEDIO": pg.Rect(300, 260, 200, 50),
    "DIFICIL": pg.Rect(300, 340, 200, 50),
    "VOLVER A MENU": pg.Rect(440, 520, 350, 50),
    "VOLVER_DE_PUNTAJES": pg.Rect(300, 300, 210, 50)
}

colores = {
    "blanco": (255, 255, 255),
    "azul": (0, 102, 204),
    "gris": (200, 200, 200),
    "gris_oscuro": (100, 100, 100),
    "verde": (0, 255, 0),
    "rojo": (255, 0, 0),
    "celeste": (135, 206, 235),
    "negro": (0, 0, 0),
    "transparente": (0, 0, 0, 0),
    "naranja": (255, 165, 0),
    "verde_militar": (75, 83, 32)
    }

def configurar_pantalla()->tuple[tuple, str]:
    '''Esta funcion se encarga de definir el tamaño de la pantalla y la fuente del texto

    Args:Ninguno

    Return:Retorna la pantalla del juego con su tamaño y la fuente del texto
    '''
    pantalla = pg.display.set_mode((800, 600))
    pg.display.set_caption("Batalla Naval - Menu Inicial")
    fuente = pg.font.SysFont("CASTELLAR", 30)

    return pantalla, fuente