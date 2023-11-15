import point as po
import pygame
import sys
import random as r

class ConvexHull:
    def __init__(self, points):
        self.points = points
        self.hull = []

    def left_index(self):
        min_idx = 0
        for i in range(1, len(self.points)):
            if self.points[i].x < self.points[min_idx].x:
                min_idx = i
            elif self.points[i].x == self.points[min_idx].x:
                if self.points[i].y > self.points[min_idx].y:
                    min_idx = i
        return min_idx

    def orientation(self, p, q, r):
        val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
        if val == 0:
            return 0
        elif val > 0:
            return 1
        else:
            return 2

    def find_convex_hull(self, screen):
        n = len(self.points)
        if n < 3:
            return

        l = self.left_index()
        p = l
        q = 0
        while True:
            self.hull.append(p)
            q = (p + 1) % n
            for i in range(n):
                if self.orientation(self.points[p], self.points[i], self.points[q]) == 2:
                    q = i

            pygame.draw.line(screen, (255, 255, 255),
                             (self.points[p].x, self.points[p].y),
                             (self.points[q].x, self.points[q].y), 2)
            pygame.display.flip()
            pygame.time.delay(500)  # Adjust the delay as needed

            p = q
            if p == l:
                break

    def draw_convex_hull(self, screen):
        for i in range(len(self.hull) - 1):
            pygame.draw.line(screen, (255, 255, 255), (self.points[self.hull[i]].x, self.points[self.hull[i]].y),
                             (self.points[self.hull[i + 1]].x, self.points[self.hull[i + 1]].y), 2)
            pygame.display.flip()
            pygame.time.delay(500)  # Adjust the delay as needed
        pygame.draw.line(screen, (255, 255, 255), (self.points[self.hull[-1]].x, self.points[self.hull[-1]].y),
                         (self.points[self.hull[0]].x, self.points[self.hull[0]].y), 2)
        pygame.display.flip()
        pygame.time.delay(500)  # Adjust the delay as needed


def jarvis(screen):
    pygame.init()
    # Set up the screen
    
    
    # Create points
    #points = [po.Point(500, 300), po.Point(400, 400), po.Point(300, 100), po.Point(200, 200), po.Point(300, 220), po.Point(50, 50), po.Point(300, 300)]
    points = []
    for a in range (0,10):
        points.append(po.Point(r.randint(100, 768-100),r.randint(100, 768-100)))


    # Create ConvexHull object
    convex_hull = ConvexHull(points)
    
    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

 
    
    
        # Draw points
        screen.fill((0, 0, 0))
        for p in points:
            p.draw(screen)
        # Find and draw convex hull in real-time
        convex_hull.find_convex_hull(screen)
        convex_hull.draw_convex_hull(screen)
    
        pygame.display.flip()
