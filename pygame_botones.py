import pygame
import random
from pygame.locals import *

FONDO = (32, 30, 32)
BLANCO = (255, 255, 255)
COLOR_TEXTO = (50, 60, 80)

def dibujar_panel():
    panel = pygame.transform.scale(imagen_panel, [560, 420])
    pantalla.blit(panel, [20, 20])

def dibujar_botones(lista_botones):
    for boton in lista_botones:
        if boton['on_click']:
            pantalla.blit(boton['imagen_pressed'], boton['rect'])
        else:
            pantalla.blit(boton['imagen'], boton['rect'])

def main():
    game_over = False
    click = False
    clock = pygame.time.Clock()
    rect_boton_1 = imagen_boton.get_rect()
    botones = []
    rect_boton_1.topleft = [80, 80]
    botones.append(
        {'texto': "Nuevo número", 'imagen': imagen_boton, 'imagen_pressed': imagen_boton_pressed, 'rect': rect_boton_1,
         'on_click': True})
    while not game_over:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_over = True
        pantalla.fill(FONDO)
        dibujar_panel()
        dibujar_botones(botones)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

pygame.init()
dimensiones = [600, 460]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Entrada de texto")
imagen_panel = pygame.image.load("../img/panel.png")
imagen_boton = pygame.image.load("../img/button.png")
imagen_boton_pressed = pygame.image.load("../img/buttonPressed.png")

if __name__ == '__main__':
    main()
