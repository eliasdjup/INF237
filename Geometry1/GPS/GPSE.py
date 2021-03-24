import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "("+str(self.x)+","+str(self.y)+")"


n, t = [int(x) for x in input().split()]

x, y, prev_time = [int(x) for x in input().split()]

gps_time = 1

prev_act = Point(x, y)
gps_point = prev_act
prev_gps_point = prev_act

actual_dist = 0.0
gps_dist = 0.0

for i in range(n-1):
    x, y, current_time = [int(x) for x in input().split()]
    
    current_act = Point(x, y)

    actual_dist += current_act.distance(prev_act)

    dx = (current_act.x - prev_act.x) / (current_time - prev_time)
    dy = (current_act.y - prev_act.y) / (current_time - prev_time)

    while gps_time <= current_time:
        gps_point.x += dx
        gps_point.y += dy  

        if (gps_time % t == 0):
            gps_dist += gps_point.distance(prev_gps_point)
            prev_gps_point = gps_point
        
        gps_time+=1

    prev_act = current_act
    prev_time = current_time

gps_dist += current_act.distance(prev_gps_point)

print((actual_dist - gps_dist) * 100 / actual_dist)
