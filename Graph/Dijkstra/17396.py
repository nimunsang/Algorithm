import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
A[-1] = 0
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    if A[a] == 1 or A[b] == 1:
        continue

    graph[a].append((t, b))
    graph[b].append((t, a))


def dijkstra(start):
    dist = [float('inf') for _ in range(N)]
    dist[start] = 0
    heap = []
    heapq.heappush(heap, (dist[start], start))
    while heap:
        d, v = heapq.heappop(heap)
        if dist[v] < d:
            continue

        for next_d, next_v in graph[v]:
            if dist[next_v] > d + next_d:
                dist[next_v] = d + next_d
                heapq.heappush(heap, (dist[next_v], next_v))


    print(-1 if dist[-1] == float('inf') else dist[-1])


dijkstra(0)