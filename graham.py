from functools import cmp_to_key
import pygame
import random as r
import math
import point as po

class GrahamConvexHull:
    def __init__(self, points):
        self.points = points
        self.screen = None

    def graham(self):
        pygame.init()

        n = len(self.points)
        hull = []

        # Find the bottommost point
        ymin = self.points[0].y
        min_index = 0
        for i in range(1, n):
            y = self.points[i].y
            if ((y < ymin) or
                    (ymin == y and self.points[i].x < self.points[min_index].x)):
                ymin = self.points[i].y
                min_index = i

        # Place the bottom-most point at the beginning
        self.points[0], self.points[min_index] = self.points[min_index], self.points[0]

        # Sort the rest of the points based on polar angle in
        # counterclockwise order from the bottom-most point
        p0 = self.points[0]
        self.points = sorted(self.points[1:], key=lambda p: math.atan2(p.y - p0.y, p.x - p0.x))

        hull.append(self.points[0])
        hull.append(self.points[1])

        for i in range(2, n):
            while len(hull) > 0 and self.orientation(hull[-2], hull[-1], self.points[i]) != 2:
                hull.pop()
            hull.append(self.points[i])

            # Draw the current state of the convex hull
            self.screen.fill((0, 0, 0))
            for point in self.points:
                point.draw(self.screen)

            for j in range(len(hull) - 1):
                p1 = hull[j]
                p2 = hull[j + 1]
                pygame.draw.line(self.screen, (255, 255, 255), (p1.x, p1.y), (p2.x, p2.y), 2)

            pygame.display.update()
            pygame.time.delay(500)

        # Draw the last line connecting the last and first points in the convex hull
        if len(hull) > 1:
            pygame.draw.line(self.screen, (255, 255, 255), (hull[-1].x, hull[-1].y), (hull[0].x, hull[0].y), 2)
            pygame.display.update()
            pygame.time.delay(500)

    def orientation(self, p, q, r):
        val = ((q.y - p.y) * (r.x - q.x) -
               (q.x - p.x) * (r.y - q.y))
        if val == 0:
            return 0  # collinear
        elif val > 0:
            return 1  # clock wise
        else:
            return 2  # counterclockwise

def graham(screen):
    # Create points
    points = [po.Point(r.randint(100, 768 - 100), r.randint(100, 768 - 100)) for _ in range(20)]

    graham_hull = GrahamConvexHull(points)
    graham_hull.screen = screen

    # Draw convex hull using Graham's Scan
    graham_hull.graham()

# Uncomment the following lines if you want to run the graham module independently
# width = 1366
# height = 768
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Graham's Scan Visualization")
# graham(screen)
# pygame.quit()
