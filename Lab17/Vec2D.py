class Vec2D:
    def __init__(self):
        self.x = 0
        self.y = 0

    def __add__(self, other):
        val = Vec2D()
        val.x = self.x + other.x
        val.y = self.y + other.y
        return(val)

    def __sub__(self,other):
        val = Vec2D()
        val.x = self.x - other.x
        val.y = self.y - other.y
        return(val)

    def __mul__(self, times):
        val = Vec2D()
        val.x = self.x * times
        val.y = self.y * times
        return(val)
    
    def combine(self):
        x = self.x + self.y
        return(x)
