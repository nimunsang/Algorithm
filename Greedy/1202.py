import heapq
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dia = [list(map(int, input().split())) for _ in range(N)]
bag = [int(input()) for _ in range(K)]
bag.sort()
dia.sort()

heap = []

answer = 0
for limit in bag:
    while dia and dia[0][0] <= limit:
        heapq.heappush(heap, -dia[0][1])
        heapq.heappop(dia)

    if heap:
        answer += heapq.heappop(heap)
    elif not dia:
        break

print(-answer)

