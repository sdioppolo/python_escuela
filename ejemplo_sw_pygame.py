''' ---------------------------------------------------------------------------
Código incompleto del disparo
--------------------------------------------------------------------------- '''

import pygame
from random import randint
pygame.init()
ventana = pygame.display.set_mode((800,600))
pygame.display.set_caption("Ejemplo SW")

tie_fighter = []
tie_speed = [2, 0]
p = int(0)

for i in range(0,20,2):
    tie_fighter.append(pygame.image.load("tie_fighter.png"))
    tie_fighter.append(tie_fighter[i].get_rect())
    tie_fighter[i+1].move_ip((30*i)+10, 10)
    p+=2

x_wing_img = pygame.image.load("x_wing.png")
x_wing = x_wing_img.get_rect()
x_wing.move_ip(400, 500)

pipo = pygame.Surface((x_wing.top, x_wing.right))

laser_img = pygame.image.load("laser.png")
laser = laser_img.get_rect()

juego = True
disparo = False

pygame.key.set_repeat(1,25)
fuente = pygame.font.Font(None, 36)

while juego:

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            juego = False

    tecla = pygame.key.get_pressed()
    
    if (tecla[pygame.K_SPACE] and not disparo):
        disparo = True
        laser.top = x_wing.top - 25
        laser.left = x_wing.left + 25

    if (disparo):
        laser.top -= 4
        if (laser.top <= 0):
            disparo = False
    
    if (tecla[pygame.K_ESCAPE]):
        juego = False

    if (tecla[pygame.K_LEFT]):
        x_wing = x_wing.move(-3,0)
    if (tecla[pygame.K_RIGHT]):
        x_wing = x_wing.move(3,0)
    if (tecla[pygame.K_UP]):
        x_wing = x_wing.move(0,-3)
    if (tecla[pygame.K_DOWN]):
        x_wing = x_wing.move(0,3)
    
    if (tie_fighter[1].right >= ventana.get_width()): #and
        #tie_fighter[1].left > 0):
        for i in range(1,20,2):
            tie_speed[1] = -tie_speed[1]
            tie_fighter[i].bottom += 5
            #tie_fighter[i].move(tie_speed,(5,0))
    else:
        if (tie_fighter[1].bottom > ventana.get_height()):
            for i in range(1,20,2):
                tie_speed[1] = -tie_speed[1]
                #tie_fighter[i].bottom += 5
                #tie_fighter[i].right = (30*i) + 10
        else:
            texto = fuente.render("Game Over", True, (125,125,125))
            texto_rect = texto.get_rect()
            texto_x = ventana.get_width() / 2 - texto_rect.width / 2
            texto_y = ventana.get_height() / 2 - texto_rect.height / 2
            ventana.blit(texto, [texto_x, texto_y])
    for i in range(1, 20, 2):
        tie_fighter[i] = tie_fighter[i].move(tie_speed)

    ventana.fill((0,0,0))

    print(x_wing.x, x_wing.y,'-->',pygame.Surface.get_at(x_wing, (x_wing.x, x_wing.y)))
    if(tuple(pygame.Surfaceget_at(x_wing, (x_wing.x, x_wing.y))) == (0,0,0)):
        print('Negro')
        
    #print(x_wing.get_at(x_wing.top+3, x_wing.left-3))

    for i in range(0,20,2):
        ventana.blit(tie_fighter[i], tie_fighter[i+1])

    ventana.blit(x_wing_img, x_wing)
    
    if (disparo):
        ventana.blit(laser_img, laser)
    
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()



