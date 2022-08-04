from collections import deque

S = int(input())

visited = [[0] * (S+1) for _ in range(S+1)]
q = deque()
q.append([1, 1, 1])
visited[1][1] = 1
while q:
    v, cnt, clip = q.popleft()

    if v == S:
        print(cnt)
        break

    if not visited[v][clip]:
        visited[v][clip] = 1
        q.append([v, cnt+1, v])

    if v + clip <= S and not visited[v+clip][clip]:
        q.append([v+clip, cnt+1, clip])

    if 0 <= v-1 and not visited[v-1][clip]:
        q.append([v-1, cnt+1, clip])


