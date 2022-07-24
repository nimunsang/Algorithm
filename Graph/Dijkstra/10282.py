import heapq
import sys
input = sys.stdin.readline


def dijkstra(v):
    dist = [float('inf')] * (n+1)
    dist[v] = 0
    heap = []
    heapq.heappush(heap, [dist[v], v])
    while heap:
        d, v = heapq.heappop(heap)
        for next_d, next_v in graph[v]:
            if dist[next_v] > d + next_d:
                dist[next_v] = d + next_d
                heapq.heappush(heap, [dist[next_v], next_v])

    return dist


T = int(input())
for _ in range(T):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for __ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append([s, a])

    dist = dijkstra(c)

    cnt, tim = 0, 0
    for i in range(1, n+1):
        if dist[i] == float('inf'):
            continue
        cnt += 1
        if dist[i] > tim:
            tim = dist[i]

    print(cnt, tim)
