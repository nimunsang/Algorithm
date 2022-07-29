from collections import deque
import sys
input = sys.stdin.readline

W, H = map(int, input().split())
board = [list(input().rstrip()) for _ in range(H)]

target = []
for i in range(H):
    for j in range(W):
        if board[i][j] == 'C':
            target.append([i, j])

start = target[0]
end = target[1]


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
q = deque()
visited = [[-1] * W for _ in range(H)]
q.append([start[0], start[1], 0])
visited[start[0]][start[1]] = 0


while q:
    y, x, cnt = q.popleft()
    if (y, x) == (end[0], end[1]):
        print(visited[y][x])
        break

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        while 0 <= ny < H and 0 <= nx < W and \
            board[ny][nx] != '*' and (visited[ny][nx] == -1 or cnt <= visited[ny][nx]):
            visited[ny][nx] = cnt
            ny += dy[i]
            nx += dx[i]
            q.append([ny-dy[i], nx-dx[i], cnt+1])
