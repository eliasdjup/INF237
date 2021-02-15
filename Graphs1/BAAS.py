#Initial setup
N = int(input())
values = [int(i) for i in input().split()]

#Creating the directed graph of nodes
a = {}
for i in range(0,N):
    ctemp = [int(x) for x in input().split()][1:]
    for n in ctemp:
        if n-1 in a:
            a[n-1] = a[n-1]+[i]
        else:
            a[n-1] = [i]
a[N-1]=[]

#Finding paths from root to end node
def traverse(a):
    path = []
    stack = [(0, path)]
    paths = []
    while len(stack) != 0:
        current, currentpath = stack.pop()
        
        if current in currentpath:
            continue
        currentpath.append(current)

        if (current == N-1):
            paths.append(currentpath)
            continue

        for neighbour in a[current]:
            if neighbour not in currentpath:
                stack.append((neighbour, currentpath.copy()))

    return paths

t = traverse(a)

#Finding the values of the paths
def path_sum(paths, values):
    return [sum([values[i] for i in l]) for l in paths]

#The node to be changed to 0 is in the path of maximum sum
slist = path_sum(t,values)
m = slist.index(max(slist))

max_path = t[m]

#Changing all nodes in the path of maximum sum to 0, to see what node should be changed to create the path of overall minimum value
def node_to_zero():
    res = sum(values)
    for i in range(len(max_path)):
        valuescopy = values.copy()
        valuescopy[i] = 0
        ps = max(path_sum(t,valuescopy))
        if ps < res:
            res = ps
    
    return res

print(node_to_zero())