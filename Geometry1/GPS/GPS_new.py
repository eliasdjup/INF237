
class Pos:
    def __init__(self,x,y,t):
        self.x = x
        self.y = y
        self.t = t

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def unpack(self):
        return self.x, self.y, self.t

    def __repr__(self):
        return "("+str(self.x)+","+str(self.y)+")"


def sumPos(positions):
    s = 0
    for i in range(1, len(positions)):
        s += positions[i-1].distance(positions[i])
    return s

def getGpsPoints(positions, stepsize):
    points = [positions[0]]
    current_segment = 1
    t_total = stepsize
    pre_x, pre_y, pre_t = positions[0].unpack()
    while t_total < positions[-1].t:
        x,y,t = positions[current_segment].unpack()
        while t_total > t:
            current_segment += 1
            pre_x, pre_y, pre_t = x, y, t
            x, y, t = positions[current_segment].unpack()
        

        t_diff = (t_total - pre_t) / (t - pre_t)
        newX = (x - pre_x) * t_diff + pre_x
        newY = (y - pre_y) * t_diff + pre_y
        
        points.append(Pos(newX,newY,t_total))
        t_total += stepsize

    points.append(positions[-1])
    return points


positions = []
n, t = map(int, input().split())
for i in range(n):
    x,y,t_ = map(int,input().split())
    positions.append(Pos(x,y,t_))

def res(posActual, posGps):
    actualDist = sumPos(posActual)
    gpsDist = sumPos(posGps)
    print(100*(actualDist - gpsDist) / actualDist)

res(positions, getGpsPoints(positions,t))


