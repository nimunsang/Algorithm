from itertools import permutations

import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
visited = [0]*(N+1)


p = permutations(range(1, 4+1), 4)

for a in p:
    print(*a)







