import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
M = int(input())

dp = [0]
for i in range(N):
    dp.append(dp[i] + lst[i])

for i in range(M):
    start, end = map(int, input().split())
    print(dp[end]-dp[start-1])