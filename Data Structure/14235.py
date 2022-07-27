import heapq

N = int(input())

heap = []

for _ in range(N):
    cmd = list(map(int, input().split()))
    if cmd == [0]:
        if not heap:
            print(-1)
        else:
            print(-heapq.heappop(heap))

    else:
        for c in cmd[1:]:
            heapq.heappush(heap, -c)