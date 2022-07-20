import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [0] * (N+1)
visited[1] = 1

def dfs(start, depth):
    global answer

    is_leaf = 1
    for next_node in tree[start]:
        if not visited[next_node]:
            is_leaf = 0
            visited[next_node] = 1
            dfs(next_node, depth+1)

    if is_leaf:
        answer += depth

answer = 0
dfs(1, 0)

print("Yes" if answer % 2 == 1 else "No")