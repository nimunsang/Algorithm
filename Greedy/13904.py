N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort(key=lambda x: x[1], reverse=True)

arr = [0] * 1001

for d, w in lst:
    for i in range(d, 0, -1):
        if arr[i] < w:
            arr[i] = w
            break

print(sum(arr))
