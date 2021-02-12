
#friends, remaining_friendships = map(int, input().split())


'''
for i in range(friends):
    friend_owes[i] = int(input())

for _ in range(remaining_friendships):
    x, y = map(int, input().split())

    friends = friendship_graph.get(x, [])
    friends.append(y)
    friendship_graph[x] = friends

    friends = friendship_graph.get(y, [])
    friends.append(x)
    friendship_graph[y] = friends


friend_owes = {}
friendship_graph = {}
'''
#friends, remaining_friendships = map(int, input().split())

#print(friendship_graph)


friends, remaining_friendships = map(int, input().split())
friend_owes = {}
graph = {}
for i in range(friends):
    friend_owes[i] = int(input())
for i in range(remaining_friendships):
    x, y = map(int, input().split())
    graph[x] = graph.get(x, []) + [y]
    graph[y] = graph.get(y, []) + [x]


def dfs(current_node, visited, graph, reachable_nodes = []):
    if current_node not in visited:
        reachable_nodes.append(current_node)
        visited.add(current_node)
        for neighbour in graph[current_node]:
            dfs(neighbour, visited, graph, reachable_nodes)
    return reachable_nodes


def calc(graph, friends):
    visited = set()

    for i in range(friends):
        if i not in graph.keys():
            if friend_owes[i] != 0:
                print("IMPOSSIBLE")
                return
            continue


        curr = dfs(i,visited,graph,[])
        if curr:
            if not sum([friend_owes[x] for x in curr]) == 0:
                print("IMPOSSIBLE")
                return
    print('POSSIBLE')


calc(graph, friends)

'''
2 0
100
-42


'''

