
def calculatePossibility(graph, who_owes_who):
    subgraphs = getSubGraphs(graph)

    for subgraph in subgraphs:
        summ = 0
        for person in subgraph:
            summ += who_owes_who[person]

        if summ != 0:
            return False

    return True

def getSubGraphs(graph):
    subgraphs = []
    
    for person in friendship_graph.keys():
        if any(person in sub for sub in subgraphs):
            continue
        
        subgraph = traverse(graph, person, [])
        subgraphs += [subgraph]
    return subgraphs



def traverse(graph, person, l = []):

    if person not in l:
        l.append(person)

    friends_not_in_l = [x for x in friendship_graph[person] if x not in l]

    for i in friends_not_in_l:
        l = traverse(graph, i, l)

    return l


## INPUTS ## 

friends, remaining_friendships = map(int, input().split())

friend_owes = {}
friendship_graph = {}

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

print(friendship_graph)

## Result ## 

# FEIL
"""
5 0
100
-75
-25
-42
42
Blir possible???
"""

if calculatePossibility(friendship_graph, friend_owes):
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")

"""

def bfs(graph, start_node):
    distance = None
    dequeue = [start_node]
    distance[start_node] = 0
    while not dequeue.empty():
        pos = dequeue.popleft()
        for nbr in graph[pos]:
            if distance[nbr] is None:
                distance[nbr] = distance[pos] + 1
                dequeue.addright(nbr)
"""

