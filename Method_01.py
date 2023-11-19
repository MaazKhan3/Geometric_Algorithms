import pygame
import point as po
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

def m1(screen):
    while True:
        pygame.display.flip()

        line1 = np.array([[100, 100], [500, 500]])
        line2 = np.array([[100, 500], [500, 100]])

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
                    return  # Return from the function to go back to the menu

        if intersection_point is not None:
            print("Lines intersect at:", intersection_point)
            pygame.font.init()
            font = pygame.font.SysFont(None, 30)
            text = font.render('Lines intersect', True, (255, 255, 255))
            screen.blit(text, (50, 50))
            pygame.display.flip()
        else:
            print("Lines do not intersect.")
            pygame.font.init()
            font = pygame.font.SysFont(None, 30)
            text = font.render('Lines do not intersect', True, (255, 255, 255))
            screen.blit(text, (50, 50))
            pygame.display.flip()

        pygame.time.delay(2000)  # Display result for 2 seconds
        pygame.time.delay(500)  # Delay before next iteration