N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
visited[0][0] = 1
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for y in range(N):
    for x in range(N):
        length = board[y][x]
        if length == 0:
            continue

        if visited[y][x]:
            for ny, nx in [[y + length, x], [y, x + length]]:
                if ny < N and nx < N:
                    visited[ny][nx] = 1
                    dp[ny][nx] += dp[y][x]

print(dp[-1][-1])
