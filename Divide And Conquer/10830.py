N, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        arr[i][j] %= 1000


def calc(sub, ar):
    ret = [[0]*N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            tmp = 0
            for k in range(N):
                tmp += sub[row][k] * ar[k][col]
            ret[row][col] = tmp%1000
    return ret


def mult(sub, cnt):
    if cnt == 1:
        return sub

    sub = mult(sub, cnt//2)

    if cnt % 2:
        return calc(calc(sub, sub), arr)
    else:
        return calc(sub, sub)


answer = mult(arr, B)

for a in answer:
    print(*a)
