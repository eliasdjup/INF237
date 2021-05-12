
speed_list = []
n = int(input())
points = [tuple(map(int, input().split()))]
print(points)

for i in range(n):
    points.append(tuple(map(int, input().split())))
    #print(points[i])
    d_t = points[i][0] - points[i-1][0]
    d_d = points[i][1] - points[i-1][1]

    avg_speed = d_d / d_t
 
    speed_list.append(avg_speed)

print(max(speed_list))
