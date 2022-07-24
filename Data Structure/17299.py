from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
F = Counter(lst)

answer = [0] * N
stack = []
for i in range(N):
    if not stack:
        stack.append(i)
        continue

    while stack and F[lst[stack[-1]]] < F[lst[i]]:
        answer[stack[-1]] = lst[i]
        stack.pop()

    else:
        stack.append(i)

while stack:
    answer[stack[-1]] = -1
    stack.pop()

print(*answer)
