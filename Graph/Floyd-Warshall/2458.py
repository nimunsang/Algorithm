import sys
input = sys.stdin.readline


N, M = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1


def floyd_warshall():
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1


floyd_warshall()


ans = [0] * (N+1)
for i in range(1, N+1):
    for j in range(1, N+1):
        ans[i] += graph[i][j]
        ans[j] += graph[i][j]

print(ans.count(N-1))
