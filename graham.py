from functools import cmp_to_key
import pygame
import random as r
import math
import point as po



p0 = po.Point(0, 0)

# A utility function to find next to top in a stack
def nextToTop(S):
    return S[-2]

# A utility function to return square of distance
# between p1 and p2
def distSq(p1, p2):
    return ((p1.x - p2.x) * (p1.x - p2.x) +
            (p1.y - p2.y) * (p1.y - p2.y))

# To find orientation of ordered triplet (p, q, r).
# The function returns following values
# 0 --> p, q and r are collinear
# 1 --> Clockwise
# 2 --> Counterclockwise
def orientation(p, q, r):
    val = ((q.y - p.y) * (r.x - q.x) -
           (q.x - p.x) * (r.y - q.y))
    if val == 0:
        return 0  # collinear
    elif val > 0:
        return 1  # clock wise
    else:
        return 2  # counterclockwise

# A function used by cmp_to_key function to sort an array of
# points with respect to the first point
def compare(p1, p2):
    # Find orientation
    o = orientation(p0, p1, p2)
    if o == 0:
        if distSq(p0, p2) >= distSq(p0, p1):
            return -1
        else:
            return 1
    else:
        if o == 2:
            return -1
        else:
            return 1

# Prints convex hull of a set of n points.
def graham(screen):
    pygame.init()
    points = []
    for a in range (0,20):
        points.append(po.Point(r.randint(100, 768-100),r.randint(100, 768-100)))

    n = len(points)
    hull = []  # To store the final convex hull

    # Find the bottommost point
    ymin = points[0].y
    min_index = 0
    for i in range(1, n):
        y = points[i].y

        # Pick the bottom-most or choose the left
        # most point in case of tie
        if ((y < ymin) or
                (ymin == y and points[i].x < points[min_index].x)):
            ymin = points[i].y
            min_index = i

    # Place the bottom-most point at the beginning
    points[0], points[min_index] = points[min_index], points[0]

    # Sort the rest of the points based on polar angle in
    # counterclockwise order from the bottom-most point
    p0 = points[0]
    points = sorted(points[1:], key=lambda p: math.atan2(p.y - p0.y, p.x - p0.x))

    hull.append(points[0])
    hull.append(points[1])

    for i in range(2, n):
        while len(hull) > 0 and orientation(hull[-2], hull[-1], points[i]) != 2:
            hull.pop()
        hull.append(points[i])

        # Draw the current state of the convex hull
        screen.fill((0, 0, 0))
        for point in points:
            point.draw(screen)

        for j in range(len(hull) - 1):
            p1 = hull[j]
            p2 = hull[j + 1]
            pygame.draw.line(screen, (255, 255, 255), (p1.x, p1.y), (p2.x, p2.y), 2)

        pygame.display.update()
        pygame.time.delay(500)

    # Draw the last line connecting the last and first points in the convex hull
    if len(hull) > 1:
        pygame.draw.line(screen, (255, 255, 255), (hull[-1].x, hull[-1].y), (hull[0].x, hull[0].y), 2)
        pygame.display.update()
        pygame.time.delay(500)


    width = 1366
    height = 768
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Graham's Scan Visualization")


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        # Draw all points
        for point in points:
            point.draw(screen)

        # Draw convex hull step by step
        graham(screen)

pygame.quit()