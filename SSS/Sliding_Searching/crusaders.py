'''
cities, applications = map(int, input().split())
income = list(map(int, input().split()))

visited = [[]]*cities


def binary_search(k, data = visited):
    lo = 0
    hi = cities-1
    returnval = 0

    while hi - lo >= 0:
        x = (lo + hi) // 2

        if visited[x] is None:
            print(f"Q {x+1}", flush=True)
            visited[x] = int(input())

        if k == visited[x]:
            return x
        elif k > visited[x]:
            if visited[x] > returnval:
                returnval = x
            lo = x + 1
        else:
            hi = x - 1
    return returnval

output = "A"
for i in income:
    output += " " + str(binary_search(i, visited)+1)

print(output)
exit()
'''
cities, _ = map(int, input().split())
income = list(map(int, input().split()))

visited = [None]*cities
visited[0] = -1


def binary_search(k):
    lo = 0
    hi = cities-1
    returnvalue = 0

    while hi - lo >= 0:
        x = (lo + hi) // 2

        if visited[x] is None:
            print(f"Q {x+1}", flush=True)
            visited[x] = int(input())

        if k == visited[x]:
            return x
        elif k > visited[x]:
            if visited[x] > returnvalue:
                returnvalue = x
            lo = x + 1
        else:
            hi = x - 1
    return returnvalue

output = "A"
for i in income:
    output += " " + str(binary_search(i) + 1)

print(output)
