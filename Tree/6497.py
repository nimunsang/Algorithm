import heapq
import sys
input = sys.stdin.readline


def prim():
    graph = [[] for _ in range(N)]
    s = 0
    for _ in range(N):
        a, b, c = map(int, input().split())
        s += c
        graph[a].append([c, b])
        graph[b].append([c, a])


    heap = []
    visited = [0] * N
    heapq.heappush(heap, [0, 0])
    answer = 0
    while heap:
        d, v = heapq.heappop(heap)
        if not visited[v]:
            visited[v] = 1
            answer += d

        for next_d, next_v in graph[v]:
            if not visited[next_v]:
                heapq.heappush(heap, [next_d, next_v])

    print(s-answer)


def kruskal():
    graph = []
    s = 0
    for _ in range(N):
        a, b, c = map(int, input().split())
        s += c
        graph.append([a, b, c])
        graph.append([b, a, c])

    parent = [x for x in range(M)]
    rank = [0 for x in range(M)]

    graph.sort(key=lambda x: x[2])

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
            parent[roota] = rootb
            if rank[roota] == rank[rootb]:
                rank[roota] += 1

    answer = 0
    for a, b, c in graph:
        if find(a) != find(b):
            union(a, b)
            answer += c

    print(s-answer)



while True:
    M, N = map(int, input().split())
    if M == 0 and N == 0:
        break

    # prim()
    kruskal()

