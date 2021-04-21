
n, c, r = map(int, input().split())
grid = []

for _ in range(n):
    grid.append(input().split())

functions = {
    "north" : lambda x,y: (x, y-1),
    "east" : lambda x,y: (x+1, y),
    "west" : lambda x,y: (x-1, y),
    "south" : lambda x,y: (x, y+1),
}

backslash = {
    "north" : "west",
    "south" : "east",
    "east" : "south",
    "west" : "north"
}
slash = {
    "north" : "east",
    "south" : "west",
    "east" : "north",
    "west" : "south"
}

def traverse(grid, curr_c, curr_r, direction):
    if grid[curr_r][curr_c] == "/": direction = slash[direction]
    elif grid[curr_r][curr_c] == "\\": direction = backslash[direction]

    path = [[curr_c, curr_r, direction, grid[curr_r][curr_c]]]
    while True:
        curr_c, curr_r = functions[direction](curr_c, curr_r)

        if (curr_c >= n or curr_c < 0) or (curr_r >= n or curr_r < 0):
            return path

        if grid[curr_r][curr_c] != '.':
            direction = slash[direction] if grid[curr_r][curr_c] == "/" else backslash[direction]
        path.append([curr_c, curr_r, direction, grid[curr_r][curr_c]])


c, r = c-1, r-1

from_start = traverse(grid, c, 0, "south")
from_end = traverse(grid, n-1, r, "west")

positions_start = []
for c, r, direction, cell in from_start:
    if cell == '.':
        positions_start.append([c,r, direction, cell])

positions_end = []
for c, r, direction, cell in from_end:
    if cell == '.':
        positions_end.append([c,r, direction, cell])

res_list = []
for s in positions_start:
    for e in positions_end:
        if s[:2] == e[:2]:
            res_list.append((s,e))

if len(res_list) > 0:
    print("YES")
else:
    print("NO")

#for curr_c, curr_r, direction, cell in from_end:
#    grid[curr_r][curr_c] = "#"

#for i in grid:
#    print(i)

#10 1 2
#. . . . . . . . . .
#. / . . . . . . . \
#. . / . . . . . \ .
#. . . / . . . \ . .
#. . . . / . \ . . .
#. . . . \ . . . . .
#. . . \ . . / . . .
#. . \ . . . . / . .
#. \ . . . . . . / .
#\ . . . . . . . . /