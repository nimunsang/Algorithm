import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [int(input()) for _ in range(M)]

low = 0
high = 10**9+1

while low + 1 < high:
    mid = (low + high) // 2

    tmp = 0
    for a in lst:
        if a%mid == 0:
            tmp += a // mid
        else:
            tmp += a // mid + 1

    if N >= tmp:
        high = mid
    else:
        low = mid

print(high)
