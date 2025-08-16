import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mi primer juego con movimiento")

# Jugador: rectángulo rojo
player = pygame.Rect(100, 100, 50, 50)
speed = 5

# Reloj para limitar FPS
clock = pygame.time.Clock()

# Bucle principal del juego
while True:
    # Limitar a 60 FPS
    clock.tick(60)

    # Eventos (cerrar ventana)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Detectar teclas presionadas
    keys = pygame.key.get_pressed()

    # Movimiento del jugador
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed

    # Evitar que se salga de los bordes
    player.x = max(0, min(player.x, WIDTH - player.width))
    player.y = max(0, min(player.y, HEIGHT - player.height))

    # Dibujar
    screen.fill((255, 255, 255))  # Fondo blanco
    pygame.draw.rect(screen, (255, 0, 0), player)  # Jugador rojo
    pygame.display.flip()  # Actualizar pantalla
