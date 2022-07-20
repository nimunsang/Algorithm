N, M = map(int, input().split())

start, end = 0, 1
branch = 1
while branch < M:
    print(start, end)
    if N-start == M:
        end += 1
        branch += 1
    else:
        start += 1
        end += 1

