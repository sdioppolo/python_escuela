import pygame

pygame.init()

ventana = pygame.display.set_mode((640,480))
pygame.display.set_caption("Ejemplo 1")

pacman = pygame.image.load("pacman_1.png")
pacrec = pacman.get_rect()

pacrec.move_ip(320-40, 240-40)
speed = [1, 1]

jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    tecla = pygame.key.get_pressed()
    if(tecla[pygame.K_a]):
        pacrec=pacrec.move(-2, 0)
    if(tecla[pygame.K_d]):
        pacrec=pacrec.move(2, 0)
    if(tecla[pygame.K_s]):
        pacrec=pacrec.move(0, -2)
    if(tecla[pygame.K_w]):
        pacrec=pacrec.move(0, 2)
        
    ventana.fill(( 0, 0, 0 ))
    ventana.blit(pacman, pacrec)
    pacrec.move(speed)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()
