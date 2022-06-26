N = int(input())
lst = list(map(int, input().split()))
target = int(input())


graph = [[] for _ in range(N)]
root = 0
for i in range(N):
    if lst[i] == -1:
        root = i
        continue

    graph[lst[i]].append(i)


leaf = 0
def dfs(v):
    global leaf
    if not graph[v]:
        leaf += 1
        return

    for next_v in graph[v]:
        if next_v == target and len(graph[v]) == 1:
            leaf += 1

        elif next_v != target:
            dfs(next_v)


if target == root:
    print(0)
else:
    dfs(root)
    print(leaf)
