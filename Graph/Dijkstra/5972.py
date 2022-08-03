import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])


def dijkstra(start, end):
    dist = [float('inf') for _ in range(N+1)]
    dist[start] = 0
    heap = []
    heapq.heappush(heap, [dist[start], start])
    while heap:
        d, v = heapq.heappop(heap)
        for next_d, next_v, in graph[v]:
            if dist[next_v] > d + next_d:
                dist[next_v] = d + next_d
                heapq.heappush(heap, [dist[next_v], next_v])

    print(dist[end])


dijkstra(1, N)