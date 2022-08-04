import sys
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [0] * 1000001
K = min(K, 500000)
for _ in range(N):
    g, x = map(int, input().split())
    visited[x] = g


s = sum(visited[:2*K+1])
answer = s
for i in range(1000000-(2*K)):
    s = s - visited[i] + visited[i+2*K+1]
    answer = max(answer, s)

print(answer)
