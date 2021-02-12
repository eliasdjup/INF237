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

print(temp)

#Creating the directed graph of nodes
a = {}
for i in range(0,N):
    ctemp = [int(x) for x in input().split()][1:]
    for n in ctemp:
        if n-1 in a:
            a[n-1] = a[n-1]+[i]
        else:
            a[n-1] = [i]



print(a)

def traverse(a):
    