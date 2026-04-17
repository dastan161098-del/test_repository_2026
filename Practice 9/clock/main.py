# main.py
import pygame
from clock import Clock

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hinata Clock")

bg = pygame.image.load("clock/images/hinata_bg.png").convert()
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

clock = pygame.time.Clock()
clock_logic = Clock(screen, (WIDTH // 2, HEIGHT // 2))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg, (0, 0))
    clock_logic.draw()

    pygame.display.update()
    clock.tick(60)

pygame.quit()