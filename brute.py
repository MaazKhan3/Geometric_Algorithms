import pygame
import sys
import random as r
import point as po

class ConvexHull:
    def __init__(self, points):
        self.points = points
        self.hull = []

    def orientation(self, p, q, r):
        val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
        if val == 0:
            return 0
        elif val > 0:
            return 1
        else:
            return 2

    def is_convex_hull_point(self, p, q, r):
        for i in range(len(self.points)):
            if i != p and i != q and i != r:
                if self.orientation(self.points[p], self.points[q], self.points[i]) == 0:
                    return False
        return True

    def find_convex_hull_bruteforce(self, screen):
        n = len(self.points)
        if n < 3:
            return

       
        for p in self.points:
            p.draw(screen)

        pygame.display.flip()
        pygame.time.delay(1000)  

        for p in range(n):
            for q in range(n):
                if p != q:
                    for r in range(n):
                        if p != r and q != r:
                            if self.orientation(self.points[p], self.points[q], self.points[r]) == 2 and self.is_convex_hull_point(p, q, r):
                                pygame.draw.line(screen, (255, 255, 255),
                                                 (self.points[p].x, self.points[p].y),
                                                 (self.points[q].x, self.points[q].y), 2)
                                pygame.display.flip()
                                pygame.time.delay(100)  

        pygame.time.delay(1000)  

    def draw_convex_hull(self, screen):
        for i in range(len(self.hull) - 1):
            pygame.draw.line(screen, (249, 222, 201), (self.points[self.hull[i]].x, self.points[self.hull[i]].y),
                             (self.points[self.hull[i + 1]].x, self.points[self.hull[i + 1]].y), 2)
            pygame.display.flip()
            pygame.time.delay(100) 
        pygame.draw.line(screen, (249, 222, 201), (self.points[self.hull[-1]].x, self.points[self.hull[-1]].y),
                         (self.points[self.hull[0]].x, self.points[self.hull[0]].y), 2)
        pygame.display.flip()
        pygame.time.delay(100) 


def brute_force(screen):
    pygame.init()
    
    # Create points
    points = []
    for a in range(0, 8):
        points.append(po.Point(r.randint(100, 768-100), r.randint(100, 768-100)))

    # Create ConvexHull object
    convex_hull = ConvexHull(points)

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    return  

        # Draw points
        for p in points:
            p.draw(screen)

        convex_hull.find_convex_hull_bruteforce(screen)
        pygame.display.flip()
        pygame.time.delay(2000)  
        pygame.time.delay(500)  