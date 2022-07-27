import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]
dp[0][0] = board[0][0]
dx = [1, 1, 0]
dy = [0, 1, 1]


for i in range(N):
    for j in range(M):
        for k in range(3):
            ny = i + dy[k]
            nx = j + dx[k]
            if 0 <= ny < N and 0 <= nx < M:
                dp[ny][nx] = max(dp[ny][nx], dp[i][j] + board[ny][nx])

print(dp[-1][-1])

