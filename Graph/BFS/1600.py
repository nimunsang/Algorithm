"""
2
9 2
0 0 1 1 0 0 1 1 0
0 0 1 0 0 0 1 0 0
answer : 7

1
5 3
0 1 0 0 0
0 1 0 1 0
0 0 0 1 0
answer : 6

1
5 5
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 1 1
0 0 0 1 0
answer : 6

1
4 4
0 0 0 0
1 0 0 0
0 0 1 0
0 1 0 0
answer : 4
"""

from collections import deque
import sys
input = sys.stdin.readline


K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]
horse_directions = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2))
adj_directions = ((-1, 0), (0, 1), (0, -1), (1, 0))
visited = [[[0] * (K+1) for __ in range(W)] for _ in range(H)]

def bfs():
    if W == H == 1:
        return 0

    sy, sx, horse_cnt, cnt = 0, 0, 0, 0

    start = (sy, sx, horse_cnt, cnt)
    q = deque()
    q.append(start)

    while q:
        y, x, horse_cnt, cnt = q.popleft()
        if y == H-1 and x == W-1:
            return cnt

        for i in range(4):
            dy, dx = adj_directions[i]
            ny = y + dy
            nx = x + dx
            if 0 <= ny < H and 0 <= nx < W and arr[ny][nx] == 0 \
                    and not visited[ny][nx][horse_cnt]:
                q.append((ny, nx, horse_cnt, cnt + 1))
                visited[ny][nx][horse_cnt] = 1

        for i in range(8):
            dy, dx = horse_directions[i]
            ny = y + dy
            nx = x + dx
            if 0 <= ny < H and 0 <= nx < W and arr[ny][nx] == 0 \
                    and horse_cnt < K and not visited[ny][nx][horse_cnt + 1]:
                q.append((ny, nx, horse_cnt + 1, cnt + 1))
                visited[ny][nx][horse_cnt + 1] = 1
    return -1


print(bfs())
