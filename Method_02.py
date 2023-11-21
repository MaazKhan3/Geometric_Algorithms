import pygame
import numpy as np

def findIntersection(line1, line2):
    p1, q1 = line1
    p2, q2 = line2

    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0
        elif val > 0:
            return 1
        else:
            return 2

    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        # Calculate the intersection point
        den = (q2[1] - p2[1]) * (q1[0] - p1[0]) - (q2[0] - p2[0]) * (q1[1] - p1[1])
        num1 = (q2[0] - p2[0]) * (p1[1] - p2[1]) - (q2[1] - p2[1]) * (p1[0] - p2[0])
        num2 = (q1[0] - p1[0]) * (p1[1] - p2[1]) - (q1[1] - p1[1]) * (p1[0] - p2[0])

        if den != 0:
            t = num1 / den
            intersection_point = p1 + t * (q1 - p1)
            return intersection_point

    return None

def visualizeLines(screen, line, color):
    # Draw endpoints of Line
    pygame.draw.circle(screen, color, line[0], 5)
    pygame.display.flip()
    pygame.time.delay(500)

    pygame.draw.circle(screen, color, line[1], 5)
    pygame.display.flip()
    pygame.time.delay(500)

    # Draw Line
    pygame.draw.line(screen, color, line[0], line[1], 2)
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
    return (np.array([x1, y1]), np.array([x2, y2]))

def m2(screen):
    screen_width, screen_height = 1366, 768

    while True:
        screen.fill((61, 12, 7))
        pygame.display.flip()

        # Randomize endpoints of Line 1 and Line 2
        line1 = randomize_line(screen_width, screen_height)
        line2 = randomize_line(screen_width, screen_height)

        # Draw Line 1
        visualizeLines(screen, line1, (255, 255, 255))

        # Draw Line 2
        visualizeLines(screen, line2, (255, 255, 255))

        intersection_point = findIntersection(line1, line2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    return  # Return from the function to go back to the menu

        if intersection_point is not None:
            intersection_text = f'Intersection Point: ({int(intersection_point[0])}, {int(intersection_point[1])})'
            print("Lines intersect at:", intersection_point)
            drawText(screen, 'Lines intersect', (50, 50))
            drawText(screen, intersection_text, (50, 80))
        else:
            print("Lines do not intersect.")
            drawText(screen, 'Lines do not intersect', (50, 50))

        pygame.display.flip()
        pygame.time.delay(2000)  # Display result for 2 seconds
        pygame.time.delay(500)  # Delay before next iteration
