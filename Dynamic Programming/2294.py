N, K = map(int, input().split())
values = [int(input()) for _ in range(N)]

dp = [float('inf')] * (K+1)
dp[0] = 0

for value in values:
    if value > K:
        continue
    for i in range(value, K+1):
        dp[i] = min(dp[i], dp[i-value] + 1)

answer = dp[-1]
print(-1 if answer == float('inf') else answer)