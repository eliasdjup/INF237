class Node:
    def __init__(self, id, value, c):
        self.id = id
        self.value = value
        self.c = c
    def __repr__(self):
        return "Node(id:"+str(self.id)+",value:"+str(self.value)+",connected_to"+str(self.c)+")"
    def __str__(self):
        return "Node(id:"+str(self.id)+",value:"+str(self.value)+",connected_to"+str(self.c)+")"

#Initial setup
N = int(input())
temp = [int(i) for i in input().split()]


#Creating the directed graph of nodes
a = {}
for i in range(0,N):
    ctemp = [int(x) for x in input().split()]
    if ctemp[0]==0:
        a[i] = Node(i,temp[i],[])
    else:
        c = [x-1 for x in ctemp[1:][:]]
        a[i] = Node(i,temp[i],c)

#Finding the paths from root to tail
paths=[]
def traverse(a, n, store):
    if n.c == []:
        paths.append(store+[n.id])
        return
    else:
        for j in n.c:
            t = store+[n.id]
            traverse(a, a[j],t)

traverse(a, a[N-1], [])

#Finding the path with the highest sum. The node to be changed to 0, must be a part of this path
def get_max_path(paths):
    s=[sum(x) for x in [[a[b].value for b in k] for k in paths]]
    return paths[s.index(max(s))]

#Finally, replacing all nodes in the maximum value path with 0, to see what node should be changed to create the path of minimum value
res=999999999999999999
for i in get_max_path(paths):
    atemp = a.copy()
    atemp[i] = Node(i,0,atemp[i].c)
    paths=[]
    traverse(atemp,atemp[N-1],[])
    s=max([sum(x) for x in [[atemp[b].value for b in k] for k in paths]])
    if s < res:
        res = s

print(res)