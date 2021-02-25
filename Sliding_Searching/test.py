
def binary_search(k, data):
    pre = None
    lo = 0
    hi = len(data)-1
    while hi - lo > 1:
        x = (lo + hi) // 2

        if data[x] == []:
            print(f"Q {x}", flush=True)
            data[x] = int(input())

        if  k > data[x]:
            lo = x
        else:
            hi = x
    return lo

print(binary_search(2, [[],[],[],[],[],[]]))

