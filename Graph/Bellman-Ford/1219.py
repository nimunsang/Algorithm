from collections import deque
import sys
input = sys.stdin.readline
INF = 10**9


def check(v):
    q = deque()
    visited = [0] * N
    for i in negative_cycle:
        visited[i] = 1
        q.append(i)
    while q:
        v = q.popleft()
        if v == E:
            return True
        for next_v in adj_list[v]:
            if not visited[next_v]:
                visited[next_v] = 1
                q.append(next_v)
    return False


def bellman_ford(start):
    dist[start] = -get[start]
    for i in range(N):
        for v, next_v, cost in graph:
            if dist[v] != INF and dist[next_v] > dist[v] + cost - get[next_v]:
                dist[next_v] = dist[v] + cost - get[next_v]
                if i == N-1:
                    negative_cycle.append(v)



N, S, E, M = map(int, input().split())
graph = []
dist = [INF] * N
negative_cycle = []
adj_list = [[] for _ in range(N)]
for _ in range(M):
    s, e, c = map(int, input().split())
    graph.append((s, e, c))
    adj_list[s].append(e)

get = list(map(int, input().split()))

bellman_ford(S)

if dist[E] == INF:
    print("gg")
elif check(S):
    print("Gee")
else:
    print(-dist[E])