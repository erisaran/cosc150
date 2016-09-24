import math

class Point:
    def __init__(self):
        self.pt[x,y]
        self.x = 0
        self.y = 0

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance(self, p2):
        dx = self.x - p2.x
        dy = self.y - p2.y
        return math.sqrt(dx*dx+dy*dy)

    def equals(self, p2):
        return (self.x == p2.x) and (self.y == p2.y)

    

    
