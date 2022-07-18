import heapq
import sys
input = sys.stdin.readline

N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort(key= lambda x: (x[0], x[1]))

heap = []

for i in range(N):
    S, T = lst[i]
    if not heap:
        heapq.heappush(heap, T)
    else:
        if S < heap[0]:
            heapq.heappush(heap, T)
        else:
            heapq.heappop(heap)
            heapq.heappush(heap, T)

print(len(heap))