# https://github.com/mohsendb7008/Online-Judge-Solutions/blob/6b85b7d093eed5b13ff34dae1087d56d17f6d8b6/Kattis/witchwood.py
N, M, K = map(int, input().split())
result = 0.0

time_prob = []
for i in range(M):
    time, prob = map(float, input().split())
    time_prob.append((time,prob))


for i in range(N):

    # ~~ INF (Største mulige verdi)
    temp = 10**30

    for j in range(M):
        local_cost = (result + time_prob[j][0] + K * time_prob[j][1]) / (1 - time_prob[j][1])
        
        temp = min(temp, local_cost)
    result = temp
    
print(result)