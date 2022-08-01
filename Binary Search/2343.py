N, M = map(int, input().split())
lst = list(map(int, input().split()))


start, end = max(lst)-1, 10**9+1

while start + 1 < end:
    mid = (start + end) // 2

    maxi = 0
    subtotal = 0
    cnt = 0
    for a in lst:
        subtotal += a
        if subtotal > mid:
            maxi = max(maxi, subtotal-a)
            subtotal = a
            cnt += 1

    maxi = max(maxi, subtotal)
    if M > cnt:
        end = mid
    else:
        start = mid

print(end)


