from sys import stdin

iterator = iter(stdin.readlines())
history = []
case = 0

while True:
    try:
        local_history = []
        m, n = map(int, next(iterator).split())
        local_history.append((m,n))

        for inp in range(n):
            a,b =  map(int, next(iterator).split())
            local_history.append((a,b))
        
        history.append(local_history)
        case += 1

    except StopIteration:
        break

def dfs(current_node, visited, graph):
    stack = [current_node]
    while len(stack) != 0:
        current = stack.pop()

        if current in visited:
            continue

        visited.append(current)

        for neighbour in graph[current]:
            if neighbour not in visited:
                stack.append(neighbour)

    return visited

def checkValidity(graph, locations):
        all_routes = [dfs(x, list(), graph) for x in range(locations)]
        success = True
        for route in all_routes:
            if len(route) != locations: # Are all locations reachable?
                success = False
        return success

def toGraph(graph_list):
    graph = {}
    m,n = graph_list[0]
    for i in range(m):
        graph[i] = []
    for (a,b) in graph_list[1:]:
        lst = graph[a]
        lst.append(b)
        graph[a] = lst
    return graph

def calc(history):
    for casenum, case_history in enumerate(history):

        case_graph = toGraph(case_history)
        valid = checkValidity(case_graph, case_history[0][0])
        if valid:
            print(f"Case {casenum + 1}: valid")
        else:
            m,n = case_history[0]

            for idx, (a,b) in enumerate(case_history[1:]):
                case_history[idx+1] = (b,a)
                valid = checkValidity(toGraph(case_history), m)
                if valid:
                    print(f"Case {casenum + 1}: {a} {b}")
                    break
                case_history[idx+1] = (a,b)
        
            if not valid:
                print(f"Case {casenum + 1}: Invalid")

calc(history)