import sys
input = sys.stdin.readline


N, K, B = map(int, input().split())
lst = [0] * N

for i in range(B):
    num = int(input())
    lst[num-1] = 1

dp = [0] * N
dp[0] = lst[0]

for i in range(1, N):
    if lst[i] == 1:
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = dp[i-1]


answer = N
for i in range(N-K+1):
    answer = min(answer, dp[i+K-1] - dp[i])

print(answer)
