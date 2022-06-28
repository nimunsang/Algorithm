from functools import reduce

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
lst = []
for i in range(N):
    if i == 0:
        lst.append(matrix[i][0])
        lst.append(matrix[i][1])
        continue
    lst.append(matrix[i][1])


def mult(arr):
    return reduce(lambda x, y: x*y, arr)


lst_length = N+1
dp = [[float('inf')]*lst_length for _ in range(lst_length)]

for length in range(1, lst_length):
    for i in range(lst_length-length):
        if length == 1:
            dp[i][i+length] = 0
            continue

        elif length == 2:
            dp[i][i+length] = mult(lst[i:i+length+1])
            continue

        for j in range(i+1, i+length):
            dp[i][i+length] = min(dp[i][i+length], dp[i][j]+dp[j][i+length]+lst[i]*lst[j]*lst[i+length])

print(dp[0][-1])