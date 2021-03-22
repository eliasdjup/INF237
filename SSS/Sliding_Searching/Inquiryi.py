
ints = int(input())

prefix_list = []
square_sums = []
acc         = 0
acc_squares = 0
for _ in range(ints):
    inp = int(input())

    acc += inp
    acc_squares += inp**2
    prefix_list.append(acc)
    square_sums.append(acc_squares)

maxi = 0
for i in range(ints):
    maxi = max(maxi, square_sums[i] * (acc - prefix_list[i]))

print(maxi)

'''
# Sliding
acc = 0
maximum = 0
for i in range(ints):
    print("before", len(int_list))
    elem = int_list.pop(0)
    print("after", len(int_list))
    acc += elem**2
    maximum = max(maximum, acc * sum(int_list))
print(maximum)



# Trivial
maximum = 0
for i in range(ints+1):
    #print(int_list[i:], int_list[:i])
    left = [x**2 for x in int_list[:i]]
    right = int_list[i:]

    maximum = max(maximum, sum(left) *sum(right))

print(maximum)

'''