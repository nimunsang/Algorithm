import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


N, R, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(v, depth):
    for next_v in graph[v]:
        if not visited[next_v]:
            visited[next_v] = 1
            dfs(next_v, depth + 1)
            cnt[v] += cnt[next_v]


cnt = [1] * (N+1)
visited = [0] * (N+1)
visited[R] = 1
dfs(R, 0)

for _ in range(Q):
    u = int(input())
    print(cnt[u])