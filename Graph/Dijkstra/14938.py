import heapq
import sys
input = sys.stdin.readline


def dijkstra(v):
    dist = [float('inf')] * (n+1)
    visited = [0] * (n+1)
    dist[v] = 0
    heap = []
    heapq.heappush(heap, [dist[v], v])
    while heap:
        d, v = heapq.heappop(heap)
        visited[v] = 1
        for next_d, next_v in graph[v]:
            if d + next_d > m:
                continue

            if dist[next_v] > d + next_d:
                dist[next_v] = d + next_d
                heapq.heappush(heap, [dist[next_v], next_v])

    cnt = 0
    for i in range(1, n+1):
        if visited[i]:
           cnt += items[i]

    return cnt


n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
items = [0] + list(map(int, input().split()))
for __ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append([l, b])
    graph[b].append([l, a])

answer = 0
for i in range(1, n+1):
    answer = max(answer, dijkstra(i))

print(answer)