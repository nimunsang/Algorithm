from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visited = [[0] * M for _ in range(N)]


def bfs(y, x):
    q = deque()
    q.append([y, x])
    visited[y][x] = 1
    area = 0
    while q:
        y, x = q.popleft()
        area += 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and arr[ny][nx] == 1:
                q.append([ny, nx])
                visited[ny][nx] = 1

    return area


maxarea = 0
cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] and not visited[i][j]:
            maxarea = max(maxarea, bfs(i, j))
            cnt += 1


print(cnt)
print(maxarea)
