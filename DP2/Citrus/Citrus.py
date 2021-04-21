import math

# initialize lists
N = int(input())
subs = [[] for _ in range(N)]
is_root = [True] * N
under = [0]*N
over = [0]*N
costs = []

def solve(employee):
    d = math.inf

    if not subs[employee]:
        under[employee] = math.inf
        return

    for n in subs[employee]:
        solve(n)
        costs[employee] = costs[employee] + over[n]

        cost = costs[n] if costs[n] < under[n] else under[n]
        over[employee] = over[employee] + cost
        under[employee] = under[employee] + cost

        lower_bounds = max(costs[n] - under[n], 0)
        d = lower_bounds if lower_bounds < d else d
    
    under[employee] = under[employee] + d


for i in range(N):
    l_in = list(map(int, input().split()))
    Ci, Ui, i_subs = l_in[0], l_in[1], l_in[2:]
    costs.append(Ci)
    
    if Ui == 0: continue
    for k in range(Ui):
        subs[i].append(i_subs[k])
        is_root[i_subs[k]] = False # Subordinates are not root

boss = is_root.index(True)
solve(boss) # Solve based on the root/boss
print(under[boss] if under[boss] < costs[boss] else costs[boss])