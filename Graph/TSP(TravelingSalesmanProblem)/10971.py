N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
cost = 10**8


def dfs(v, subtotal, cnt):
    global start, cost
    for next_v in range(N):
        if graph[v][next_v] != 0:
            if not visited[next_v] and subtotal+graph[v][next_v] < cost:
                visited[next_v] = 1
                dfs(next_v, subtotal + graph[v][next_v], cnt+1)
                visited[next_v] = 0
            elif next_v == start and cnt == N:
                cost = min(cost, subtotal + graph[v][next_v])


for i in range(N):
    start = i
    visited[i] = 1
    dfs(i, 0, 1)
    visited[i] = 0

print(cost)