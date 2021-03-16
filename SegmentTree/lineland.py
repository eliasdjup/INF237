
N, K, Q = map(int, input().split())
register = [0]*(N)*2

left = lambda i: 2 * i
right = lambda i: 2 * i + 1
parent = lambda i: i // 2
index = lambda T, i: len(T) // 2 + i


def update(l, r, v, T = register):
    l = index(T,l)
    r = index(T,r)
    T[l] += v

    while True:
        pl = parent(l)
        pr = parent(r)
        if pl == pr:
            return
        if l % 2 == 0:
            T[right(pl)] += v
        if r % 2 == 1:
            T[left(pr)] += v
        l,r = pl, pr

def query(i, T = register):
    s = 0
    i = index(T, i-1)
    while i > 0:
        s += T[i]
        i = parent(i)
    print(s)


for _ in range(K + Q):
    inp = input()

    if inp[0] == '!':
        L, R, D = map(int,inp[1:].split())
        update(L,R,D)

    if inp[0] == '?':
        X = int(inp[1:])
        query(X)

'''
10 1 1
! 0 10 10
? 5




 # Trivial solution
N, K, Q = map(int, input().split())
register = [0]*(N+1)

def update(p):
    L, R, D = map(int,p[1:].split())
    length = R - L
    for i in range(length+1):
        register[L+i] += D


def query(q):
    X = int(q[1:])
    print(register[X])

for _ in range(K + Q):
    inp = input()

    if inp[0] == '!':
        update(inp)
    if inp[0] == '?':
        query(inp)

'''
