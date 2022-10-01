import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [0] * N


def dfs(v, depth):
    global answer
    if depth == 5:
        answer = 1
        return

    for next_v in graph[v]:
        if not visited[next_v]:
            visited[next_v] = 1
            dfs(next_v, depth + 1)
            visited[next_v] = 0



answer = 0
for i in range(N):
    visited[i] = 1
    dfs(i, 1)
    visited[i] = 0
    if answer:
        break

print(answer)