import pygame
import numpy as np
import point as po

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
        return True

    return False

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

def m2(screen):
    while True:
        screen.fill((0, 0, 0))
        pygame.display.flip()

        line1 = (np.array([100, 100]), np.array([500, 500]))
        line2 = (np.array([100, 500]), np.array([500, 100]))

        # Draw Line 1
        visualizeLines(screen, line1, (255, 255, 255))

        # Draw Line 2
        visualizeLines(screen, line2, (255, 255, 255))

        intersection = findIntersection(line1, line2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    return  # Return from the function to go back to the menu

        if intersection:
            print("Lines intersect.")
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
