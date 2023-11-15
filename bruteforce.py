import pygame
import math as m 
import brutealgo as ba


def bruteforce(screen):
    pygame.init()
    print("hello")   
    # Example points (you can replace this with your own set of points)
    sample_points = [
    (100, 100),
    (200, 200),
    (300, 100),
    (200, 50),
    (400, 200),
    (500, 100),
    (600, 300),]

    while true:
        for a in sample_points:
            ba.draw_point(screen,a)


