import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
graph = [[0]*N for _ in range(H)]
for i in range(1, M+1):
    a, b = map(int, input().split())
    graph[a-1][b-1] = i
    graph[a-1][b] = i


def isBridgeLeft(y, x): # 왼쪽에 다리가 있는가?
    return True if x-1 >= 0 and graph[y][x-1] == graph[y][x] else False

def isBridgeRight(y, x): # 오른쪽에 다리가 있는가?
    return True if x+1 < N and graph[y][x+1] == graph[y][x] else False


def simulation():  # 사다리게임 시뮬레이션 ..
    for i in range(N):
        cury, curx = 0, i
        while cury < H:
            if graph[cury][curx] != 0: # 다리가 있다.
                if isBridgeLeft(cury, curx): # 왼쪽에 다리가 있다면
                    curx -= 1
                elif isBridgeRight(cury, curx): # 오른쪽에 다리가 있다면
                    curx += 1
            cury += 1

        if curx != i:
            return False
    return True


def dfs(start, c):
    global answer
    if c == cnt+1:
        if simulation():
            answer = c
        return

    for i in range(start, N*H):
        y, x = i//N, i%N
        if x == N-1:
            continue
        if graph[y][x] == 0 and isBridgeRight(y, x):
            graph[y][x] = M+c
            graph[y][x+1] = M+c
            dfs(i+1, c+1)
            graph[y][x] = 0
            graph[y][x+1] = 0


answer = -1
for cnt in range(4):
    dfs(0, 1)
    if answer != -1:
        break


if answer != -1:
    answer -= 1
print(answer)
