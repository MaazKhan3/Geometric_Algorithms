import pygame
pygame.init()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (247, 140, 162)
        self.size = 6

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)