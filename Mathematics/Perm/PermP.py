
def genFactorials(n):
    fac = [1] * n
    for i in range(2, n):
        fac[i] = i * fac[i-1]
    return fac

def main():
    while True:
        try:
            n, k = map(int, input().split())
            nums = list(range(1,n+1))
            perm = []
            while n > 0:
                n -= 1
                q = k // fac[n]
                perm.append(nums[q])
                nums.pop(q)
                k %= fac[n]

            print(*(map(str,perm)))
        except EOFError:
            exit()

if __name__ == '__main__':
    fac = genFactorials(50)
    main()
