from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(v):
    q = deque()
    q.append(v)
    visited = [0] * (N+1)
    visited[v] = 1
    cnt = 0
    while q:
        v = q.popleft()
        for next_v in graph[v]:
            if not visited[next_v]:
                visited[next_v] = 1
                q.append(next_v)
                cnt += 1

    return cnt


answer = []
for i in range(1, N+1):
    answer.append(bfs(i))

maxx = max(answer)

res = []
for i in range(N):
    if answer[i] == maxx:
        res.append(i+1)

print(*res)



