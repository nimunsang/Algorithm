N, M = map(int, input().split())
square = [list(input()) for _ in range(N)]

sizeMax = min(N, M)
answer = 0

for size in range(sizeMax-1, 0, -1):
    for i in range(N):
        for j in range(M):
            if i+size < N and j+size < M and \
                square[i][j] == square[i+size][j] == square[i][j+size] == square[i+size][j+size]:
                answer = size
                break

        if answer:
            break
    if answer:
        break

print((answer+1)**2)
