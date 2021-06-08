import math

def prime(num):
    if (num <= 1):
        return False
    elif (num == 2):
        return True
    else:
        for x in range(2,int(math.sqrt(num)) + 1):
            if(num % x == 0):
                return False
        return True  

def displayfraction(delim, denom):
    if delim == 0:
        denom = 1

    elif delim == denom:
        delim = 1
        denom = 1

    elif delim == 2 and denom == 4:
        delim = 1
        denom = 2

    print(str(delim) + "/" + str(denom))

T = int(input())
for i in range(T):
    count = 0
    denominator = 0
    case = input()
    for i in [2, 8, 10, 16]:
        try:
            num = int(case, i)
            denominator += 1
            if prime(num):
                count += 1
        except ValueError:
            continue
    displayfraction(count, denominator)
