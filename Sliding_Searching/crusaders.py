cities, applications = map(int, input().split())
income = list(map(int, input().split()))

visited = [[]]*cities


def binary_search(k, data = visited):
    lo = 0
    hi = len(data)

    #print(data)

    while hi - lo > 1:
        #print(data)
        x = (lo + hi) // 2

        if data[x] == []:
            print(f"Q {x+1}", flush=True)
            data[x] = int(input())

        if k == data[x]:
            return x
        elif k > data[x]:
            lo = x
        else:
            hi = x
    return lo

output = "A"
for i in income:
    output += " " + str(binary_search(i, visited)+1)

print(output)
