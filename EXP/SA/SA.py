def graphSets(graph):

    if(len(graph) == 0):
        return []
     
    if(len(graph) == 1):
        return [list(graph.keys())[0]]
      
    vCurrent = list(graph.keys())[0]
      
    graph2 = dict(graph)

    del graph2[vCurrent]
      
    res1 = graphSets(graph2)
      
    for v in graph[vCurrent]:
          
        if(v in graph2):
            del graph2[v]
      

    res2 = [vCurrent] + graphSets(graph2)
      
    if(len(res1) > len(res2)):
        return res1
    return res2
  

cases = int(input())
  
for c in range(cases):
    users = int(input())

    edges = []

    for i in range(1,users+1):
        lst = [int(x) for x in input().split()]

        for friend in lst[1:]:
            edges.append((i,friend))



  
graph = dict([])
  

for i in range(len(edges)):
    v1, v2 = edges[i]
      
    if(v1 not in graph):
        graph[v1] = []
    if(v2 not in graph):
        graph[v2] = []
      
    graph[v1].append(v2)
    graph[v2].append(v1)
  

MIS = graphSets(graph)
  
for res in MIS: print(res)