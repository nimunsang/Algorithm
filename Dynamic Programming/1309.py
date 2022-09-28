N = int(input())
MOD = 9901
dp = [[0, 0, 0] for _ in range(N)]
dp[0] = [1, 1, 1]
for i in range(1, N):
    dp[i][0] = sum(dp[i-1]) % MOD
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % MOD
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % MOD

print(sum(dp[N-1]) % MOD)