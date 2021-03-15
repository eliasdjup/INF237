def update(BIT, i, val):
    while i < len(BIT):
        print(i)
        BIT[i] += val
        i += -i & i



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