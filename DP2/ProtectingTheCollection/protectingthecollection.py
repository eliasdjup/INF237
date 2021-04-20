#cat .\DP2\ProtectingTheCollection\mirror01.in | py .\DP2\ProtectingTheCollection\protectingthecollection.py
#cat .\DP2\ProtectingTheCollection\mirror02.in | py .\DP2\ProtectingTheCollection\protectingthecollection.py
n, c, r = map(int, input().split())
grid = []

for _ in range(n):
    grid.append(input().split())

def goSouth(grid, curr_c, curr_r):
    new_r = curr_r + 1
    if new_r >= n or new_r < 0:
        return None,None,None

    new_dir = goSouth
    if grid[new_r][curr_c] == '\\' : new_dir = goEast
    elif grid[new_r][curr_c] == '/': new_dir = goWest
    return curr_c, new_r, new_dir


def goNorth(grid, curr_c, curr_r):
    new_r = curr_r - 1
    if new_r >= n or new_r < 0:
        return None,None,None

    new_dir = goNorth
    if grid[new_r][curr_c] == '\\' : new_dir = goWest
    elif grid[new_r][curr_c] == '/': new_dir = goEast
    return curr_c, new_r, new_dir

def goEast(grid, curr_c, curr_r):
    new_c = curr_c + 1
    if new_c >= n or new_c < 0:
        return None,None,None

    new_dir = goEast
    if grid[curr_r][new_c] == '\\' : new_dir = goSouth
    elif grid[curr_r][new_c] == '/': new_dir = goNorth
    return new_c, curr_r, new_dir

def goWest(grid, curr_c, curr_r):
    new_c = curr_c - 1
    if new_c >= n or new_c < 0:
        return None,None,None

    new_dir = goWest
    if grid[curr_r][new_c] == '\\' : new_dir = goNorth
    elif grid[curr_r][new_c] == '/': new_dir = goSouth
    return new_c, curr_r, new_dir


def traverse(grid, c, s_r = 0, direction = goSouth, firstpass = False):

    path = [[c, s_r, direction.__name__[2:]]]
    while True:
        c, s_r, d = direction(grid, c, s_r)
        if d == None : return path
        direction = d
        path.append([c, s_r, direction.__name__[2:]])


newpaths = {
    "East" : ["North", "South"],
    "West" : ["South", "North"],
    "North" : ["East", "West"],
    "South" : ["West", "East"]
}

functions = {
    "East" : goEast,
    "West" : goWest,
    "North" : goNorth,
    "South" : goSouth
}

for p in traverse(grid, c-1):
    new_c, new_r, d = p
    for new_d in newpaths[d]:
        new_path = traverse(grid, new_c, new_r, functions[new_d])
        if new_path[-1][0:2] == [n-1, r-1]:
            print("YES")
            exit()
    
print("NO")


