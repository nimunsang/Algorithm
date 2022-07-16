import sys
input = sys.stdin.readline
INF = 10**9


N, M = map(int, input().split())
graph = [] * (N+1)
dist = [INF] * (N+1)
for _ in range(M):
    A, B, C = map(int, input().split())
    graph.append((A, B, C))


def bellman_ford(start):
    dist[start] = 0
    for i in range(N):
        for v, next_v, cost in graph:
            if dist[v] != INF and dist[next_v] > dist[v] + cost:
                dist[next_v] = dist[v] + cost
                if i == N-1:
                    return True
    return False


negative_cycle = bellman_ford(1)

if negative_cycle:
    print(-1)
else:
    for i in range(2, N+1):
        print(-1 if dist[i] == INF else dist[i])