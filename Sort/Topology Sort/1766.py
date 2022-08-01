import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
heap = []
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    indegree[B] += 1
    graph[A].append(B)

answer = []

for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

while len(answer) != N:
    v = heapq.heappop(heap)
    answer.append(v)

    for next_v in graph[v]:
        indegree[next_v] -= 1
        if indegree[next_v] == 0:
            heapq.heappush(heap, next_v)

print(*answer)



