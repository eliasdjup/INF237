import math

def distance(p1, p2):
    x1,y1 = p1
    x2, y2 = p2
    return math.hypot(x1 - x2, y1 - y2)

def center(mosk1, mosk2, r):
    x1, y1 = mosk1
    x2, y2 = mosk2
    px = (x1 + x2) / 2
    py = (y1 + y2) / 2
    p = (px, py)

    t = r**2 - distance(mosk1, p)**2

    if t < 0:
        return None
    
    c = t**0.5
    rads = math.atan2(x1 - x2, y2 - y1)

    rx = c * math.cos(rads) + px
    ry = c * math.sin(rads) + py
    return((rx,ry))    



def checkcase(moskitos, m, r):
    result = 0
    for mosk1 in range(m):
        for mosk2 in range(m):
            r_ = 0
            c = center(moskitos[mosk1], moskitos[mosk2], r)
            if c is None:
                continue

            for i in range(m):
                n_dist = distance(c,moskitos[i])
                if (n_dist <= r):
                    r_ += 1
            
            result = max(result, r_)


    print(result)


n = int(input())
for _ in range(n):
    case_moskitos = []
    input()
    m, d = input().split()
    m = int(m)
    d = float(d)
    r = d / 2.0

    for _ in range(m):
        x, y = map(float, input().split())
        case_moskitos.append((x,y))

    checkcase(case_moskitos, m, r)
