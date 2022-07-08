from copy import deepcopy
from collections import deque
from itertools import combinations


N, M, D = map(int, input().split())
board = deque([list(map(int, input().split())) for _ in range(N)])
Enemy = sum(map(lambda x: x.count(1), board))
dx = [-1, 0, 1]
dy = [0, -1, 0]


def attack(x):
    visited = [[0]*M for _ in range(N)]
    q = deque()
    q.append([N-1, x, 1])
    visited[N-1][x] = 1
    while q:
        y, x, distance = q.popleft()
        if distance > D:
            break

        if simulationBoard[y][x] == 1:
            return y, x

        for i in range(3):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny and 0 <= nx < M and not visited[ny][nx]:
                visited[ny][nx] = 1
                q.append([ny, nx, distance+1])

    return -1


def goDown():
    global remainedEnemyCount
    lastLineEnemyCount = simulationBoard[-1].count(1)
    remainedEnemyCount -= lastLineEnemyCount
    simulationBoard.pop()
    simulationBoard.appendleft([0]*M)


def simulation(archers):
    global remainedEnemyCount
    killed = 0
    while remainedEnemyCount > 0:
        attackedEnemys = set()
        for archer in archers:
            attackedEnemy = attack(archer)
            if attackedEnemy == -1:
                continue
            attackedEnemys.add(attackedEnemy)

        for y, x in attackedEnemys:
            remainedEnemyCount -= 1
            killed += 1
            simulationBoard[y][x] = 0

        goDown()

    return killed


answer = 0
archerPosition = combinations(range(M), 3)

for archers in archerPosition:
    simulationBoard = deepcopy(board)
    remainedEnemyCount = deepcopy(Enemy)
    killedEnemyCount = simulation(archers)
    answer = max(answer, killedEnemyCount)

print(answer)

