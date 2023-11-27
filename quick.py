import pygame
import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 6

    def draw(self, screen, color=(255, 255, 255)):
        pygame.draw.circle(screen, color, (self.x, self.y), self.radius)

class QuickHull:
    def __init__(self, points):
        self.points = points
        self.hull = []

    def find_hull(self, screen):
        if len(self.points) < 3:
            print("Convex hull is not possible with less than 3 points.")
            return

        # Sort points by x-coordinate for initial visualization
        self.points.sort(key=lambda p: p.x)

        # Draw all points initially
        for p in self.points:
            p.draw(screen)

        pygame.display.flip()
        pygame.time.delay(500)  # Adjust the delay as needed

        # Find the leftmost and rightmost points
        min_x, max_x = float('inf'), float('-inf')
        leftmost, rightmost = None, None
        for point in self.points:
            if point.x < min_x:
                min_x = point.x
                leftmost = point
            if point.x > max_x:
                max_x = point.x
                rightmost = point

        self.hull.append(leftmost)
        self.hull.append(rightmost)

        # Split the points into two sets based on which side of the line they lie
        points_left = [point for point in self.points if self.orientation(leftmost, rightmost, point) == 1]
        points_right = [point for point in self.points if self.orientation(leftmost, rightmost, point) == -1]

        # Recursively find the convex hull on each side of the line
        self.find_hull_recursive(leftmost, rightmost, points_left, screen)
        self.find_hull_recursive(rightmost, leftmost, points_right, screen)

        return self.hull

    def find_hull_recursive(self, p1, p2, points, screen):
        if not points:
            return

        # Find the point with the maximum distance from the line formed by p1 and p2
        max_distance = 0
        farthest_point = None
        for point in points:
            current_distance = self.distance(p1, p2, point)
            if current_distance > max_distance:
                max_distance = current_distance
                farthest_point = point

        # Add the farthest point to the convex hull
        self.hull.insert(self.hull.index(p2), farthest_point)

        # Split the points into two sets based on which side of the line they lie
        points_left = [point for point in points if self.orientation(p1, farthest_point, point) == 1]
        points_right = [point for point in points if self.orientation(farthest_point, p2, point) == 1]

        # Draw the current step
        self.draw_hull_lines(screen, color=(255, 255, 255))
        farthest_point.draw(screen, color=(255, 0, 0))
        pygame.display.flip()
        pygame.time.delay(500) 

        # Recursively find the convex hull on each side of the line
        self.find_hull_recursive(p1, farthest_point, points_left, screen)
        self.find_hull_recursive(farthest_point, p2, points_right, screen)

    def draw_hull_lines(self, screen, color=(255, 255, 255)):
        if len(self.hull) > 1:
            for i in range(len(self.hull) - 1):
                self.draw_line(screen, self.hull[i], self.hull[i + 1], color)
                pygame.display.flip()
                pygame.time.delay(500)  
            self.draw_line(screen, self.hull[-1], self.hull[0], color)
            pygame.display.flip()
            pygame.time.delay(500)  
        else:
            print("Convex hull not found.")

    def draw_line(self, screen, p1, p2, color=(255, 255, 255)):
        pygame.draw.line(screen, color, (p1.x, p1.y), (p2.x, p2.y), 2)

    @staticmethod
    def orientation(p, q, r):
        val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
        if val == 0:
            return 0
        return 1 if val > 0 else -1

    @staticmethod
    def distance(p1, p2, p):
        return abs((p.y - p1.y) * (p2.x - p1.x) - (p2.y - p1.y) * (p.x - p1.x)) / (
                    (p2.y - p1.y) ** 2 + (p2.x - p1.x) ** 2) ** 0.5

def quick_hull(screen):
    pygame.init()

    num_points = 20
    points = [Point(random.randint(50, 750), random.randint(50, 550)) for _ in range(num_points)]

    quick_hull_instance = QuickHull(points)

    convex_hull = quick_hull_instance.find_hull(screen)

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    return  
