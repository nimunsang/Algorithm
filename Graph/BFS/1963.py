from collections import deque
import math

sosu = [1] * 10000
for i in range(2, int(math.sqrt(10000))+1):
    if sosu[i]:
        for j in range(2*i, 10000, i):
            sosu[j] = 0

def bfs(start, end):
    q = deque()
    q.append([start, 0])
    visited = [0] * 10000
    visited[int(start)] = 1
    while q:
        number, cnt = q.popleft()
        if number == end:
            print(cnt)
            break

        for i in range(4):
            for j in range(10):
                if (i == 0 and j == 0) or str(j) == number[i]:
                    continue

                next_number = number[:i] + str(j) + number[i+1:]
                if not visited[int(next_number)] and sosu[int(next_number)]:
                    visited[int(next_number)] = 1
                    q.append([next_number, cnt+1])

    else:
        print("Impossible")


T = int(input())
for _ in range(T):
    a, b = input().rstrip().split()
    bfs(a, b)


