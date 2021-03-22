
class BinaryIndexedTree:
    def __init__(self, treesize):     
        self.treesize = treesize
        self.tree = [0 for i in range(self.treesize+1)]
    
    def sumrange(self,a,b):
        return self.sum(b) - self.sum(a-1)

    def sum(self, i):
        s = 0
        i = i+1
        while i > 0:
            s += self.tree[i]
            i -= self.bitwise_and(i)
        return s

    def update(self, i, val):
        while i <= self.treesize:
            self.tree[i] += val
            i += self.bitwise_and(i)

    def bitwise_and(self, x):
        return x & -x

if __name__ == '__main__':

    n_gems = 6
    bit_trees=[]
    N, Q = map(int, input().split())
    values = list(map(int, input().split()))
    gems = list(map(int, input().split(sep=None)[0]))


    for i in range(n_gems): # Construct and store one tree for each gem
        bit_trees.append(BinaryIndexedTree(N+1))

    for i in range(N):
        bit_trees[gems[i]-1].update(i+1,1)

    for _ in range(Q):

        result = 0
        i, K, P = map(int, input().split())

        if i == 1: # Replace
            bit_trees[gems[K-1]-1].update(K, -1)
            gems[K-1] = P
            bit_trees[gems[K-1]-1].update(K, 1)
        elif i == 2: # Revalue
            values[K-1] = P
        else: # Query price
            print(sum([(bit_trees[j].sumrange(K-1, P-1)) * values[j] for j in range(n_gems)]))
