import sys
input = sys.stdin.readline

# sparse graph 이므로, Kruskal Algortihm 사용

N, M = map(int, input().split())
school = list(input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
graph.sort(key=lambda x: x[2])
parent = [x for x in range(N+1)]
rank = [0 for x in range(N+1)]


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


cost, cnt = 0, 0
for a, b, c in graph:
    if find(a) != find(b) and school[a-1] != school[b-1]:
        union(a, b)
        cost += c
        cnt += 1

if cnt == N-1:
    print(cost)
else:
    print(-1)
