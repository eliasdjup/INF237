from itertools import product as iter_product
n = 6
board = []

for _ in range(n):
    line = input().split()
    line = list(map(lambda s: s.replace('-', '0'), line))
    line = [ [int(x[0]),int(x[2])] if len(x) > 1 else [int(x)] for x in line]
    board.append(line)

def checknum(h, w, i, board, ints = range(1,10)):
    for num in ints:
        if possible(board, num, h, w, i):
            board[h][w][i] = num
            if backtracking(board):
                return True
            else:
                board[h][w][i] = 0
    return False

def backtracking(board):
    for h, w in iter_product(range(n), range(n)):
        for i in range(len(board[h][w])):
            if board[h][w][i] != 0: continue
            return checknum(h, w, i, board)
    return True


def getboxcoords(h, w):
    return (h//2)*2, (w//3)*3

def checksize(board, h, w, num, i):
    if len(board[h][w]) == 2:
        this, other = i,  1 - i
        if other < this and board[h][w][other] >= num:
            return False
        elif other > this and board[h][w][other] != 0 and board[h][w][other] <= num:
            return False

def possible(board, num, h, w, i):

    if checksize(board, h, w, num, i) == False:
        return False

    for k in range(6):
        if k != h and num in board[k][w]: return False
        if k != w and num in board[h][k]: return False

    bh, bw = getboxcoords(h, w)
    for k, j in iter_product(range(2), range(3)):
        if not (bh + k, bw + j) == (h, w) and num in board[bh+k][bw+j]:
            return False

    return True


backtracking(board)
b = []
for line in board:
    s = []
    for cell in line:
        s.append('/'.join(map(str, cell)))
    b.append(" ".join(s))
print('\n'.join(b))

'''
def findplacement(board, h, w, secondary = False):
    ints = range(1,10)
    cell = board[h][w]

    found_first = False
    ns = []
    for n in ints:
        if can_place(n,h,w,0,board):
            ns.append(n)
            found_first = True
            continue
        
        if found_first and can_place(n,h,w,1,board):
            ns.append(n)
            break
    return ns



def depthfirst(board, boardsize):
    for h, w in iter_product(range(boardsize), range(boardsize)):
        sec = True if len(board[h][w]) > 1 else False
        ns = findplacement(board, h, w, sec)

        if ns == []: return False
        old_value = board[h][w]
        board[h][w] = ns
        
        if depthfirst(board, boardsize): return True

        board[h][w] = old_value
    return True #(?)

def can_place(*x):
    pass

        #if len(board[h][w]) == 1:

print(depthfirst(board, 6))




'''




