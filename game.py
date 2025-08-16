import pygame
import sys

# Inicializar Pygame
pygame.init()

# Crear ventana (800 x 600 píxeles)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mi primer juego")

# Crear el jugador: un rectángulo rojo (x, y, ancho, alto)
player = pygame.Rect(100, 100, 50, 50)

# Bucle principal del juego
while True:
    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Rellenar la pantalla con blanco
    screen.fill((255, 255, 255))

    # Dibujar el jugador (rojo)
    pygame.draw.rect(screen, (255, 0, 0), player)

    # Actualizar la pantalla
    pygame.display.flip()
