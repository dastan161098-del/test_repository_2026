import pygame
import random
from ball import Ball

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

clock = pygame.time.Clock()


stars = []
for _ in range(120):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    stars.append([x, y])

ball = Ball(WIDTH // 2, HEIGHT // 2)

running = True
while running:
    clock.tick(60)

   
    screen.fill((5, 5, 20))

   
    for star in stars:
        pygame.draw.circle(screen, (255, 255, 255), star, 1)
        star[1] += 1  # falling effect

        if star[1] > HEIGHT:
            star[0] = random.randint(0, WIDTH)
            star[1] = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    dx, dy = 0, 0

    if keys[pygame.K_LEFT]:
        dx = -1
    if keys[pygame.K_RIGHT]:
        dx = 1
    if keys[pygame.K_UP]:
        dy = -1
    if keys[pygame.K_DOWN]:
        dy = 1

    ball.move(dx, dy, WIDTH, HEIGHT)

   
    pygame.draw.circle(screen, (160, 80, 255), (int(ball.x), int(ball.y)), ball.radius)

    pygame.display.flip()

pygame.quit()