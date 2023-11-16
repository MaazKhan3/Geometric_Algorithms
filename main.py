import pygame
import sys
import jarvis as j
import graham as g
import brute as b
#import chan as c

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1366, 768
BUTTON_WIDTH, BUTTON_HEIGHT = 300, 75
PADDING = 20

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Algorithm Menu")

# Fonts
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

def main_menu():
    while True:
        screen.fill(BLACK)
        draw_text("DESIGN AND ANALYSIS OF ALGORITHMS", font, WHITE, 50, 50)

        intersect_button = pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2, 200, BUTTON_WIDTH, BUTTON_HEIGHT)
        convex_button = pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2, 300, BUTTON_WIDTH, BUTTON_HEIGHT)

        pygame.draw.rect(screen, WHITE, intersect_button)
        pygame.draw.rect(screen, WHITE, convex_button)

        
        draw_text("INTERSECTING LINE SEGMENTS", small_font, BLACK, intersect_button.x + 20, intersect_button.y + 30)
        draw_text("CONVEX HULL SOLUTION", small_font, BLACK, convex_button.x + 20, convex_button.y + 30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if intersect_button.collidepoint(event.pos):
                    intersect_menu()
                elif convex_button.collidepoint(event.pos):
                    convex_menu()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    return  # return from main_menu function to exit the loop and go back to the main loop

        pygame.display.update()

def intersect_menu():
    while True:
        screen.fill(BLACK)
        draw_text("Choose Method for Line Segments", font, WHITE, 50, 50)

        method1_button = pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2, 200, BUTTON_WIDTH, BUTTON_HEIGHT)
        method2_button = pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2, 300, BUTTON_WIDTH, BUTTON_HEIGHT)

        pygame.draw.rect(screen, WHITE, method1_button)
        pygame.draw.rect(screen, WHITE, method2_button)

        draw_text("METHOD 1", small_font, BLACK, method1_button.x + 10, method1_button.y + 15)
        draw_text("METHOD 2", small_font, BLACK, method2_button.x + 10, method2_button.y + 15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if method1_button.collidepoint(event.pos):
                    # Implement actions for method 1
                    pass  # Placeholder for now
                elif method2_button.collidepoint(event.pos):
                    # Implement actions for method 2
                    pass  # Placeholder for now

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    return  # return from intersect_menu function to exit the loop and go back to the main_menu loop

        pygame.display.update()

def convex_menu():
    while True:
        screen.fill(BLACK)
        draw_text("Choose Method for Convex Hull", font, WHITE, 50, 50)

        methods = ["BRUTE FORCE", "JARVIS MARCH", "GRAHAM SCAN", "QUICK ELIMINATION", "CHAN'S ALGORITHM"]
        buttons = []

        for i, method in enumerate(methods):
            button = pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2, 150 + (i * (BUTTON_HEIGHT + PADDING)), BUTTON_WIDTH, BUTTON_HEIGHT)
            buttons.append(button)
            pygame.draw.rect(screen, WHITE, button)
            draw_text(method, small_font, BLACK, button.x + 10, button.y + 15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, button in enumerate(buttons):
                    if button.collidepoint(event.pos):
                        # Implement actions for each method
                        if i == 0:
                            screen.fill(BLACK)
                            b.brute_force(screen)
                            pass  # Placeholder for brute force
                        elif i == 1:
                            screen.fill(BLACK)
                            j.jarvis(screen)
                           # pass  # Placeholder for Jarvis March
                        elif i == 2:
                            screen.fill(BLACK)
                            g.graham(screen)
                            #pass  # Placeholder for Graham Scan
                        elif i == 3:
                            pass  # Placeholder for Quick Elimination
                        elif i == 4:
                            screen.fill(BLACK)
                            #c.convexHull(points, len(points), screen)
                            #pass  # Placeholder for Chan Algorithm

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    return  # return from convex_menu function to exit the loop and go back to the main_menu loop

        pygame.display.update()

# Run the main menu
main_menu()