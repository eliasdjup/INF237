q = int(input())

store = None
res = 0

for i in range(q):
    if (store == None):
        store = input()
    else:
        if (input() == store):
            res+=1

print(res)

