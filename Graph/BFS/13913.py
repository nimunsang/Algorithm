from collections import deque

N, K = map(int, input().split())

q = deque()
q.append([N, 0])
visited = [0] * 200001
dic = {i : -1 for i in range(200001)}
visited[N] = 1
while q:
    v, tim = q.popleft()
    if v == K:
        print(tim)
        path = [K]
        next_v = K
        while True:
            next_v = dic[next_v]
            if next_v == -1:
                break

            path.append(next_v)

        print(*list(reversed(path)))
        break

    if v+1 <= 100000 and not visited[v+1]:
        visited[v+1] = 1
        dic[v+1] = v
        q.append([v+1, tim+1])

    if 0 <= v-1 and not visited[v-1]:
        visited[v-1] = 1
        dic[v-1] = v
        q.append([v-1, tim+1])

    if v <= 100000 and not visited[v*2]:
        visited[v*2] = 1
        dic[v*2] = v
        q.append([v*2, tim+1])



