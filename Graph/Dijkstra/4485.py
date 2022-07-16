from collections import deque
import sys
import heapq
input = sys.stdin.readline


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def solve():
    q = deque()
    q.append([0, 0])
    dp[0][0] = graph[0][0]
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and dp[ny][nx] > dp[y][x] + graph[ny][nx]:
                dp[ny][nx] = dp[y][x] + graph[ny][nx]
                q.append([ny, nx])


def dijkstra():
    heap = []
    heapq.heappush(heap, [graph[0][0], 0, 0])
    while heap:
        subtotal, y, x = heapq.heappop(heap)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                next_cost = subtotal + graph[ny][nx]
                if dp[ny][nx] > next_cost:
                    dp[ny][nx] = next_cost
                    heapq.heappush(heap, [next_cost, ny, nx])


idx = 1
while True:
    N = int(input())
    if N == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(N)]
    dp = [[float('inf')]*N for _ in range(N)]
    dijkstra()
    #solve()
    print(f"Problem {idx}: {dp[-1][-1]}")
    idx += 1
