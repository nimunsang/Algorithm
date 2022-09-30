import sys
input = sys.stdin.readline

N = int(input())
houses = list(map(int, input().split()))
houses.sort()
dist = 100000 * 200000
left, right = 0, sum(houses[1:]) - houses[0] * (N-1)
leftcnt, rightcnt = 0, N-1
answer = houses[0]
for i in range(1, N):
    tmp = houses[i] - houses[i-1]
    leftcnt += 1
    left += tmp * leftcnt
    right -= tmp * rightcnt
    rightcnt -= 1
    if left + right < dist:
        dist = left + right
        answer = houses[i]



print(answer)
