from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
indegree = {i : 0 for i in range(1, N+1)}
graph = [[] for _ in range(N+1)]
for _ in range(M):
    inp = list(map(int, input().split()))
    for i in range(1, inp[0]):
        graph[inp[i]].append(inp[i+1])
        indegree[inp[i+1]] += 1


def topology_sort():
    q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        x = q.popleft()
        answer.append(x)

        for next_x in graph[x]:
            indegree[next_x] -= 1
            if indegree[next_x] == 0:
                q.append(next_x)


answer = []
topology_sort()

if len(answer) == N:
    for a in answer:
        print(a)
else:
    print(0)
