from math import sqrt

N = int(input())

dp = [float('inf')] * (N+1)
for i in range(1, N+1):
    if int(sqrt(i)) == sqrt(i):
        dp[i] = 1
        continue

    for j in range(int(sqrt(i)), 0, -1):
        dp[i] = min(dp[i], dp[i-j**2] + 1)

print(dp[-1])