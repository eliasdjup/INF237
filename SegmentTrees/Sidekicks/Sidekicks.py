# Binary indexed tree
class BIT:
    def __init__(self, size):     
        self.size = size
        self.tree = [0 for i in range(self.size+1)]
 
    def get_sum(self, j):
        s = 0
        while j > 0:
            s += self.tree[j-1]
            j -= j & (-j)
        return s

    def get_sum_range(self,a,b):
        #print(a,b)
        return self.get_sum(b) - self.get_sum(a-1)

    def update(self, j, val):
        diff = val - self.tree[i]
        self.tree[i] = val
        i += 1
        while i < (self.size+1):
            self.aux[i] += diff
            i += i & -i
    
    def update(self, j, val):                    
        while j <= self.size:
            self.tree[j] += val 
            j += j & (-j)  

    def __repr__(self):
        return "BIT("+str(self.tree)+")"
    
    
n,q = [int(x) for x in input().split()]
gem_values = [int(x) for x in input().split()]
gems = [int(x)for x in input().split(sep=None)[0]]

print(n,q)
print(gem_values)
print(gems)


trees = []
for i in range(6):
    trees.append(BIT(n + 1))

for i in range(0,n-1):
    print(i)
    trees[gems[i]-1].update(i,1)

for _ in range(q):
    i, a, b = [int(x) for x in input().split()]
    print(i,a,b)

    if i == 1:
        trees[gems[a - 1] - 1].update(a - 1, -1)
        gems[a - 1] = 0 + b
        trees[gems[a - 1] - 1].update(a - 1, 1)

    elif i == 2:
        gem_values[a - 1] = b

    else:
        res = 0
        for j in range(0,5):
            res += trees[j].get_sum_range(a-1, b-1) * gem_values[j]
        print(res)
