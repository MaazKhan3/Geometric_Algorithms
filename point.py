import pygame
pygame.init()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (200, 200, 90)
        self.size = 5

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)