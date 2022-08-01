import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
S = int(input())

start, end = 0, max(lst)+1

while start + 1 < end:
    mid = (start + end) // 2

    summ = sum([min(num, mid) for num in lst])

    if summ > S:
        end = mid

    else:
        start = mid

print(start)