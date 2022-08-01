X, Y = map(int, input().split())

def calc(son, mother):
    return (son * 100) // mother


Z = calc(Y, X)
target = Z + 1

start, end = 0, X+1
while start + 1 < end:
    mid = (start + end) // 2

    if calc(Y+mid, X+mid) >= target:
        end = mid

    else:
        start = mid

print(-1 if calc(Y, X) >= 99 else end)