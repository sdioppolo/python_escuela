import pygame
from random import randint
pygame.init()
ventana = pygame.display.set_mode((640,480))
pygame.display.set_caption("Ejemplo 6")
ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
# La velocidad se calcular con un valor pseudialeatorio entre 3,6
speed = [randint(3,6),randint(3,6)]
ballrect.move_ip(0,0)
bate = pygame.image.load("bate.png")
baterect = bate.get_rect()
baterect.move_ip(240,450)
puntaje=int(0)
bloques = []
pos = int(0)
for i in range(0, 42, 6):
    bloques.append(pygame.image.load("block_r.png"))
    bloques.append(bloques[i].get_rect())
    bloques[i+1].move_ip((80*pos)+30, 100)
    bloques.append(pygame.image.load("block_g.png"))
    bloques.append(bloques[i+2].get_rect())
    bloques[i+3].move_ip((80*pos)+30,130)
    bloques.append(pygame.image.load("block_b.png"))
    bloques.append(bloques[i+4].get_rect())
    bloques[i+5].move_ip((80*pos)+30,160)
    pos+=1

# Esta es la fuente que usaremos para el texto que aparecerá en pantalla (tamaño 36)
fuente = pygame.font.Font(None, 36)
# Bucle principal

score = fuente.render(str(puntaje), True, (125,125,125))
score_rect = score.get_rect()

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

    for i in range(1, len(bloques), 2):
        if bloques[i].colliderect(ballrect):
            speed[1] = -speed[1]
            bloques[i].move_ip(1000, 1000)
            if (i%2 == 0):
                puntaje += 25
            elif (i%3 == 0):
                puntaje += 35
            else:
                puntaje += 15
            score = fuente.render(str(puntaje), True, (125,125,125))
            score_rect = score.get_rect()

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
        ventana.fill((252, 243, 207))
        ventana.blit(score, [ 500, 5])
        ventana.blit(ball, ballrect)
        for i in range(0, len(bloques), 2):
            ventana.blit(bloques[i], bloques[i+1])
        # Dibujo el bate
        ventana.blit(bate, baterect)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
