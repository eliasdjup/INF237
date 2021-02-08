
def calc(graph, dept, friends_num):
    visited = set()

    for friend in range(friends_num):
        if friend in visited:
            continue

        if friend not in graph.keys():
            if dept[friend] != 0:
                return False
            continue


        component_sum = 0
        stack = [friend]
        while len(stack) != 0:
            current = stack.pop()

            if current in visited:
                continue

            visited.add(current)
            component_sum += dept[current]

            for neighbour in graph[current]:
                if neighbour not in visited:
                    stack.append(neighbour)

        if component_sum != 0:
            return False

    return True

friends_num, remaining = map(int, input().split())

dept = []
for _ in range(friends_num):
    dept.append(int(input()))

graph = {}
for _ in range(remaining):
    x,y = map(int, input().split())

    friends = graph.get(x, [])
    friends.append(y)
    graph[x] = friends

    friends = graph.get(y, [])
    friends.append(x)
    graph[y] = friends

if calc(graph, dept, friends_num):
    print ("POSSIBLE")
else:
    print ("IMPOSSIBLE")
