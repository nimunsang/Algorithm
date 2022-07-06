N = int(input())

low = -1
high = 2**32

while low + 1 < high:
    mid = (low + high) // 2

    if mid**2 >= N:
        high = mid
    else:
        low = mid

print(high)


