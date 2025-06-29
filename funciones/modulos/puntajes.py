import pygame as pg
import json
import os
from funciones.recursos.botones import dibujar_botones
from funciones.pantallas.pantalla import *

def guardar_puntaje_json(nick, puntaje):
    archivo = "puntajes.json"
    datos = []
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
    datos.append({"nick": nick, "puntaje": puntaje})
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)

def mostrar_puntajes_json(pantalla, fuente, colores):
    fondo2 = pg.image.load("publico/imagenes/02.jpg")
    pantalla.blit(fondo2, (0, 0))

    titulo_render = fuente.render("PUNTAJES", True, colores["negro"])
    pantalla.blit(titulo_render, (300, 50)) 

    archivo = "puntajes.json"
    datos = []
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
    datos_ordenados = sorted(datos, key=lambda x: x["puntaje"], reverse=True)
    fondo2 = pg.image.load("publico/imagenes/02.jpg")
    pantalla.blit(fondo2, (0, 0))
    titulo = fuente.render("PUNTAJES", True, colores["negro"])
    pantalla.blit(titulo, (300, 50))
    y = 120
    for entrada in datos_ordenados[:3]: #slice
        texto = fuente.render(f"{entrada['nick']}: {entrada['puntaje']}", True, colores["negro"])
        pantalla.blit(texto, (250, y))
        y += 40

    dibujar_botones(pantalla, fuente, colores, botones["VOLVER_DE_PUNTAJES"], "VOLVER")

    pg.display.flip()

    esperando = True
    while esperando:
        for evento in pg.event.get():
            if evento.type == pg.KEYDOWN and evento.key == pg.K_ESCAPE:
                esperando = False
            elif evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
                if botones["VOLVER_DE_PUNTAJES"].collidepoint(evento.pos):
                    esperando = False

