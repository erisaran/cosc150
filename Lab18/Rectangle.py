from Point import *
import copy

class Rectangle:
    def __init__(self):
        self.corner = Point()
        self.width = 100
        self.height = 100

    def centre(self):
        c = Point()
        c.x = self.corner.x + self.width/2.0
        c.y = self.corner.y + self.height/2.0
        return c

    def equals(self,other):
        """
        >>> r1 = Rectangle()
        >>> r1.corner.x = 50
        >>> r1.corner.y = 40
        >>> r1.width = 200
        >>> r2 = Rectangle()
        >>> r2.corner.x = 50
        >>> r2.corner.y = 40
        >>> r2.width = 200
        >>> r1.equals(r2)
        True
        >>> r2.height = 200
        >>> r1.equals(r2)
        False
        """
        q = self.corner.x, self.corner.y, self.width, self.height
        x = other.corner.x, other.corner.y, other.width, other.height
        if q == x:
            return True
        else:
            return False
            
    def move(self, xdist, ydist):
        self.corner.x += xdist
        self.corner.y += ydist
        return self.corner.x, self.corner.y


box = Rectangle()
print box.corner.x, box.corner.y, box.width, box.height
c = box.centre()
print c.x, c.y

if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)
