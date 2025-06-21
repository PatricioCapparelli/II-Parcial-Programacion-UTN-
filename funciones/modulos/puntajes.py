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
    fondo2 = pg.image.load("publico/02.jpg")
    pantalla.blit(fondo2, (0, 0))

    titulo_render = fuente.render("PUNTAJES", True, colores["NEGRO"])
    pantalla.blit(titulo_render, (300, 50)) 

    archivo = "puntajes.json"
    datos = []
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
    datos_ordenados = sorted(datos, key=lambda x: x["puntaje"], reverse=True)

    y = 120
    for entrada in datos_ordenados[:10]:
        texto = fuente.render(f"{entrada['nick']}: {entrada['puntaje']}", True, colores["NEGRO"])
        pantalla.blit(texto, (250, y))
        y += 40

    boton_volver = pg.Rect(300, y + 40, 200, 50) 
    pg.draw.rect(pantalla, colores["NEGRO"], boton_volver, width=2, border_radius=10)
    texto_volver = fuente.render("VOLVER", True, colores["NEGRO"])
    text_rect = texto_volver.get_rect(center=boton_volver.center) 
    pantalla.blit(texto_volver, text_rect)

    pg.display.flip()

    esperando = True
    while esperando:
        for evento in pg.event.get():
            if evento.type == pg.KEYDOWN and evento.key == pg.K_ESCAPE:
                esperando = False
            elif evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
                if boton_volver.collidepoint(evento.pos):
                    esperando = False

