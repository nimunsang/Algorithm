import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])


def dijkstra(start):
    heap = []
    dist = [float('inf') for _ in range(N+1)]
    dist[start] = 0
    heapq.heappush(heap, [dist[start], start])
    while heap:
        d, v = heapq.heappop(heap)
        for next_d, next_v in graph[v]:
            if dist[next_v] > d + next_d:
                answer[start-1][next_v-1] = answer[start-1][v-1] + [next_v]
                dist[next_v] = d + next_d
                heapq.heappush(heap, [dist[next_v], next_v])



answer = [[[] for _ in range(N)] for __ in range(N)]

for v in range(1, N+1):
    dijkstra(v)


for i in range(N):
    for j in range(N):
        if i == j:
            answer[i][j] = '-'
        else:
            answer[i][j] = answer[i][j][0]

for a in answer:
    print(*a)