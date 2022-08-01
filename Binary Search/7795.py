from bisect import bisect_left, bisect_right

import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    answer = 0
    idx = 0
    for a in A:
        while idx < len(B) and a > B[idx]:
            idx += 1
        answer += idx

    print(answer)
