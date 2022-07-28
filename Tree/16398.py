import heapq
import sys
input = sys.stdin.readline


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]


def kruskal():
    parent = [x for x in range(N)]
    rank = [0 for x in range(N)]
    graph = []

    for i in range(N):
        for j in range(i+1, N):
            graph.append([i, j, board[i][j]])

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
                rank[rootb] += 1

    cost = 0
    cnt = 0
    for a, b, c in graph:
        if find(a) != find(b):
            union(a, b)
            cost += c
            cnt += 1
            if cnt == N-1:
                break

    print(cost)


def prim():
    heap = []
    heapq.heappush(heap, [0, 0])
    visited = [0] * N

    graph = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            graph[i].append([board[i][j], j])
            graph[j].append([board[i][j], i])

    cost = 0
    while heap:
        d, v = heapq.heappop(heap)
        if not visited[v]:
            visited[v] = 1
            cost += d
            for next_d, next_v in graph[v]:
                if not visited[next_v]:
                    heapq.heappush(heap, [next_d, next_v])

    print(cost)


# kruskal()
prim()