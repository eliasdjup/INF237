
import math
from copy import copy, deepcopy

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        if self.x > other.x:
            return False
        if self.x == other.x:
            if self.y > other.y:
                return False
        return True

    #https://math.stackexchange.com/questions/274712/calculate-on-which-side-of-a-straight-line-is-a-given-point-located
    def shortestdist_point2line(self, end, point):
        return (point.x - end.x) * (self.y - end.y) - (point.y - end.y) * (self.x - end.x)
        #return (other.x - other_2.x) * (self.y - other_2.y) - (other.y - other_2.y) * (self.x - other_2.x)

def calc(points, points_s):
    polygon_points = []
    ordering = []
    for i in range(len(points_s)):
        while len(polygon_points) >=2 and (points_s[i].shortestdist_point2line(polygon_points[-2], polygon_points[-1]) > 0):
            polygon_points.pop()
        polygon_points.append(points_s[i])

    for i in range(len(points_s),0,-1):
        if points_s[i-1] not in polygon_points:
            polygon_points.append(points_s[i-1])

    for res_points in polygon_points:
        ordering.append(points.index(res_points))
    displayresult(ordering)


def displayresult(res):
    print(" ".join(map(str,res)))

def main():
    c = int(input())
    for _ in range(c):

        case = list(map(int, input().split()))
        n = case[0]
        points = [Point(case[i], case[i+1]) for i in range(1,n*2,2)]
        points_s = sorted(deepcopy(points))

        calc(points, points_s)

if __name__ == '__main__':
    main()