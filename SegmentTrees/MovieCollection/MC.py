def update(BIT, i, val, op=sum)):
    BIT[i] = val
    while (i := parent(i)) > 0:
        BIT[i] = op((BIT[left(idx)],BIT[right(idx)]))


def fill(BIT, op=sum):
    internal = range(1, len(tree) // 2)
    for idx in reversed(internal): # internal nodes backwards
    tree[idx] = op((tree[left(idx)],
    tree[right(idx)]))



cases = int(input())

for c in range(cases):
    m,r = [int(x) for x in input().split()]

    collection = [0]*(m+1)
    BIT = [0]*15

    for i in range(1,m):
        update(BIT, i, 1)
        collection[i] = m- i + 1




    movies = [int(x) for x in input().split()]
    c = m
    for m in movies:
        c+=1
        t = 0
        
        index = collection[m]

        while index > 0:
            t += BIT[index]
            index -= -index & index

        update(BIT, collection[m], -1)
        collection[m] = c
        update(BIT, collection[m], 1)
        print(m - t + " ")