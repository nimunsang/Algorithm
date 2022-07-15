from collections import deque
import sys
input = sys.stdin.readline


INF = 10**9
def bellman_ford(start):
    dist = [INF] * (N+1)
    dist[start] = 0
    for i in range(N):
        for v, next_v, cost in graph:
            if dist[next_v] > dist[v] + cost:
                dist[next_v] = dist[v] + cost
                if i == N-1:
                    return True

    return False


TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    graph = []
    for __ in range(M):
        S, E, T = map(int, input().split())
        graph.append((S, E, T))
        graph.append((E, S, T))
    for __ in range(W):
        S, E, T = map(int, input().split())
        graph.append((S, E, -T))

    print("YES" if bellman_ford(1) else "NO")
