from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def removeCheese(visited):
    removeCnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] >= 2:
                removeCnt += 1
                arr[i][j] = 0

    return removeCnt


def setOuter(): # 바깥 지역을 0으로 초기화 해주고, 없어지는 치즈 수를 리턴하는 함수
    q = deque()
    q.append([0, 0])
    visited = [[0]*M for _ in range(N)]
    visited[0][0] = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if arr[ny][nx] == 0 and not visited[ny][nx]:
                    visited[ny][nx] = 1
                    q.append([ny, nx])
                elif arr[ny][nx] == 1:
                    visited[ny][nx] += 1

    removedCheese = removeCheese(visited)
    return removedCheese


day = 0
while True:
    removedCnt = setOuter()
    if removedCnt == 0:
        break
    day += 1

print(day)
