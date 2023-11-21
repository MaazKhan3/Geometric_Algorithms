import pygame
import numpy as np

def ccw(A, B, C):
    return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])

def doIntersect(line1, line2):
    A, B = line1
    C, D = line2

    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)

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

def m3(screen):
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

        intersection = doIntersect(line1, line2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    return  # Return from the function to go back to the menu

        if intersection:
            intersection_point = line1[0] + (line1[1] - line1[0]) * np.random.rand()
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
