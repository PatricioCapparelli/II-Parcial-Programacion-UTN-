import pygame

def press_to_move(teclas, rect):
    if teclas[pygame.K_LEFT]:
        rect.x -= 5
    if teclas[pygame.K_RIGHT]:
        rect.x += 5
    if teclas[pygame.K_UP]:
        rect.y -= 5
    if teclas[pygame.K_DOWN]:
        rect.y += 5
