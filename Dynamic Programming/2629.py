import sys
input = sys.stdin.readline


N = int(input())
choo = list(map(int, input().split()))
M = int(input())
marble = list(map(int, input().split()))

C = sum(choo)
dp = [[0]*(2*C+1) for _ in range(N)]


for i in range(N):
    dp[i][C+choo[i]] = 1
    dp[i][C-choo[i]] = 1
    for j in range(2*C+1):
        if dp[i-1][j] == 1:
            dp[i][j] = 1
            dp[i][j-choo[i]] = 1
            dp[i][j+choo[i]] = 1

answer = set()
for i in range(2*C+1):
    if dp[-1][i]:
        answer.add(abs(i-C))

print(*list(map(lambda x: "Y" if x in answer else "N", marble)))
