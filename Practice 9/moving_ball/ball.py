import pygame

class Ball:
    def __init__(self, x, y, radius=25, speed=20):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed

    def move(self, dx, dy, screen_width, screen_height):
        new_x = self.x + dx * self.speed
        new_y = self.y + dy * self.speed

        # Boundary check (left/right)
        if self.radius <= new_x <= screen_width - self.radius:
            self.x = new_x

        # Boundary check (top/bottom)
        if self.radius <= new_y <= screen_height - self.radius:
            self.y = new_y

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), self.radius)