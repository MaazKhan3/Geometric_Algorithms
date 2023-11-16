import pygame
import random
import point as po

class ChanConvexHull:
    def __init__(self, points):
        self.points = points

    def convex_hull(self, n, screen):
        if n < 3:
            return

        hull = []

        leftmost = min(self.points, key=lambda p: p.x)
        current = leftmost

        while True:
            hull.append(current)
            next_point = self.points[0]

            for j in range(1, n):
                if (next_point == current or
                        self.orientation(current, next_point, self.points[j]) == 2):
                    next_point = self.points[j]

            current = next_point

            screen.fill((0, 0, 0))
            for point in self.points:
                point.draw(screen)

            for i in range(len(hull)):
                p1 = hull[i]
                p2 = hull[(i + 1) % len(hull)]
                pygame.draw.line(screen, (255, 255, 255), (p1.x, p1.y), (p2.x, p2.y), 2)

            pygame.display.update()
            pygame.time.delay(500)

            if current == leftmost:
                break

        return hull

    def orientation(self, p, q, r):
        val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
        if val == 0:
            return 0  # collinear
        elif val > 0:
            return 1  # clockwise
        else:
            return 2  # counterclockwise

def chan(screen):
    width, height = 1366, 768
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Chan's Algo Visualization")

    # Generate random points
    points = [po.Point(random.randint(50, width - 50), random.randint(50, height - 50)) for _ in range(20)]

    chan_hull = ChanConvexHull(points)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        for point in points:
            point.draw(screen)

        chan_convex_hull = chan_hull.convex_hull(len(points), screen)

        pygame.display.flip()

    pygame.quit()
