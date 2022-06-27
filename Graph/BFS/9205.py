from collections import deque

T = int(input())
for _ in range(T):
    N = int(input())
    housex, housey = map(int, input().split())
    conv = [list(map(int, input().split())) for __ in range(N)]
    endx, endy = map(int, input().split())

    visited = [0]*N
    q = deque()
    q.append([housex, housey])
    while q:
        x, y = q.popleft()
        if abs(x-endx) + abs(y-endy) <= 1000:
            print("happy")
            break

        for i in range(N):
            if not visited[i]:
                nx, ny = conv[i]
                if abs(x-nx) + abs(y-ny) <= 1000:
                    q.append([nx, ny])
                    visited[i] = 1
    else:
        print("sad")

