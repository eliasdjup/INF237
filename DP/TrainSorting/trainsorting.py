
N = int(input())

train_order = []
for i in range(N):
    train_order.append(int(input()))


def LIS(data): 
    lis = [0] * len(data)
    lis[0] = 1
    for i in range (1, len(data)):
        for j in range(i):
            if data[j] < data[i]:
                lis[i] = max(lis[i], lis[j] + 1)
    return lis

forward = LIS(train_order)
backwards = list(reversed(LIS(list(reversed(train_order)))))

#print(forward, backwards)

curr_max = 0
for i in range(len(forward)):
    if forward[i] + backwards[i] > curr_max:
        print(i, forward[i], backwards[i])
        curr_max = forward[i] + backwards[i]
print(forward, backwards)
print(curr_max - 2)




##for i in range(len(forward)):


#print(LIS(list(reversed(train_order))))

#print(LIS(train_order) + LIS(list(reversed(train_order))) - 1)


5
2
5
1
4
3
