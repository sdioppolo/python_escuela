import pygame
from random import randint
pygame.init()
ventana = pygame.display.set_mode((640,480))
pygame.display.set_caption("Ejemplo 4")
ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
# La velocidad se calcular con un valor pseudialeatorio entre 3,6
speed = [randint(3,6),randint(3,6)]
ballrect.move_ip(0,0)
bate = pygame.image.load("bate.png")
baterect = bate.get_rect()
baterect.move_ip(240,450)

bloques = []
'''
pos = int(0)
for i in range(0, 14, 2):
    bloques.append(pygame.image.load("block_r.png"))
    bloques.append(bloques[i].get_rect())
    bloques[i+1].move_ip((80*pos)+30,150)
    pos+=1
'''
p=int(0)
#Rectangulos
bloques.append(pygame.draw.rect(ventana, (255, 115, 179), ( 80, 50, 100, 25)))
bloques.append(bloques[p].get_rect())
p+=1
bloques.append(pygame.draw.rect(ventana, (255, 115, 179), (190, 50, 100, 25)))
bloques.append(bloques[p].get_rect())
p+=1
bloques.append(pygame.draw.rect(ventana, (255, 115, 179), (300, 50, 100, 25)))
bloques.append(bloques[p].get_rect())
p+=1
bloques.append(pygame.draw.rect(ventana, (255, 115, 179), (410, 50, 100, 25)))
bloques.append(bloques[p].get_rect())
p+=1
bloques.append(pygame.draw.rect(ventana, (255, 115, 179), (520, 50, 100, 25)))
bloques.append(bloques[p].get_rect())
p+=1
bloques.append(pygame.draw.rect(ventana, (255, 115, 179), (630, 50, 100, 25)))
bloques.append(bloques[p].get_rect())
p+=1
'''
#Rectangulos 2
rect1_2 = pygame.draw.rect(screen, (142, 0, 0), (135, 85, 100, 25))
rect2_2 = pygame.draw.rect(screen, (142, 0, 0), (245, 85, 100, 25))
rect3_2 = pygame.draw.rect(screen, (142, 0, 0), (355, 85, 100, 25))
rect4_2 = pygame.draw.rect(screen, (142, 0, 0), (465, 85, 100, 25))
rect5_2 = pygame.draw.rect(screen, (142, 0, 0), (575, 85, 100, 25))
#Rectangulos 3
rect1_3 = pygame.draw.rect(screen, (10, 65, 87), (80, 120, 100, 25))
rect2_3 = pygame.draw.rect(screen, (10, 65, 87), (190, 120, 100, 25))
rect3_3 = pygame.draw.rect(screen, (10, 65, 87), (300, 120, 100, 25))
rect4_3 = pygame.draw.rect(screen, (10, 65, 87), (410, 120, 100, 25))
rect5_3 = pygame.draw.rect(screen, (10, 65, 87), (520, 120, 100, 25))
rect6_3 = pygame.draw.rect(screen, (10, 65, 87), (630, 120, 100, 25))
#Rectangulos 4
rect1_4 = pygame.draw.rect(screen, (199, 147, 0), (135, 155, 100, 25))
rect2_4 = pygame.draw.rect(screen, (199, 147, 0), (245, 155, 100, 25))
rect3_4 = pygame.draw.rect(screen, (199, 147, 0), (355, 155, 100, 25))
rect4_4 = pygame.draw.rect(screen, (199, 147, 0), (465, 155, 100, 25))
rect5_4 = pygame.draw.rect(screen, (199, 147, 0), (575, 155, 100, 25))
#Rectangulos 5
rect1_5 = pygame.draw.rect(screen, (0, 228, 179), (80, 190, 100, 25))
rect2_5 = pygame.draw.rect(screen, (0, 228, 179), (190, 190, 100, 25))
rect3_5 = pygame.draw.rect(screen, (0, 228, 179), (300, 190, 100, 25))
rect4_5 = pygame.draw.rect(screen, (0, 228, 179), (410, 190, 100, 25))
rect5_5 = pygame.draw.rect(screen, (0, 228, 179), (520, 190, 100, 25))
rect6_5 = pygame.draw.rect(screen, (0, 228, 179), (630, 190, 100, 25))
'''

# Esta es la fuente que usaremos para el texto que aparecerá en pantalla (tamaño 36)
fuente = pygame.font.Font(None, 36)
# Bucle principal
jugando = True
while jugando:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        baterect = baterect.move(-3,0)
    if keys[pygame.K_RIGHT]:
        baterect = baterect.move(3,0)
    if baterect.colliderect(ballrect):
        speed[1] = -speed[1]
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    '''
    for i in range(1, 14, 2):
        if bloques[i].colliderect(ballrect):
            speed[1] = -speed[1]
            bloques[i].move_ip(1000, 1000)
    '''
    for i in range(len(bloques)):
        if(ballrect.colliderect(bloques[i])):
            speed[1] = -speed[1]
            bloques[i].fill((252, 243, 207))

    if ballrect.top < 0: 
        speed[1] = -speed[1]
    # Si la pelota toca el border inferior, has perdido ("Game Over")
    if ballrect.bottom > ventana.get_height():
        texto = fuente.render("Game Over", True, (125,125,125))
        texto_rect = texto.get_rect()
        texto_x = ventana.get_width() / 2 - texto_rect.width / 2
        texto_y = ventana.get_height() / 2 - texto_rect.height / 2
        ventana.blit(texto, [texto_x, texto_y])
    else:
        ventana.fill((0, 0, 0))
        ventana.blit(ball, ballrect)
        '''
        for i in range(0, 14, 2):
            ventana.blit(bloques[i], bloques[i+1])
        '''
        for i in range(0, len(bloques), 2):
            ventana.blit(bloques[i], bloques[i+1])
        # Dibujo el bate
        ventana.blit(bate, baterect)
    pygame.display.update()
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
