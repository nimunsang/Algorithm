from collections import deque
import sys
input = sys.stdin.readline


N = int(input())
M = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
lst = list(map(int, input().split()))


# def solve_with_bfs():
#     q = deque()
#     start = lst[0]-1
#     q.append(start)
#     visited = [0] * (N+1)
#     visited[start] = 1
#     visited_list = set()
#     while q:
#         start = q.popleft()
#         visited_list.add(start)
#         for i in range(N):
#             if not visited[i] and graph[start][i]:
#                 visited[i] = 1
#                 q.append(i)
#
#
#     for a in lst:
#         if a-1 not in visited_list:
#             print("NO")
#             break
#
#     else:
#         print("YES")
#
#
# solve_with_bfs()


def solve_with_UNION_FIND():
    parent = [i for i in range(N)]

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

    for i in range(N):
        for j in range(N):
            if graph[i][j]:
                union(i, j)


    for i in range(1, M):
        if parent[lst[i]-1] != parent[lst[0]-1]:
            print("NO")
            break
    else:
        print("YES")

solve_with_UNION_FIND()













