import heapq
from math import sqrt

N = int(input())
stars = [list(map(float, input().split())) for _ in range(N)]


def kruskal():
    graph = []
    for i in range(N-1):
        for j in range(i+1, N):
            d = sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2)
            graph.append([i, j, d])
            graph.append([j, i, d])

    graph.sort(key=lambda x: x[2])

    parent = [x for x in range(N)]
    rank = [0 for i in range(N)]

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]


    def union(a, b):
        roota = find(a)
        rootb = find(b)

        if rank[roota] > rank[rootb]:
            parent[rootb] = roota
        else:
            parent[rootb] = roota
            if rank[roota] == rank[rootb]:
                rank[rootb] += 1


    answer = 0
    for a, b, dist in graph:
        if find(a) != find(b):
            union(a, b)
            answer += dist

    print(answer)



def prim():
    graph = [[] * N for _ in range(N)]
    for i in range(N-1):
        for j in range(i+1, N):
            d = sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2)
            graph[i].append([d, j])
            graph[j].append([d, i])

    heap = []
    visited = [0] * N
    heapq.heappush(heap, [0, 0])
    answer = 0
    while heap:
        d, v = heapq.heappop(heap)
        if not visited[v]:
            answer += d
            visited[v] = 1
            for next_d, next_v in graph[v]:
                if not visited[next_v]:
                    heapq.heappush(heap, [next_d, next_v])

    print(answer)


kruskal()