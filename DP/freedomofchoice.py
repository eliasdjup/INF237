'''
def count_paths(H, W, clear_grid):
    path_grid = [[0] * W for _ in range(H)]
    
    for h in range(H):
        if not clear_grid[h][0]:
            break
        path_grid[h][0] = 1
    
    for w in range(1, W):
        run_start = 0
        run_sum = 0
        for h in range(H):
            if clear_grid[h][w]:
                run_sum += path_grid[h][w - 1]
                continue
            for h2 in range(run_start, h):
                path_grid[h2][w] = run_sum
            run_start = h + 1
            run_sum = 0
        for h2 in range(run_start, H):
            path_grid[h2][w] = run_sum
    return path_grid[-1][-1]






def main():
    H, W = [int(x) for x in input().split()]
    while H or W:
        grid = [
            [c == '.' for c in input()] for _ in range(H)
        ][::-1]
        print(count_paths(H, W, grid))

        H, W = [int(x) for x in input().split()]

if __name__ == '__main__':
    main()
'''

def find_possible_paths(height, width, data):
    data = list(reversed(data)) # Top row now equals bottom row
    empty = [[0]*width for i in range(height)]

    for i in range(height):
        if not data[i][0]:
            break
        empty[i][0] = 1
    
    for j in range(1, width):
        s = 0
        ss = 0

        for i in range(height):
            if data[i][j]:
                ss += empty[i][j-1]
                continue
            for k in range(s, i):
                empty[k][j] = ss
            s = j + 1
            ss = 0

        for k in range(s, height):
            empty[k][j] = s
        
        print(empty)
        return empty[-1][-1]


    #return


h,w = map(int, input().split())

while h or w:
    grid = [[x == '.' for x in input()] for _ in range(h)]
    print(find_possible_paths(h,w,grid))
    h,w= map(int, input().split())

