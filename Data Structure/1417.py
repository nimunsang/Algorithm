import heapq

N = int(input())
dasom = int(input())
lst = [int(input()) for _ in range(N-1)]
heap = []
for l in lst:
    heapq.heappush(heap, -l)

if N == 1:
    print(0)
else:
    cnt = 0

    while -heap[0] >= dasom:
        l = heapq.heappop(heap)
        heapq.heappush(heap, l+1)
        dasom += 1
        cnt += 1

    print(cnt)