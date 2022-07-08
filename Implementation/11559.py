from collections import deque
N, M = 12, 6
field = [list(input()) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def checkAndCrash(visited, y, x):
    if visited[y][x]:
        return 0

    visited[y][x] = 1
    removeList = [[y, x]]
    isCrashed = 0
    q = deque()
    q.append([y, x])
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < M and 0 <= ny < N:
                if not visited[ny][nx] and field[y][x] == field[ny][nx]:
                    visited[ny][nx] = 1
                    removeList.append([ny, nx])
                    q.append([ny, nx])

    if len(removeList) >= 4:
        for y, x in removeList:
            field[y][x] = '.'
        isCrashed = 1

    return isCrashed


def goDown():
    for x in range(M):
        for y in range(N-1, -1, -1):
            if field[y][x] != '.':
                target = y
                while target+1 < N and field[target+1][x] == '.':
                    target += 1
                field[target][x], field[y][x] = field[y][x], field[target][x]


def simulation():
    visited = [[0]*6 for _ in range(N)]
    isCrashed = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] != '.':
                isCrashed += checkAndCrash(visited, i, j)

    return isCrashed


answer = 0
while simulation():
    answer += 1
    goDown()

print(answer)

