import math

def angleVector(x1, y1, x2, y2):
    return math.acos( (x1*x2 + y1*y2) / (math.hypot(x1 , y1) * math.hypot(x2 , y2)) )


def update(corner , angles):
    angles.clear()
    
    angles.append(anglePoints(corner[-1], corner[0] , corner[1]))

    for i in range(1, len(corner)):
        angles.append(anglePoints(corner[i-1] , corner[i] , corner[(i+1) % len(corner)]))

def anglePoints(a, b, c):
    x1 = a.x - a.y
    x3 = c.x - b.x 
    y1 = a.y - b.y
    y3 = c.y - b.y

    return angleVector(x1, y1, x3, y3)


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "("+str(self.x)+","+str(self.y)+")"



inp = [int(x) for x in input().split()]

while inp[0] != 0:

    n = inp[0]

    poly = []
    angles = []

    for i in range(1,n*2,2):
        poly.append(Point(inp[i],inp[i+1]))


    update(poly, angles)

    uniMin = 0
    lastRemoved = Point(0,0)
    lastMinIndex = 0


    while True: 
        m = 999999999999
        mIndex = 0
        for i in range(len(angles)):
            if angles[i] < m:
                m = angles[i]
                minIndex = i
  
        if m < uniMin:
            poly.append(Point(lastMinIndex,lastRemoved))
            break
        
        if len(angles) == 3:
            break
        
        lastRemoved = poly.pop(minIndex)
        uniMin = m
        lastMinIndex = minIndex
        
        update(poly , angles)

    print(str(len(poly)) + " " + str(poly[1:-1]))



    inp = [int(x) for x in input().split()]

