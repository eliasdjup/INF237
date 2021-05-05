'''
def uniquePathsWithObstacles(A):

    print(A)
    
    # create a 2D-matrix and initializing with value 0
    paths = [[0]*len(A[0]) for i in A]
     
    # initializing the left corner if no obstacle there
    if A[0][0] == 0:
        paths[0][0] = 1
     
    # initializing first column of the 2D matrix
    for i in range(1, len(A)):
         
        # If not obstacle
        if A[i][0] == 0:
            paths[i][0] = paths[i-1][0]
             
    # initializing first row of the 2D matrix
    for j in range(1, len(A[0])):
         
        # If not obstacle
        if A[0][j] == 0:
            paths[0][j] = paths[0][j-1]
             
    for i in range(1, len(A)):
        for j in range(1, len(A[0])):
 
            # If current cell is not obstacle
            if A[i][j] == 0:
                paths[i][j] = paths[i-1][j] + paths[i][j-1]
 
    # returning the corner value of the matrix
    return paths[-1][-1]
def count_the_paths(grid):
    N = len(grid)
    M = len(grid[0])

    ways = [[None for _ in range(M)] for _ in range(N)] # Generate empty matrix to store the number of ways
    ways[N-1][0] = 1 # There's only 1 way to reach the starting point

    for row in range(N-1, -1, -1):
        for col in range(0, M):
            if grid[row][col] == 1: # Blocked cell
                ways[row][col] = 0
            elif row != N-1 or col != 0: # If it's not the starting point
                ways[row][col] = 0
                if row < N-1:
                    ways[row][col] += ways[row+1][col]
                if col > 0:
                    ways[row][col] += ways[row][col-1]

    return ways[0][M-1]

def validMove(x, y):
    return not (x < 0 or y < 0 or x >= N or y >= N)
 
def count_all_paths(maze, x, y, visited, count):
 
    if x == N - 1 and y == N - 1:
        return count + 1

    visited[x][y] = True
 
    if validMove(x, y) and maze[x][y] == 1:

        if x + 1 < N and not visited[x + 1][y]:
            count = count_all_paths(maze, x + 1, y, visited, count)

        if x - 1 >= 0 and not visited[x - 1][y]:
            count = count_all_paths(maze, x - 1, y, visited, count)

        if y + 1 < N and not visited[x][y + 1]:
            count = count_all_paths(maze, x, y + 1, visited, count)
 
    # remove from current path
    visited[x][y] = False
    return count
 

'''
def find_all_paths(H, W, current_map):
    paths = [[0] * W for _ in range(H)]
    current_map[::-1]

    for h in range(H):
        if not current_map[h][0]:
            break
        paths[h][0] = 1
    

    for w in range(1, W):
        runstart = 0
        runsum = 0
        for h in range(H):
            if current_map[h][w]:
                runsum += paths[h][w-1]
                continue
            for h2 in range(runstart, h):
                paths[h2][w] = runsum
            
            runstart = h+1
            runsum = 0

        for h2 in range(runstart, H):
            paths[h2][w] = runsum
        
    print(paths)
    return paths[-1][-1]
'''

# Get_paths(row, column, last_actionz<)

def validMove(x, y, maxX, maxY):
    return not (x < 0 or y < 0 or x >= maxX or y >= maxY)


def get_paths(current_map, rows, columns):
    
    ways = [[0 for _ in range(rows)] for _ in range(columns)]
    
    # Basecase (If we have reached the first column)
    for i in range(rows):
        if current_map[0][i]:
            ways[0][i] = 1
        else:
            break
    
    # Iterative case
    for i in range(1, columns):

'''
from collections import defaultdict
hist = defaultdict

def find_paths(current_map, row, col):
    if 


    #if hist.get((row,col), 0) != 0:
    #    hist[(row,col)] += 1

    #for i in valid_moves(current_map, row, col):
    


r, c = map(int, input().split())

while r or c:
    current_map = [[1 if x == '.' else 0 for x in input()] for _ in range(r)]

    find_all_paths(r, c, current_map)

    r, c = map(int, input().split())

