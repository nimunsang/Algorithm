import sys
import heapq
input = sys.stdin.readline

# 2 <= N <= 1000, 0 <= M <= 15*1000
N, M = map(int, input().split())
lst = list(map(int, input().split()))

# O(N)
heapq.heapify(lst)

# O(M) * 2 * O(logN) + 2 * O(logN) = O(MlogN) ==> 15000(log1000)
for _ in range(M):
    a, b = heapq.heappop(lst), heapq.heappop(lst)
    heapq.heappush(lst, a+b)
    heapq.heappush(lst, a+b)

# O(N)
print(sum(lst))

# 시간복잡도 : 15000 * log1000