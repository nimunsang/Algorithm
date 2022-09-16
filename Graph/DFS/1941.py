from collections import deque
from itertools import combinations

board = [list(input()) for _ in range(5)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
coords = [i for i in range(25)]


def is_connected(y, x):
    q = deque()
    q.append([y, x])
    visited[y][x] = 0
    cnt = 1
    som = 0
    while q:
        y, x = q.popleft()
        if board[y][x] == 'S':
            som += 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < 5 and 0 <= nx < 5 and visited[ny][nx] == 1:
                visited[ny][nx] = 0
                q.append([ny, nx])
                cnt += 1

    if cnt == 7 and som >= 4:
        return True

    return False


combination = combinations(coords, 7)
answer = 0
for comb in combination:
    visited = [[0] * 5 for _ in range(5)]
    for num in comb:
        y, x = num // 5, num % 5
        visited[y][x] = 1

    if is_connected(y, x):
        answer += 1

print(answer)
