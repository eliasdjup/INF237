#Minimal Independant set

import random

def graphSets(graph):

    # Base cases
    if(len(graph) == 0):
        return []
    if(len(graph) == 1):
        return [list(graph.keys())[0]]
      
    # Selecting vertex
    vCurrent = list(graph.keys())[0]

    # Removing the current vertex from the MIS
    graph2 = dict(graph)
    del graph2[vCurrent]
    
    # Recursive call
    #res1 = graphSets(graph2)
    
    # Deleting neighbours
    for v in graph[vCurrent]:
        if(v in graph2):
            del graph2[v]
    
    # Recursive call without neighbours
    res2 = [vCurrent] + graphSets(graph2)
    
    # Returning the minimal independant set
    #if(len(res1) < len(res2)):
    #    return res1
    return res2
  

cases = int(input())
  
for c in range(cases):
    graph = dict([])
    v = int(input())
    e = []

    unconnected = 0
    for i in range(1,v+1):
        lst = [int(x) for x in input().split()]

        # Handling unconnected nodes
        if lst[0] == 0:
            unconnected +=1
            graph[i] = []
            continue

        for friend in lst[1:]:
            e.append((i,friend))

    # Graph creation
    for i in range(len(e)):
        v1, v2 = e[i]
        
        if(v1 not in graph):
            graph[v1] = []
        if(v2 not in graph):
            graph[v2] = []
        
        graph[v1].append(v2)

    # Testing V raandom combinations with one of the vertexes as nodes, 
    # i found this to give the correct answer, 
    # and did not take as much time as checking all permutations
    ret = []
    for i in range(v*30):
        reslist =[]
        for i in range(1,v+1):
            save = graph.copy()
            tempgraph = dict([])
            tempgraph[i] = graph[i]
            del save[i]


            l = list(save.items())
            random.shuffle(l)
            s = dict(l)
            tempgraph.update(s)
            
            MIS = graphSets(tempgraph)

            reslist.append(len(MIS))
        ret.append(min(reslist))

    print(min(ret))
