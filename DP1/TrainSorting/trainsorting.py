

N = int(input())

train_order = []
for x in range(N):
    train_order.append(int(input()))
train_order = train_order[::-1]

def LIS():
    for i in range (1, N): 
        for j in range(i): 
            if forward[i] < forward[j]+1 and train_order[i] > train_order[j]:
                forward[i] = forward[j] + 1
            
            if backward[i] < backward[j]+1 and train_order[i] < train_order[j]:
                backward[i] = backward[j] + 1


if __name__ == '__main__':
    forward = [1]*N
    backward = [1]*N
    LIS()

    res=0
    if len(train_order) == 0:
        res = 1

    for i in range(N):
        res = max((forward[i] + backward[i]), res)

    print(res-1)


