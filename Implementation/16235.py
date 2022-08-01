from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
nutrition = [[5] * N for _ in range(N)]
trees = [[deque() for _ in range(N)] for __ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)


def spring_summer():
    global trees
    for i in range(N):
        for j in range(N):
            T = len(trees[i][j])
            for k in range(T):
                old = trees[i][j][k]
                if nutrition[i][j] - old < 0:
                    for _ in range(k, T):
                        nutrition[i][j] += trees[i][j].pop() // 2
                    break
                else:
                    nutrition[i][j] -= old
                    trees[i][j][k] += 1


def fall_winter():
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(N):
        for j in range(N):
            for k in range(len(trees[i][j])):
                old = trees[i][j][k]
                if old % 5 == 0:
                    for l in range(8):
                        ny = i + dy[l]
                        nx = j + dx[l]
                        if 0 <= ny < N and 0 <= nx < N:
                            trees[ny][nx].appendleft(1)

            nutrition[i][j] += A[i][j]


for _ in range(K):
    spring_summer()
    fall_winter()


answer = 0
for i in range(N):
    for j in range(N):
        answer += len(trees[i][j])

print(answer)