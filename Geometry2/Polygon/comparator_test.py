import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __lt__(self, other):
        if self.x > other.x:
            return False
        if self.x == other.x:
            if self.y > other.y:
                return False
        return True
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

lst = [Point(x,y) for x in range(1, 9, 3) for y in range(9, 1, -2)]
print(lst)
print(sorted(lst))