import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    dp = [lst[0]]

    for i in range(1, N):
        dp.append(max(dp[i-1] + lst[i], lst[i]))

    print(max(dp))