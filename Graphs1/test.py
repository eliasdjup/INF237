

g = {0: [1, 2], 1: [3], 2: [3, 4], 3: [5], 4: [5], 5: []}

path = list()
#print(dfs(0, path, g, 5))



def dfsnonrec(start, end, g):
    path = []
    stack = [(start, path)]
    paths = []
    while len(stack) != 0:
        current, currentpath = stack.pop()

        print(current, currentpath)
        
        if current in currentpath:
            continue
        currentpath.append(current)

        if (current == end):
            paths.append(currentpath)
            continue

        for neighbour in g[current]:
            if neighbour not in currentpath:
                stack.append((neighbour, currentpath.copy()))

    return paths


print(dfsnonrec(0, 5, g))
