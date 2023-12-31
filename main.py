import pygame
import sys
import jarvis as j
import graham as g
import brute as b
import chan as c
import quick as q
import monotone as m
import Method_01 as m1
import Method_02 as m2
import Method_03 as m3

pygame.init()

# Constants
WIDTH, HEIGHT = 1366, 768
BUTTON_WIDTH, BUTTON_HEIGHT = 300, 75
PADDING = 20

# Colors
BLACK = (0, 0, 0)
WHITE = (61,12,7)
GRAY = (150, 150, 150)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Algorithm Menu")

# Fonts
font = pygame.font.Font("Blackiron.ttf", 36)
small_font = pygame.font.Font("Blackiron.ttf", 24)

def draw_text(text, font, color, x, y):
    color = (216,0,50)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

def time_complexities_menu():
    while True:
        screen.fill((61, 12, 7))

        draw_text("Time Complexities of Algorithms", font, WHITE, 50, 50)

        algorithms_info = [
            ("Brute Force Convex Hull", "O(n^3)"),
            ("Jarvis March Convex Hull", "O(n^2)"),
            ("Graham Scan Convex Hull", "O(n log n)"),
            ("Quick Hull Convex Hull", "O(n log n)"),
            ("Chan's Algorithm Convex Hull", "O(n log n)"),
            ("Monotone Chain Convex Hull", "O(n log n)"),
            ("All Line Intersection Algorithms", "O(1)"),
            #("Slope-Intercept Line Intersection", "O(1)"),
            #("CCW Order Line Intersection", "O(1)"),
        ]

        buttons = []

        for i, (algorithm, complexity) in enumerate(algorithms_info):
            button = pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2, 150 + (i * (BUTTON_HEIGHT + PADDING)), BUTTON_WIDTH, BUTTON_HEIGHT)
            buttons.append(button)
            pygame.draw.rect(screen, WHITE, button)
            draw_text(f"{algorithm}: {complexity}", small_font, (61, 12, 7), button.x + 10, button.y + 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    return

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, button in enumerate(buttons):
                    if button.collidepoint(event.pos):

                        

                        pygame.display.update()

def main_menu():
    while True:
        screen.fill((61, 12, 7))
        draw_text("DESIGN AND ANALYSIS OF ALGORITHMS", font, WHITE, 450, 60)

        intersect_button = pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2, 200, BUTTON_WIDTH, BUTTON_HEIGHT)
        convex_button = pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2, 300, BUTTON_WIDTH, BUTTON_HEIGHT)
        time_complexities_button = pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2, 400, BUTTON_WIDTH, BUTTON_HEIGHT)

        pygame.draw.rect(screen, WHITE, intersect_button)
        pygame.draw.rect(screen, WHITE, convex_button)
        pygame.draw.rect(screen, WHITE, time_complexities_button)

        draw_text("INTERSECTING LINE SEGMENTS", small_font, BLACK, intersect_button.x + 20, intersect_button.y + 30)
        draw_text("CONVEX HULL SOLUTION", small_font, BLACK, convex_button.x + 20, convex_button.y + 30)
        draw_text("TIME COMPLEXITIES", small_font, BLACK, time_complexities_button.x + 20, time_complexities_button.y + 30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if intersect_button.collidepoint(event.pos):
                    intersect_menu()
                elif convex_button.collidepoint(event.pos):
                    convex_menu()
                elif time_complexities_button.collidepoint(event.pos):
                    time_complexities_menu()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    return  # return from main_menu function to exit the loop and go back to the main loop

        pygame.display.update()

def intersect_menu():
    while True:
        screen.fill((61,12,7))
        draw_text("Choose Method for Line Segments", font, WHITE, 50, 50)

        method1_button = pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2, 200, BUTTON_WIDTH, BUTTON_HEIGHT)
        method2_button = pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2, 300, BUTTON_WIDTH, BUTTON_HEIGHT)
        method3_button = pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2, 400, BUTTON_WIDTH, BUTTON_HEIGHT)

        pygame.draw.rect(screen, WHITE, method1_button)
        pygame.draw.rect(screen, WHITE, method2_button)
        pygame.draw.rect(screen, WHITE, method3_button)

        draw_text("Parametric Intersection", small_font, BLACK, method1_button.x + 10, method1_button.y + 15)
        draw_text("Slope Intercept", small_font, BLACK, method2_button.x + 10, method2_button.y + 15)
        draw_text("CCW Order", small_font, BLACK, method3_button.x + 10, method3_button.y + 15)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if method1_button.collidepoint(event.pos):
                    #screen.fill(BLACK)
                    m1.m1(screen)
                elif method2_button.collidepoint(event.pos):
                    #screen.fill(BLACK)
                    m2.m2(screen)
                elif method3_button.collidepoint(event.pos):
                    #screen.fill(BLACK)
                    m3.m3(screen) 
                    pass  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    return  

        pygame.display.update()

def convex_menu():
    while True:
        screen.fill((61,12,7))
        
        draw_text("Choose Method for Convex Hull", font, WHITE, 50, 50)

        methods = ["BRUTE FORCE", "JARVIS MARCH", "GRAHAM SCAN", "QUICK ELIMINATION", "CHAN'S ALGORITHM","MONOTONE'S ALGORITHM"]
        buttons = []

        for i, method in enumerate(methods):
            button = pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2, 150 + (i * (BUTTON_HEIGHT + PADDING)), BUTTON_WIDTH, BUTTON_HEIGHT)
            buttons.append(button)
            pygame.draw.rect(screen, WHITE, button)
            draw_text(method, small_font, (61,12,7), button.x + 10, button.y + 15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, button in enumerate(buttons):
                    if button.collidepoint(event.pos):
                      
                        if i == 0:
                            screen.fill((61,12,7))
                            b.brute_force(screen)
                            pass  
                        elif i == 1:
                            screen.fill((61,12,7))
                            j.jarvis(screen)
                            pass  
                        elif i == 2:
                            screen.fill((61,12,7))
                            g.graham(screen)
                            pass  
                        elif i == 3:
                            screen.fill((61,12,7))
                            q.quick_hull(screen)
                            pass
                        elif i == 4:
                            screen.fill((61,12,7))
                            c.chan(screen)
                            pass  
                        elif i == 5:
                            screen.fill((61,12,7))
                            m.monotone(screen)
                            pass  

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    return  
        pygame.display.update()

main_menu()