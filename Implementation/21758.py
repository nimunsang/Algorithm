from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
dp = [lst[0]]
for i in range(1, N):
    dp.append(dp[i-1] + lst[i])

tmp = float('inf')
for i in range(1, N):
    tmp = min(tmp, lst[i]+dp[i])

answer = 2*dp[-1] - (lst[0]+tmp)

for center in range(1, N-1):
    answer = max(answer, dp[center]-dp[0] + dp[-2]-dp[center-1])

dp = deque([lst[-1]])
for i in range(N-2, -1, -1):
    dp.appendleft(dp[0] + lst[i])

tmp = float('inf')
for i in range(N-2, -1, -1):
    tmp = min(tmp, dp[i]+lst[i])

answer = max(answer, 2*dp[0] - (lst[-1]+tmp))

print(answer)