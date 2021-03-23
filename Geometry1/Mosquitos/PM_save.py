import math
import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "("+str(self.x)+", "+str(self.y)+")"


def center(p, q, radius):
    mid = Point(((p.x + q.x)/2), ((p.y + q.y)/2))

    l = (math.pow(radius, 2)) - (math.pow(p.dist(mid), 2))

    # Square root of zero
    if l < 0:
        return None

    mid_centre = math.sqrt(l)
    
    radians = math.atan2(p.x - q.x, q.y - p.y)

    return Point(mid_centre * math.cos(radians) + mid.x, mid_centre * math.sin(radians) + mid.y)



n = int(input())


for _ in range(n):
    input()
    inp = input().split()
    m = int(inp[0])
    d = float(inp[1])/2.0

    points = []

    for _ in range(m):
        x, y = [float(x) for x in input().split()]
        points.append(Point(x,y))

    res = 0

    for a in range(m):
        for b in range(m):
            temp_res = 0

            cntr = center(points[a],points[b],d)

            if cntr is None:
                continue

            for k in range(m):
                p_dist = cntr.dist(points[k])
                if (p_dist <= d):
                    temp_res += 1
 
            if (temp_res > res): 
                res = temp_res

    print(res)