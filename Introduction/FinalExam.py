
import sys

questions = int(input())

previous =  None
count = 0

for i in range(questions):
    answer = input()
    if answer == previous:
        count += 1
    previous = answer

print(count)

sys.exit()

# Eksempler i første forelesning fra 57 min
# ctrl-D (Key for exiting a stream! Brukes med stdin)

""" Eksempel
import sys

sys.stdin.readline()
for x in map(int, sys.stdin):
    print(x, "is", "even" if x % 2 == 0 else "odd")

"""

# Always use long long (Not int!)




