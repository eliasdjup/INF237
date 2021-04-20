from itertools import product as iter_product

n, c, r = map(int, input().split())
c, r = c-1, r-1
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
    path = [[curr_c, curr_r, direction]]
    while True:
        curr_c, curr_r = functions[direction](curr_c, curr_r)

        if (curr_c >= n or curr_c < 0) or (curr_r >= n or curr_r < 0):
            return path

        if grid[curr_r][curr_c] != '.':
            direction = slash[direction] if grid[curr_r][curr_c] == "/" else backslash[direction]
        path.append([curr_c, curr_r, direction])


def checkpath(path):
    if path[-1][0:2] == [n-1, r]:
        print("YES")
        return
    else:
        for p, get_dir in iter_product(range(len(path)), [slash, backslash]):
            new_c, new_r, d = path[p]
            new_path = traverse(grid, new_c, new_r, get_dir[d])
            if new_path[-1][0:2] == [n-1, r]:
                print("YES")
                return
    print("NO")

path = traverse(grid, c, 0, "south")
checkpath(path)