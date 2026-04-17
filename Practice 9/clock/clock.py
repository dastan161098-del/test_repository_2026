# clock.py
import pygame
import math
from datetime import datetime

class Clock:
    def __init__(self, screen, center):
        self.screen = screen
        self.center = center

    def get_angles(self):
        now = datetime.now()

        hour = now.hour % 12
        minute = now.minute
        second = now.second

        hour_angle = math.radians(hour * 30 + minute * 0.5)
        minute_angle = math.radians(minute * 6)
        second_angle = math.radians(second * 6)

        return hour_angle, minute_angle, second_angle

    def draw_hand(self, angle, length, width, color):
        angle -= math.pi / 2

        x = self.center[0] + length * math.cos(angle)
        y = self.center[1] + length * math.sin(angle)

        pygame.draw.line(self.screen, color, self.center, (x, y), width)
        pygame.draw.circle(self.screen, color, (int(x), int(y)), width)

    def draw(self):
        hour_a, min_a, sec_a = self.get_angles()

        self.draw_hand(hour_a, 80, 6, (120, 0, 200))
        self.draw_hand(min_a, 120, 4, (180, 80, 255))
        self.draw_hand(sec_a, 140, 2, (255, 100, 200))