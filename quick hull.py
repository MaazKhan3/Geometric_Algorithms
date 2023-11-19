import pygame
import sys
import random

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Pygame initialization
pygame.init()
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('QuickHull Visualization')
clock = pygame.time.Clock()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 6

    def draw(self, color=WHITE):
        pygame.draw.circle(screen, color, (self.x, self.y), self.radius)

class QuickHull:
    def __init__(self, points):
        self.points = points
        self.hull = []

    def find_hull(self):
        if len(self.points) < 3:
            print("Convex hull is not possible with less than 3 points.")
            return

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
        self.find_hull_recursive(leftmost, rightmost, points_left)
        self.find_hull_recursive(rightmost, leftmost, points_right)

        return self.hull

    def find_hull_recursive(self, p1, p2, points):
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
        self.draw_hull_lines(screen, color=WHITE)
        farthest_point.draw(color=RED)
        pygame.display.flip()
        clock.tick(1)  # Adjust the speed of visualization

        # Recursively find the convex hull on each side of the line
        self.find_hull_recursive(p1, farthest_point, points_left)
        self.find_hull_recursive(farthest_point, p2, points_right)

    def draw_hull_lines(self, screen, color=WHITE):
        if len(self.hull) > 1:
            for i in range(len(self.hull) - 1):
                self.draw_line(screen, self.hull[i], self.hull[i + 1], color)
            self.draw_line(screen, self.hull[-1], self.hull[0], color)
        else:
            print("Convex hull not found.")

    def draw_line(self, screen, p1, p2, color=WHITE):
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

# Create random points
num_points = 20
points = [Point(random.randint(50, screen_size[0] - 50), random.randint(50, screen_size[1] - 50)) for _ in range(num_points)]
for p in points:
        p.draw()
# Sort points by x-coordinate for initial visualization
points.sort(key=lambda p: p.x)

# Pygame loop
running = True
quick_hull = QuickHull(points)
convex_hull = quick_hull.find_hull()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    # Draw points
    for p in points:
        p.draw()

    # Draw convex hull lines
    quick_hull.draw_hull_lines(screen)

    pygame.display.flip()
    clock.tick(1)  # Adjust the speed of visualization

# Quit Pygame
pygame.quit()
sys.exit()