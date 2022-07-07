from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
airArea = [[-1]*M for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def setOuterArea(day):
    q = deque()
    q.append([0, 0])
    removeList = []
    visited = [[0]*M for _ in range(N)]
    visited[0][0] = 1
    while q:
        y, x = q.popleft()
        if airArea[y][x] == -1:
            airArea[y][x] = day
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<M and not visited[ny][nx]:
                visited[ny][nx] = 1
                if graph[ny][nx] == 1:
                    removeList.append([ny, nx])
                    answer[-1] += 1
                else:
                    q.append([ny, nx])
    return removeList


answer = []
day = 0
while True:
    answer.append(0)
    removeList = setOuterArea(day)
    if not removeList:
        break
    for y, x in removeList:
        graph[y][x] = 0
    day += 1

print(day)
print(answer[-2])