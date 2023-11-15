import pygame
import sys

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
pygame.display.set_caption("Convex Hull Visualization")

# Fonts
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

def draw_point(screen,point, color=WHITE):
    pygame.draw.circle(screen, color, point, 5)

def draw_line(start, end):
    pygame.draw.line(screen, WHITE, start, end, 2)

def brute_force_convex_hull(points):
    n = len(points)
    if n < 3:
        return points  # Convex hull not possible with less than 3 points

    hull = []  # Convex hull points

    for i in range(n):
        for j in range(i+1, n):
            valid = True
            for k in range(n):
                if k != i and k != j:
                    if orientation(points[i], points[j], points[k]) == 0:
                        valid = False
                        break

            if valid:
                if points[i] not in hull:
                    hull.append(points[i])
                if points[j] not in hull:
                    hull.append(points[j])

    return hull

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Collinear
    return 1 if val > 0 else 2  # Clockwise or Counterclockwise

def visualize_convex_hull(points):
    convex_hull = brute_force_convex_hull(points)

    while True:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Draw points
        for point in points:
            draw_point(point)

        # Draw convex hull points
        for hull_point in convex_hull:
            draw_point(hull_point, GREEN)

        # Draw convex hull lines
        for i in range(len(convex_hull) - 1):
            draw_line(convex_hull[i], convex_hull[i + 1])

        pygame.display.update()



