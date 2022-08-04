from math import sqrt
import sys
input = sys.stdin.readline


visited = [0] * 1000001
for i in range(2, int(sqrt(1000001))+1):
    if not visited[i]:
        for j in range(2*i, 1000001, i):
            visited[j] = 1

sosu = []
for i in range(2, 1000001):
    if not visited[i]:
        sosu.append(i)


T = int(input())
for _ in range(T):
    N = int(input())
    start, end = 0, len(sosu)-1
    answer = 0
    while start <= end:
        result = sosu[start] + sosu[end]
        if result == N:
            answer += 1
            start += 1
            end -= 1
        elif result < N:
            start += 1
        else:
            end -= 1

    print(answer)