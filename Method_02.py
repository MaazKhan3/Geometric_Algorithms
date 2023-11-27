import pygame
import numpy as np

def findIntersectionSlopeIntercept(line1, line2):
    def slope_intercept(line):
        point1, point2 = line
        if point1[0] == point2[0]:
            # Vertical line, slope is undefined
            return None, None
        m = (point2[1] - point1[1]) / (point2[0] - point1[0])
        c = point1[1] - m * point1[0]
        return m, c

    m1, c1 = slope_intercept(line1)
    m2, c2 = slope_intercept(line2)

    if m1 is None and m2 is None:
        # Both lines are vertical, check if they are coincident
        if line1[0][0] == line2[0][0]:
            return True, (line1[0][0], max(min(line1[0][1], line1[1][1]), min(line2[0][1], line2[1][1])))
        else:
            return False, None
    elif m1 is None or m2 is None or m1 != m2:
        # Lines are not parallel, find point of intersection
        if m1 is None:
            x_intersection = line1[0][0]
            y_intersection = m2 * x_intersection + c2
        elif m2 is None:
            x_intersection = line2[0][0]
            y_intersection = m1 * x_intersection + c1
        else:
            x_intersection = (c2 - c1) / (m1 - m2)
            y_intersection = m1 * x_intersection + c1

        # Check if the intersection point is within the line segments
        if (
            min(line1[0][0], line1[1][0]) <= x_intersection <= max(line1[0][0], line1[1][0]) and
            min(line2[0][0], line2[1][0]) <= x_intersection <= max(line2[0][0], line2[1][0]) and
            min(line1[0][1], line1[1][1]) <= y_intersection <= max(line1[0][1], line1[1][1]) and
            min(line2[0][1], line2[1][1]) <= y_intersection <= max(line2[0][1], line2[1][1])
        ):
            return True, (x_intersection, y_intersection)
        else:
            return False, None
    else:
        # Lines are parallel and not coincident
        return False, None

def visualizeLines(screen, line, color):
    pygame.draw.circle(screen, color, line[0], 5)
    pygame.display.flip()
    pygame.time.delay(500)

    pygame.draw.circle(screen, color, line[1], 5)
    pygame.display.flip()
    pygame.time.delay(500)

    pygame.draw.line(screen, color, line[0], line[1], 2)
    pygame.display.flip()
    pygame.time.delay(500)

def m2(screen):
    while True:
        screen.fill((61, 12, 7))
        pygame.display.flip()

        line1 = (np.array([100, 100]), np.array([500, 500]))
        line2 = (np.array([100, 500]), np.array([500, 100]))

        visualizeLines(screen, line1, (255, 255, 255))
        visualizeLines(screen, line2, (255, 255, 255))

        intersect, intersection_point = findIntersectionSlopeIntercept(line1, line2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    return

        if intersect:
            print("Lines intersect at point:", intersection_point)
            pygame.font.init()
            font = pygame.font.SysFont(None, 30)
            text = font.render(f'Lines intersect at {intersection_point}', True, (255, 255, 255))
            screen.blit(text, (50, 50))
            pygame.display.flip()
        else:
            print("Lines do not intersect.")
            pygame.font.init()
            font = pygame.font.SysFont(None, 30)
            text = font.render('Lines do not intersect', True, (255, 255, 255))
            screen.blit(text, (50, 50))
            pygame.display.flip()

        pygame.time.delay(2000)
        pygame.time.delay(500)