import sys
input = sys.stdin.readline


N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]


def find(x):
    while x != parent[x]:
        x = find(parent[x])
    return x


def union(a, b):
    roota = find(a)
    rootb = find(b)
    if roota == rootb:
        return

    if roota > rootb:
        parent[roota] = rootb
    else:
        parent[rootb] = roota

direction = ['U', 'D', 'L', 'R']
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dir_move = dict(zip(direction, move))
parent = [x for x in range(N*M)]
for y in range(N):
    for x in range(M):
        dy, dx = dir_move[arr[y][x]]
        ny, nx = y + dy, x + dx
        union(ny * M + nx, y * M + x)


for i in range(M*N):
    parent[i] = find(i)

print(len(set(parent)))
