N = int(input())
a = [int(i) for i in input().split()]

print()
print("Inputs")
print(N)
print(a)
print()

def build_graph(): 
    g={}
    for i in range(0,N):
        c = [int(a) for a in input().split()]
        if c[0] == 0:
            g[a[i]]=[]
        else:
            for j in range(1,len(c)):
                ci =c[j]
                g[a[ci-1]] = g.get(a[ci-1], []) + [a[i]]
    return g

graph = build_graph()

print(graph)




