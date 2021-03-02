
n, m, k = map(int, input().split())

time_prob = []
for i in range(m):
    time, prob = map(float, input().split())
    time_prob.append((time,prob))

result = 0.0

# Loop over logs for out cabin
for i in range(n):

    # Initial (Du kan sikkert endre denne til noe stort også loope over alle m under)
    temp = (result + time_prob[0][0] + k * time_prob[0][1]) / (1 - time_prob[0][1])

    # Loop over locations
    for j in range(1, m):
        loc_cost = (result + time_prob[j][0] + k * time_prob[j][1]) / (1 - time_prob[j][1])
        temp = min(temp, loc_cost)
    result = temp
    
print(result)