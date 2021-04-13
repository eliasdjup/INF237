def is_possible(color_matrix):

    l = [x for x in range(num_vertices) if color_matrix[x] == -1]
    current = -1 if len(l) == 0 else l[0]

    if current == -1:
        return True

    s = set(color_matrix[i] for i in adj[current] if color_matrix[i] != -1)
    possible_colors = [x for x in range(num_colors) if x not in s]

    for color_id in possible_colors:
        color_matrix[current] = color_id

        if is_possible(color_matrix):
            return True

        color_matrix[current] = -1
    return False

num_vertices = int(input())   # 2 <= num_vertices <= 11
adj = [[]] * num_vertices     # indices: [0, ..., 10(at most)] 
num_colors = 1
iterate = True

for vertex in range(num_vertices):
    adj[vertex] = [int(x) for x in input().split()]

while iterate:
    num_colors += 1
    
    color_matrix            = [-1] * num_vertices
    color_matrix[0]         = 0
    color_matrix[adj[0][0]] = 1

    iterate = not is_possible(color_matrix)

print(num_colors)

