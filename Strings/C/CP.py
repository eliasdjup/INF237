
def kmp(text, pattern, lps):
    n, k = len(text), len(pattern)
    txt_idx, pat_idx = 0, 0

    while txt_idx < n:
        if pattern[pat_idx] == text[txt_idx]:
            txt_idx += 1
            pat_idx += 1

        if pat_idx == k:
            yield txt_idx - k
            pat_idx = lps[pat_idx - 1]

        elif txt_idx < n and pattern[pat_idx] != text[txt_idx]:
            if pat_idx != 0:
                pat_idx = lps[pat_idx - 1]

            else:
                txt_idx += 1 

def longest_prefix_suffix(pattern):
    n, k = 0, len(pattern)
    lps = [0] * k
    idx = 1
    while idx < k:
        if pattern[idx] == pattern[n]:
            n += 1
            lps[idx] = n
            idx += 1
        else:
            if n != 0:
                n = lps[n - 1]
            else:
                lps[idx] = 0
                idx += 1
    return lps

def getAngles(n, first, second, MAX = 360000):
    first_angles = []
    second_angles = []

    first_sorted = sorted(first)
    second_sorted = sorted(second)

    for i in range(1, n):
        first_angle = first_sorted[i] - first_sorted[i-1]
        second_angle = second_sorted[i] - second_sorted[i-1]

        first_angles.append(first_angle)
        second_angles.append(second_angle)
    
    first_angles.append((MAX - first_sorted[n-1]) + first_sorted[0])
    second_angles.append((MAX - second_sorted[n-1]) + second_sorted[0])

    return first_angles, second_angles


n = int(input())
first = list(int(x) for x in input().split())
second = list(int(x) for x in input().split())

first_angles, second_angles = getAngles(n,first,second)
lps = list(kmp(first_angles+first_angles, second_angles, longest_prefix_suffix(second_angles)))

if lps == []:
    print("impossible")
else:
    print("possible")
