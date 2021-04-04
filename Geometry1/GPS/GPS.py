# cat .\Geometry1\GPS\sample1.in | python .\Geometry1\GPS\GPS.py

def getGpsPoints(positions, stepsize):
    ''' Calculate points based on GPS refresh-rate '''
    if len(positions) == 1:
        return positions
    
    # Initialize variables
    cutout_point = positions[-1][2]
    points = [positions[0]]
    pre_x, pre_y, pre_t = positions[0]
    t_total = stepsize
    current_index = 1

    while t_total < cutout_point:
        x,y,t = positions[current_index]
        while t_total > t:
            current_index += 1
            pre_x, pre_y, pre_t = x,y,t
            x,y,t = positions[current_index]

        t_diff = (t_total - pre_t) / (t - pre_t)
        newPoint = ((x - pre_x) * t_diff + pre_x,(y - pre_y) * t_diff + pre_y ,t_total)
        points.append(newPoint)
        t_total += stepsize
    points.append(positions[-1])
    return points



def distance(x1, x2, y1, y2):
    ''' Return distance between two input points '''
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def runDist(pos):
    ''' Calculates the combined distance between all points in a list '''
    tot = 0
    pre_x, pre_y, _ = pos[0]
    for pos in pos[1:]:
        x, y, _ = pos
        tot += distance(pre_x, x, pre_y, y)
        pre_x, pre_y = x, y
    return tot
    



n, t = map(int, input().split())
positions = [list(map(int,input().split())) for _ in range(n)]
last_t = positions[-1][2]


def list_generator(l):
    return iter(l)


actual = runDist(positions)
gps = runDist(getGpsPoints(positions, t))

print(((actual - gps) / actual) * 100)





#print(calcPointsOnLine(p1, p2, 1, 1))


#print(positions)
#print(positions[1:])

'''

def getGpsPoints_(pos, gpsTime):
    points = []
    start_x, start_y, start_t= pos[0]
    leftover_time = 0
    diff_x, diff_y = 0, 0

    for (x,y,t) in pos[1:]:

        # Line between start and p. (Line information, slope per t)
        diff_t = t - start_t

        diff_x = (x - start_x) # Change in x in current line segment.
        diff_y = (y - start_y) # Change in y in current line segment.
        
        steps = (diff_t - leftover_time) // gpsTime
        if steps == 0:
            continue

        # Find first point on line based on "leftover"-t
        start_x, start_y = start_x + diff_x*leftover_time/diff_t, start_y + diff_y*leftover_time/diff_t
        points.append((start_x, start_y, -1))

        leftover_time = diff_t




        for i in range(steps):
            new_x = start_x + diff_x * i
            new_y = start_y + diff_y * i
            points.append((new_x, new_y, -1))
            leftover_time -= gpsTime

        # Update start = p
        start_x, start_y, start_t = x, y, t

    #print(points)
    return points
def calcPointsOnLine(p1, p2, t_curr, t):

    points = []
    x1, y1, t1 = p1
    x2, y2, t2 = p2

    x_diff = x2 - x1
    y_diff = y2 - y1
    t_diff = t2 - t1

    x_curr = x1 - x_diff*t_curr/t_diff
    y_curr = y1 - y_diff*t_curr/t_diff
    num_points = (t2-t1) // t

    intervalX = x_diff /(num_points)
    intervalY = y_diff /(num_points)

    #x_curr = x1 - intervalX*t_curr
    #y_curr = y1 - intervalY*t_curr

    for i in range(1, num_points+1):
        points.append((x_curr + intervalX * i, y_curr + intervalY * i, 0))

    return points


def runDist(pos, t):
    #Calculates the combined distance between all points in a list
    tot = 0
    pre_x, pre_y, _ = pos[0]
    for pos in pos[1:]:
        x, y, _ = pos
        tot += distance(pre_x, x, pre_y, y)
        pre_x, pre_y = x, y
    return tot


        # while loop until p is reached
        #while not endOfLine:
        #    if :
        #        pass


        #    start_x = start_x + diff_x*gpsTime
        #    start_y = start_y + diff_y*gpsTime

        # Find leftovertime


#            if leftover_time <= 0 or start_x > x or start_y > y:
#                endOfLine = True
#                continue
            
            #points.append((start_x,start_y, -1))

        # Update start = p
        #start_x, start_y = x, y

        # Draw new p from pos




        
    points = [positions[0]]
    generator = list_generator(positions[1:])
    current_t = gpsT

    start_x, start_y, start_t = positions[0]
    x,y,t = next(generator)
    #for x,y,t in generator:
    while current_t < last_t:
        
        if current_t > t:
            x,y,t = next(generator)

        while t < gpsT: # Or x,y,t not None
            start_x, start_y, start_y = x,y,t
            x,y,t = next(generator)

        diff_t = (current_t - start_t) / (t - start_t)

        print("x", (x - start_x)*diff_t)
        print("y", (y - start_y)*diff_t)

        #newPoint = ((start_x + (x - start_x)*diff_t),( start_y + (y - start_y)*diff_t), current_t)
        #print("s", start_x, start_y)
        #points.append(newPoint)
        #start_x, start_y, start_y = newPoint
        #print(current_t)
        current_t += gpsT
    points.append(positions[-1])
'''