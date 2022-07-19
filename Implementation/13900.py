import sys
input = sys.stdin.readline


N = int(input())
lst = list(map(int, input().split()))
s = sum(lst)
answer = 0
for i in range(N):
    answer += (s-lst[i]) * lst[i]
print(answer//2)