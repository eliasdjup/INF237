# Iterative function to find the longest decreasing subsequence of a given list
def LDS(A):
    
    n = len(A)
    memory = [1]*n 
 
    # start from the second element in the list
    for i in range(1, len(A)):
        # do for each element in sublist `A[0…i-1]`
        for j in range(i):
            # find longest decreasing subsequence that ends with `A[j]`
            # where `A[j]` is more than the current element `A[i]`
            if A[i] < A[j] and memory[i]< memory[j] + 1:
                memory[i] = memory[j]+1

    count = 0
    for i in range(n): 
        count = max(memory[i], count) 
    # print LDS
    print(count)
 
 
if __name__ == '__main__':
 
    A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    LDS(A)