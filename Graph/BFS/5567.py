from collections import deque

N = int(input())
M = int(input())
graph = [[] for _ in range(N)]
visited = [0] * N
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)


def bfs(start):
    global answer
    q = deque()
    q.append([start, 0])
    while q:        
        v, cnt = q.popleft()
        for next_v in graph[v]:
            if not visited[next_v] and cnt <= 1:
                q.append([next_v, cnt+1])
                visited[next_v] = 1
                answer += 1


answer = 0
visited[0] = 1
bfs(0)
print(answer)