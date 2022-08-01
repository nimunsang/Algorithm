import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [int(input()) for _ in range(N)]

start, end = max(lst)-1, sum(lst)+1

while start + 1 < end:
    mid = (start + end) // 2

    cnt = 1
    subtotal = 0
    for a in lst:
        subtotal += a
        if subtotal > mid:
            cnt += 1
            subtotal = a

    if cnt > M:
        start = mid
    else:
        end = mid

print(end)