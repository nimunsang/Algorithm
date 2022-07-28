import math
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
road = [list(map(int, input().split())) for _ in range(M)]


def kruskal():
    parent = [x for x in range(N+1)]
    rank = [0 for x in range(N+1)]

    graph = []
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            graph.append([i, j, math.dist(board[i-1], board[j-1])])

    graph.sort(key=lambda x: x[2])

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        roota = find(a)
        rootb = find(b)

        if rank[roota] > rank[rootb]:
            parent[rootb] = roota
        else:
            parent[roota] = rootb
            if rank[roota] == rank[rootb]:
                rank[roota] += 1

    for a, b in road:
        union(a, b)

    cost = 0
    for a, b, c in graph:
        if find(a) != find(b):
            union(a, b)
            cost += c

    print("{:.2f}".format(cost))

kruskal()

