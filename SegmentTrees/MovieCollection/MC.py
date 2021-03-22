# Binary indexed tree
class BIT:
    def __init__(self, size):     
        self.size = size
        self.tree = [0 for i in range(self.size+1)]
            
    def update(self, index, val):
        index = index+1
        while index <= self.size:
            self.tree[index] += val
            index += index & (-index)
    
    def getSum(self, index):
        s = 0
        index = index+1

        while index > 0:
            s += self.tree[index]
            index -= index & (-index) 

        return s

    def getSumRange(self,a,b):
        return self.getSum(b) - self.getSum(a-1)

    def __repr__(self):
        return ("BIT:"+str(self.tree))


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