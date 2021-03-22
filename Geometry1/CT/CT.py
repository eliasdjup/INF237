def cross(v1, v2):
    return v1.x * v2.y - v1.y * v2.x


def orient(a, b, c):
    return (b - a).cross(c - a)

def sgn2(k, l): # have different sign
    return k * l < 0

def intersect(line1, line2):
    (a, b), (c, d) = line1, line2
    oa = orient(c, d, a)
    ob = orient(c, d, b)
    oc = orient(a, b, c)
    od = orient(a, b, d)
    if sgn2(oa, ob) and sgn2(oc, od):
        return (a * ob - b * oa) / (ob - oa)




n = int(input())

while n != 0:
    for i in range (n):
        x1, x2, y1, y2 = [int(x) for x in input().split()]



    n = int(input())