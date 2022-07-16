import heapq

N = int(input())
board = [list(input().rstrip()) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def solve():
    heap = []
    heapq.heappush(heap, [0, 0, 0])
    visited = [[0] * N for _ in range(N)]
    visited[0][0] = 1
    while heap:
        weight, y, x = heapq.heappop(heap)
        if (y, x) == (N-1, N-1):
            return weight

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                visited[ny][nx] = 1
                if board[ny][nx] == '1':
                    heapq.heappush(heap, [weight, ny, nx])
                else:
                    heapq.heappush(heap, [weight+1, ny, nx])


print(solve())
