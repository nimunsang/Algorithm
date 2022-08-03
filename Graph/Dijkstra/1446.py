import sys
input = sys.stdin.readline

N, D = map(int, input().split())
dp = [i for i in range(D+1)]
graph = [list(map(int, input().split())) for _ in range(N)]
graph.sort(key=lambda x: (x[0], x[1]))

for a, b, c in graph:
    if b > D or b-a < c:
        continue

    dp[b] = min(dp[b], dp[a] + c)

    for i in range(1, D+1):
        dp[i] = min(dp[i-1] + 1, dp[i])

print(dp[-1])
