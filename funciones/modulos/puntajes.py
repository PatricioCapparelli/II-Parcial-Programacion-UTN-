import pygame as pg
import json
import os

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
    archivo = "puntajes.json"
    datos = []
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
    datos_ordenados = sorted(datos, key=lambda x: x["puntaje"], reverse=True)
    pantalla.fill(colores["GRIS"])
    titulo = fuente.render("PUNTAJES", True, colores["NEGRO"])
    pantalla.blit(titulo, (300, 50))
    y = 120
    for entrada in datos_ordenados[:10]:
        texto = fuente.render(f"{entrada['nick']}: {entrada['puntaje']}", True, colores["NEGRO"])
        pantalla.blit(texto, (250, y))
        y += 40
    pg.display.flip()
    esperando = True
    while esperando:
        for evento in pg.event.get():
            if evento.type == pg.QUIT or (evento.type == pg.KEYDOWN and evento.key == pg.K_ESCAPE):
                esperando = False
