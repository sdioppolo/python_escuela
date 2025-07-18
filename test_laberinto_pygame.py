import pygame

pygame.init()

ventana = pygame.display.set_mode((800,600))
pygame.display.set_caption("Test PyGame 1")

fondo = pygame.transform.scale(pygame.image.load('laberinto.png').convert(),(800,600))
bola_img = pygame.image.load('ball.png')
bola = bola_img.get_rect()

ventana.blit(fondo, (0,0))
# convertimos el fondo en una superficie para poder leer coordenadas
pxfondo = pygame.display.get_surface()

bola.move_ip(100,100)
ventana.blit(bola_img, bola)

juego = True

while juego:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            juego = False

    tecla = pygame.key.get_pressed()
    if(tecla[pygame.K_UP]):
        # convertimos la superficie del fondo en un vector de pixeles para poder leer los colores
        pxa = pygame.PixelArray(pxfondo)
        # tomamos el color del fondo 
        px = pygame.Color(pxa[bola.x, bola.y-2])
        # y borramos el vector de pixeles
        del pxa
        # comparamos el color de la coordenada con el límite que queremos (BLACK)
        if(px == (0, 255, 255, 255)):
            bola = bola.move(0,-4)
            pygame.display.update()
    if(tecla[pygame.K_DOWN]):
        pxa = pygame.PixelArray(pxfondo)
        px = pygame.Color(pxa[bola.x, bola.y+22])
        del pxa

        if(px == (0, 255, 255, 255)):
            bola = bola.move(0,4)
            pygame.display.update()
    if(tecla[pygame.K_LEFT]):
        pxa = pygame.PixelArray(pxfondo)
        px = pygame.Color(pxa[bola.x-2, bola.y])
        del pxa

        if(px == (0, 255, 255, 255)):
            bola = bola.move(-4,0)
    if(tecla[pygame.K_RIGHT]):
        pxa = pygame.PixelArray(pxfondo)
        px = pygame.Color(pxa[bola.x+22, bola.y])
        del pxa

        if(px == (0, 255, 255, 255)):
            bola = bola.move(4,0)

    #pygame.display.update()
    #ventana.fill((0,0,0))
    ventana.blit(fondo, (0,0))
    ventana.blit(bola_img, bola)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
