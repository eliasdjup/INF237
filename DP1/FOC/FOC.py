from sys import stdin
import itertools

iterator = iter(stdin.readlines())
maps=[]

# Input
while True:
    try:
        local= []
        x, y = map(int, next(iterator).split())
        for i in range(x):
            #l = next(iterator).split(sep=None)[0]
            local.append(next(iterator).split(sep=None)[0])
        maps.append([[x,y],local])
    except StopIteration:
        break

for m in maps:
    if m[1] == []:
        continue
    x,y = m[0]
    m = m[1]
    print(x,y)
    print(m)


    


'''

opt = defaultdict(int) # <- cool
for x in reversed(range(1, N)): # going right to left
for y in range(1, M):
rval = max(
opt[(x + 1, y + 1)], # right and up
opt[(x + 1, y )], # right and straight
opt[(x + 1, y - 1)], # right and down
)
opt[(x, y)] = data[x][y] + rval
print(max(opt[1, y] for y in range(M)))
'''