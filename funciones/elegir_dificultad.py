import pygame as pg
import pygame.mixer as mixer
import sys
import json
import os

# Inicializacion
pg.init()
mixer.init()

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
pantalla = pg.display.set_mode((ANCHO, ALTO))
pg.display.set_caption("Batalla Naval - Menu Inicial")

# Fondo (imagen)
fondo = pg.image.load("01.png")

# Fuente
fuente = pg.font.SysFont("Courier New", 30)

# Colores
BLANCO = (255, 255, 255)
AZUL = (0, 102, 204)
GRIS = (200, 200, 200)
NEGRO = (0, 0, 0)

# Botones del menu principal
botones = {
    "Nivel": pg.Rect(300, 100, 200, 50),
    "Jugar": pg.Rect(300, 180, 200, 50),
    "Ver Puntajes": pg.Rect(280, 260, 250, 50),
    "Salir": pg.Rect(300, 340, 200, 50)
}

def dibujar_botones(): # Dibuja los botones(Nivel, Jugar, Ver Puntaje, Salir) en la pantalla de inicio
    for texto, rect in botones.items(): # Este bucle recorre el diccionario botones que contiene el texto y la posicion/tamaño de cada boton.
        pg.draw.rect(pantalla, AZUL, rect)
        pg.draw.rect(pantalla, NEGRO, rect, 2)
        texto_render = fuente.render(texto, True, BLANCO) # Convierte el texto (por ejemplo "Jugar") en una imagen que se puede mostrar en pantalla.
        pantalla.blit( # blit -> Dibuja (renderiza) el texto sobre el boton
            texto_render,
            (rect.x + (rect.width - texto_render.get_width()) // 2, # calcula cuanto espacio sobra en horizontal
             rect.y + (rect.height - texto_render.get_height()) // 2) # rect → es un pygame.Rect, que indica posicion y tamaño (x, y, ancho, alto)
        )

def pedir_nick():
    nick = ""
    activo = True # Bandera que controla que el bucle siga funcionando hasta que se confirme el nick

    while activo:
        for evento in pg.event.get():
            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_RETURN and len(nick) > 0: #Si se presiona ENTER (K_RETURN) y ya hay texto, se sale del bucle
                    activo = False
                elif evento.key == pg.K_BACKSPACE: #Elimina el ultimo caracter del nick
                    nick = nick[:-1]
                else:
                    if len(nick) < 10: #Si no es ENTER ni borrar, y el nick tiene menos de 10 caracteres, agrega la tecla que se presiono (evento.unicode)
                        nick += evento.unicode 

        pantalla.fill(GRIS) # Pinta toda la pantalla de gris para empezar de cero
        texto = fuente.render("Ingresa tu nick y presiona ENTER:", True, NEGRO) # Dibuja el texto de instrucción en negro.
        pantalla.blit(texto, (50, 100))

        caja = pg.Rect(50, 150, 500, 40) # Dibuja la caja blanca donde aparece lo que se escribe.
        pg.draw.rect(pantalla, BLANCO, caja)
        pg.draw.rect(pantalla, NEGRO, caja, 2)

        texto_nick = fuente.render(nick, True, NEGRO)
        pantalla.blit(texto_nick, (caja.x + 5, caja.y + 5)) #Dibuja lo que el jugador escribio adentro de la caja, con un margen.

        pg.display.flip() # Actualiza la pantalla con todos los cambios.


    return nick # Devuelve el nombre para luego guardarlo en el JSON.

def guardar_puntaje_json(nick, puntaje):
    archivo = "puntajes.json" #ruta donde se guardan los datos
    datos = [] # guarda los puntajes

    if os.path.exists(archivo): #Verifica si el archivo puntajes.json ya existe, para evitar errores
        with open(archivo, "r", encoding="utf-8") as puntajes: #Si el archivo existe, lo abre en modo lectura ("r")
            datos = json.load(puntajes) # Convertir el contenido del archivo (que esta en formato JSON) en una lista de diccionarios.

    datos.append({"nick": nick, "puntaje": puntaje}) #Crea un nuevo diccionario con el nick y puntaje. Lo agrega al final de la lista datos.

    with open(archivo, "w", encoding="utf-8") as f:  #Abrir el archivo en modo escritura
        json.dump(datos, f, indent=4) #Dump para escribir la lista datos en formato JSON, "indent=4" hace que el JSON quede ordenado, con sangria de 4 espacios.

def mostrar_puntajes_json():
    archivo = "puntajes.json"
    datos = []

    # Si el archivo existe, lo abre y carga los datos como una lista de diccionarios
    if os.path.exists(archivo): 
        with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)

    # Ordena los datos por puntaje de mayor a menor
    datos_ordenados = sorted(datos, key=lambda x: x["puntaje"], reverse=True)

    # Limpia la pantalla y muestra el titulo "PUNTAJES"
    pantalla.fill(GRIS)
    titulo = fuente.render("PUNTAJES", True, NEGRO)
    pantalla.blit(titulo, (300, 50))

    # Muestra los primeros 10 puntajes ordenados
    y = 120  # Posicion vertical inicial
    for entrada in datos_ordenados[:10]:
        texto = fuente.render(f"{entrada['nick']}: {entrada['puntaje']}", True, NEGRO)
        pantalla.blit(texto, (250, y))
        y += 40  # Incrementa la posicion para el siguiente puntaje

    # Actualiza la pantalla para mostrar los puntajes
    pg.display.flip()

    # Espera hasta que el usuario presione ESC o cierre la ventana
    esperando = True
    while esperando:
        for evento in pg.event.get():
            if evento.type == pg.QUIT or (evento.type == pg.KEYDOWN and evento.key == pg.K_ESCAPE):
                esperando = False  # Sale del bucle si se presiona ESC o se cierra la ventana

def jugar():
    nick = pedir_nick()
    puntaje = 123  # Esto se reemplaza por logica real del juego
    guardar_puntaje_json(nick, puntaje)

def menu_principal():
    corriendo = True
    while corriendo:
        # Dibuja la imagen de fondo
        pantalla.blit(fondo, (0, 0))
        
        # Dibuja los botones del menu
        dibujar_botones()

        # Captura los eventos del mouse o teclado
        for evento in pg.event.get():
            if evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1: # Detecta clic con boton izquierdo
                for texto, rect in botones.items():
                    if rect.collidepoint(evento.pos):
                        if texto == "Salir": # Cierra el programa si se hace clic en "Salir"
                            pg.quit()
                            sys.exit()
                        elif texto == "Nivel": # Muestra mensaje (puede abrir pantalla de seleccion de nivel)
                            print("Elegir nivel...")
                        elif texto == "Jugar": # Ejecuta la funcion jugar                           
                            jugar()
                        elif texto == "Ver Puntajes": # Muestra la pantalla de puntajes
                            mostrar_puntajes_json()

        # Refresca la pantalla
        pg.display.flip()

menu_principal()
