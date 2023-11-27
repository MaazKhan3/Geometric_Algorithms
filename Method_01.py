import pygame
import numpy as np

def findIntersection(line1, line2):
    x1, y1 = line1[0]
    x2, y2 = line1[1]
    x3, y3 = line2[0]
    x4, y4 = line2[1]

    denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if np.isclose(denominator, 0):
        return None

    intersection_x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denominator
    intersection_y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denominator

    intersection_point = np.array([intersection_x, intersection_y])

    if (
        min(x1, x2) <= intersection_x <= max(x1, x2) and
        min(y1, y2) <= intersection_y <= max(y1, y2) and
        min(x3, x4) <= intersection_x <= max(x3, x4) and
        min(y3, y4) <= intersection_y <= max(y3, y4)
    ):
        return intersection_point
    else:
        return None

def drawLines(screen, line, color):
    pygame.draw.circle(screen, color, line[0], 5)
    pygame.display.flip()
    pygame.time.delay(500)

    pygame.draw.circle(screen, color, line[1], 5)
    pygame.draw.line(screen, color, line[0], line[1], 2)
    pygame.display.flip()
    pygame.time.delay(500)

def drawIntersectionPoint(screen, intersection_point):
    pygame.draw.circle(screen, (255, 0, 0), intersection_point.astype(int), 5)
    pygame.display.flip()
    pygame.time.delay(500)

def drawText(screen, text, position):
    pygame.font.init()
    font = pygame.font.SysFont(None, 30)
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, position)
    pygame.display.flip()

def randomize_line(screen_width, screen_height):
    x1 = np.random.randint(50, screen_width // 2 - 50)
    y1 = np.random.randint(50, screen_height - 50)
    x2 = np.random.randint(screen_width // 2 + 50, screen_width - 50)
    y2 = np.random.randint(50, screen_height - 50)
    return np.array([[x1, y1], [x2, y2]])

def m1(screen):
    screen_width, screen_height = 1366, 768

    while True:
        screen.fill((61, 12, 7))
        pygame.display.flip()

        line1 = randomize_line(screen_width, screen_height)
        line2 = randomize_line(screen_width, screen_height)

        # Draw Line 1
        drawLines(screen, line1, (255, 255, 255))

        # Draw Line 2
        drawLines(screen, line2, (255, 255, 255))

        intersection_point = findIntersection(line1, line2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    return  

        if intersection_point is not None:
            intersection_text = f'Intersection Point: ({int(intersection_point[0])}, {int(intersection_point[1])})'
            print("Lines intersect at:", intersection_point)
            drawText(screen, 'Lines intersect', (50, 50))
            drawText(screen, intersection_text, (50, 80))
            drawIntersectionPoint(screen, intersection_point)
        else:
            print("Lines do not intersect.")
            drawText(screen, 'Lines do not intersect', (50, 50))

        pygame.display.flip()
        pygame.time.delay(2000)  
        pygame.time.delay(500)  
