from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def check(y, x):
    q = deque()
    q.append((y, x, 0))
    visited = [[0] * M for _ in range(N)]
    visited[y][x] = 1
    max_dist = 0
    while q:
        y, x, dist = q.popleft()
        max_dist = max(dist, max_dist)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if not visited[ny][nx] and arr[ny][nx] == 'L':
                    q.append((ny, nx, dist+1))
                    visited[ny][nx] = 1

    return max_dist


visited = [[0] * M for _ in range(N)]
answer = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            answer = max(answer, check(i, j))

print(answer)

