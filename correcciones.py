import pygame
import random

# Inicialización de Pygame
pygame.init()

# Configuraciones de la pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego Arcade")

# Colores
COLOR_FONDO = (0, 0, 0)
COLOR_TEXTO = (255, 255, 255)

# Configuraciones de fuentes
fuente = pygame.font.Font(None, 36)

# Clase del objeto principal
class ObjetoPrincipal(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))  # Color verde
        self.rect = self.image.get_rect(center=(ANCHO // 2, ALTO - 50))
        self.vidas = 3

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if teclas[pygame.K_RIGHT] and self.rect.right < ANCHO:
            self.rect.x += 5

    def disparar(self):
        bala = Bala(self.rect.centerx, self.rect.top)
        balas.add(bala)

# Clase de los objetos independientes (enemigos)
class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 0, 0))  # Color rojo
        self.rect = self.image.get_rect(
            center=(random.randint(20, ANCHO - 20), random.randint(-100, -40))
        )
        self.velocidad = random.randint(2, 5)

    def update(self):
        self.rect.y += self.velocidad
        if self.rect.top > ALTO:
            self.rect.y = random.randint(-100, -40)
            self.rect.x = random.randint(20, ANCHO - 20)

# Clase para las balas
class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 15))
        self.image.fill((255, 255, 0))  # Color amarillo
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.y -= 10
        if self.rect.bottom < 0:
            self.kill()

# Grupos de sprites
todos_los_sprites = pygame.sprite.Group()
enemigos = pygame.sprite.Group()
balas = pygame.sprite.Group()

# Instanciación del objeto principal
jugador = ObjetoPrincipal()
todos_los_sprites.add(jugador)

# Creación de enemigos
for i in range(5):
    enemigo = Enemigo()
    todos_los_sprites.add(enemigo)
    enemigos.add(enemigo)

# Variables del juego
puntaje = 0
juego_activo = True

# Bucle principal del juego
reloj = pygame.time.Clock()
while juego_activo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            juego_activo = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                jugador.disparar()

    # Actualización de los sprites
    todos_los_sprites.update()

    # Detección de colisiones entre balas y enemigos
    colisiones = pygame.sprite.groupcollide(enemigos, balas, True, True)
    for colision in colisiones:
        puntaje += 10
        nuevo_enemigo = Enemigo()
        todos_los_sprites.add(nuevo_enemigo)
        enemigos.add(nuevo_enemigo)

    # Detección de colisiones entre el jugador y los enemigos
    if pygame.sprite.spritecollideany(jugador, enemigos):
        jugador.vidas -= 1
        if jugador.vidas <= 0:
            juego_activo = False

    # Renderizado de la pantalla
    pantalla.fill(COLOR_FONDO)
    todos_los_sprites.draw(pantalla)

    # Mostrar puntaje y vidas
    texto_puntaje = fuente.render(f"Puntaje: {puntaje}", True, COLOR_TEXTO)
    pantalla.blit(texto_puntaje, (10, 10))
    texto_vidas = fuente.render(f"Vidas: {jugador.vidas}", True, COLOR_TEXTO)
    pantalla.blit(texto_vidas, (ANCHO - 120, 10))

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
