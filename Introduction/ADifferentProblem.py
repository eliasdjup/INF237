import sys

for line in sys.stdin:
    x, y = map(int, line.split())
    print(abs(x - y))

sys.exit()


"""
while True:
    i = input()
    x, y = map(int, i.split())
    print(abs(x - y))
"""
    
    