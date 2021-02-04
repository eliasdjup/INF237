N = input()
a = input()


def build_graph(N, abs): 

    import networkx as nx

    graph = nx.DiGraph()
    graph.add_edges_from([("root", "a"), ("a", "b"), ("a", "e"), ("b", "c"), ("b", "d"), ("d", "e")])
    print(graph.in_edges("e")) # => [('a', 'e'), ('d', 'e')]
    return graph 


g = build_graph(N,a)