n, c ,r = [int(x) for x in input().split()]

room = []

for i in range(n):
    room.append(input().split(" "))

print(room)

def nextCor(x, y, d):
    if d == 'S':
        return x, y+1

    elif d == 'E':
        return x+1, y

    elif d == 'N':
        return x, y-1
        
    elif d == 'W':
        return x-1, y


def possible(room):
    sensor = False
    x = 0
    y = c-1
    d = 'S'
    while not sensor:

        current = room[x][y]

        if current == '.':
        
        elif current == 

        x, y = nextCor(x,y,d)
        
              

