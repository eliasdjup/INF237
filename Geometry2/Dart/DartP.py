import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return math.hypot(other.x - self.x, other.y - self.y)

    def doesturnleft(self, p, q):
        return ((p.x - self.x) * (q.y - self.y) - (p.y - self.y) * (q.x - self.x)) < 0

def graham(points):
    points.sort(key=lambda p:[p.x,p.y])
    S, hull = [], []
    for p in points:
        while len(S) >= 2 and S[-2].doesturnleft(S[-1], p):
            S.pop()
        S.append(p)
    hull += S

    S = []
    for p in reversed(points):
        while len(S) >= 2 and S[-2].doesturnleft(S[-1], p):
            S.pop()
        S.append(p)

    hull += S[1:]

    return hull


while True:
    try:
        i = list(map(float, input().split(" ")))
        n = int(len(i)/2)
        if n == 1:
            print(float(100))
        else:
            points = [Point(x,y) for (x,y) in zip(i[::2], i[1::2])]
            g_points = graham(points)
            res = sum([g_points[idx].dist(g_points[idx+1]) for idx in range(len(g_points)-1)])
            print((100*n)/(1+res))

    except EOFError:
         exit()

