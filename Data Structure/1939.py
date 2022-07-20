import sys
input = sys.stdin.readline


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
lst = [list(map(int, input().split())) for _ in range(M)]
S, E = set(map(int, input().split()))
lst.sort(key=lambda x: -x[2])

parent = list(range(N + 1))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x


for a, b, cost in lst:
    union(a, b)
    if find(parent[S]) == find(parent[E]):
        print(cost)
        break
