from collections import deque

F, S, G, U, D = map(int, input().split())

q = deque([[S, 0]])
visited = [0] * (F+1)
visited[S] = 1

while q:
    floor, cnt = q.popleft()
    if floor == G:
        print(cnt)
        break
    for next in {U, D}:
        if next == U:
            next_floor = floor + next
        else:
            next_floor = floor - next

        if 1 <= next_floor <= F and not visited[next_floor] :
            visited[next_floor] = 1
            q.append([next_floor, cnt+1])

else:
    print("use the stairs")
