import pygame
import random as r
import point as po

class QuickElimination:
    def __init__(self, points):
        self.points = points
        self.screen = None

    def quick_elimination(self, left, right, points, convex_hull):
        if len(points) == 0:
            return

        # Find the point with the maximum distance
        max_dist = 0
        farthest_point = None
        for point in points:
            dist = self.distance(left, right, point)
            if dist > max_dist:
                max_dist = dist
                farthest_point = point

        # Add the farthest point to the convex hull
        convex_hull.append(farthest_point)

        # Divide the points into two sets
        set1 = []
        set2 = []
        for point in points:
            if point != farthest_point:
                if self.orientation(left, farthest_point, point) == -1:
                    set1.append(point)
                elif self.orientation(farthest_point, right, point) == -1:
                    set2.append(point)

        # Recursively find the convex hull on both sides of the line
        self.quick_elimination(left, farthest_point, set1, convex_hull)
        self.quick_elimination(farthest_point, right, set2, convex_hull)

    def distance(self, left, right, point):
        return abs((right.x - left.x) * (left.y - point.y) - (left.x - point.x) * (right.y - left.y))

    def orientation(self, p, q, r):
        val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
        if val == 0:
            return 0  # collinear
        elif val > 0:
            return 1  # clockwise
        else:
            return -1  # counterclockwise

    def draw_quick_elimination(self):
        if len(self.points) < 3:
            return

        convex_hull = []
        # Find the leftmost and rightmost points
        leftmost = min(self.points, key=lambda p: p.x)
        rightmost = max(self.points, key=lambda p: p.x)

        convex_hull.append(leftmost)
        convex_hull.append(rightmost)

        # Divide the points into two sets based on the side of the line
        set1 = []
        set2 = []
        for point in self.points:
            if point != leftmost and point != rightmost:
                if self.orientation(leftmost, rightmost, point) == -1:
                    set1.append(point)
                elif self.orientation(leftmost, rightmost, point) == 1:
                    set2.append(point)

        # Recursively find the convex hull on both sides of the line
        self.quick_elimination(leftmost, rightmost, set1, convex_hull)
        self.quick_elimination(rightmost, leftmost, set2, convex_hull)

        # Sort the convex hull points for drawing
        convex_hull.sort(key=lambda p: p.x)

        # Draw the convex hull
        for i in range(len(convex_hull) - 1):
            pygame.draw.line(self.screen, (255, 255, 255), (convex_hull[i].x, convex_hull[i].y),
                             (convex_hull[i + 1].x, convex_hull[i + 1].y), 2)

        pygame.draw.line(self.screen, (255, 255, 255), (convex_hull[-1].x, convex_hull[-1].y),
                         (convex_hull[0].x, convex_hull[0].y), 2)

        pygame.display.update()
        pygame.time.delay(1000)  # Adjust the delay as needed

def quick_elimination(screen):
    pygame.init()
    points = [po.Point(r.randint(100, 768 - 100), r.randint(100, 768 - 100)) for _ in range(20)]

    quick_elimination_obj = QuickElimination(points)
    quick_elimination_obj.screen = screen

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        for point in points:
            point.draw(screen)

        quick_elimination_obj.draw_quick_elimination()

    pygame.quit()