from Point import Point
import copy

class Polygon:
    """
    A polygon class with any number of points.
    """

    def __init__(self):
        self.points = []

    def add_point(self, x, y):
        self.points.append(Point(x, y))

    def get_point(self, index):
        if 0 < index < len(self.points):
            return self.points[index]
        else:
            return None

    def remove_point(self, index):
        if 0 < index < len(self.points):
            del self.points[index]

    def move(self, dx, dy):
        for p in self.points:
            p.move(dx, dy)

    def get_point_index(self, pt):
        """
        Search through the points in the polygon and return the index if the
        passed in point is found, or -1 otherwise.
        """
        index = -1
        for i,p in enumerate(self.points):
            if p.equals(pt):
                index = i
        return index

    def __str__(self):
        s = ""
        for p in self.points:
            s += str(p) + "; "
        return s

    def equals(self, p2):
        eq = len(self.points)==len(p2.points)
        for p1,p2 in zip(self.points, p2.points):
            eq = eq and p1.equals(p2)
            return eq

    def insert_point_at(self, pt, index):
        







        
