
def add_edge(a,b, graph):
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

def create_graph(n, m):
    graph = [[] for x in range(n)]
    for _ in range(m): # Create graph
        a, b = map(int, input().split())
        add_edge(a,b,graph)

    return graph

def try_match(previous_matchings, new_matching, matches, graph):
    if new_matching not in matches: return True
    potential = matches[new_matching]
    previous_matchings[new_matching] = True

    for neighbor in graph[potential]:
        if (not previous_matchings[neighbor] and 
                try_match(previous_matchings, neighbor, matches, graph)):
            matches[neighbor] = potential
            return True
    return False

def calc(n, graph):
    matches = {}
    for i in range(n):
        previous_matchings = [False] * n
        for j in graph[i]:
            if (try_match(previous_matchings, j, matches, graph)):
                matches[j] = i
                break
    return matches

def main():
    n, m = map(int, input().split())
    graph = create_graph(n, m)
    matches = calc(n, graph)

    if len(matches) != n:
        print("Impossible")
    else:
        for i in range(n):
            print(matches[i]+1)

if __name__ == '__main__':
    main()