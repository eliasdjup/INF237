
def leftturn(x,y):
    pass

def graham(points):
    points = sorted(set(points))
    S, hull = [], [] # S is a stack of points
    for p in points:
        while len(S) >= 2 and leftturn(S[-2], S[-1], p):
            S.pop()
        S.append(p)
    hull += S
    S = []
    for p in reversed(points):
        while len(S) >= 2 and leftturn(S[-2], S[-1], p):
            S.pop()
        S.append(p)
    hull += S[1:-1]

def compare(u, v):
    if u[0] > 0 and v[0] < 0:
        return 

def calc(points):
    pass

test_cases = int(input())
for _ in range(test_cases):
    case = list(map(int, input().split()))
    points_n = case[0]
    points = [ (case[i], case[i+1]) for i in range(1, points_n*2, 2)]



    calc(points)

