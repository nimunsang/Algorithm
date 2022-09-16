import heapq
import sys
input = sys.stdin.readline


def dijkstra(v):
    heap = []
    dist = [float('inf') for _ in range(N+1)]
    dist[v] = 0
    heapq.heappush(heap, (dist[v], v))
    while heap:
        d, v = heapq.heappop(heap)
        if dist[v] < d:
            continue

        for next_d, next_v in graph[v]:
            if dist[next_v] > d + next_d:
                dist[next_v] = d + next_d
                heapq.heappush(heap, (dist[next_v], next_v))

    return dist


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append([c, b])
        graph[b].append([c, a])

    K = int(input())
    lst = list(map(int, input().split()))
    subtotal = []
    for friend in lst:
        subtotal.append(dijkstra(friend))

    answer = sys.maxsize
    idx = 0
    for i, v in enumerate(list(map(sum, list(zip(*subtotal))))):
        if answer > v:
            answer = v
            idx = i

    print(idx)
