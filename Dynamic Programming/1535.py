N = int(input())
health = list(map(int, input().split()))
happy = list(map(int, input().split()))

dp = [0] * 101

for i in range(N):
    heal = health[i]
    hap = happy[i]
    for j in range(100, heal-1, -1):
        dp[j] = max(dp[j], dp[j-heal] + hap)

print(max(dp[:-1]))